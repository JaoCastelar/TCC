import pandas as pd
import numpy as np
import torch
from sklearn.utils import shuffle
from torch.optim.lr_scheduler import ReduceLROnPlateau
import matplotlib.pyplot as plt
import sys

# Criar um modelo de Rede Neural
class Net(torch.nn.Module):
  def __init__(self, input_size, hidden_size, output_size):
    super(Net, self).__init__()
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.output_size = output_size
    self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size) #full connected
    self.relu = torch.nn.ReLU() #(0, infinito)
    
    self.dropout = torch.nn.Dropout(0.3)
    
    self.fc2 = torch.nn.Linear(self.hidden_size, self.output_size)
    self.sigmoid = torch.nn.Sigmoid() #(0, 1)
  def forward(self, x):
    hidden = self.fc1(x)
    relu = self.relu(hidden)
    
    relu = self.dropout(relu)
    
    output = self.fc2(relu)
    output = self.sigmoid(output)
    return output

df = pd.read_csv('base_nba_final.csv')

df = df.drop(['Unnamed: 0'], axis=1)

df = df.drop(['Match Up', 'a.Match Up', 'Game Date', 'a.Game Date', '+/-', 'a.+/-'], axis=1)

dfNome = df[['Team', 'a.Team']]

df = df.drop(['Team', 'a.Team'], axis=1)

df2 = pd.DataFrame(columns=list(['Home', 'Away']))
for i in range(df.shape[0]):
  if df['W/L'][i] == "W" and df['a.W/L'][i] == "L":
    df2.loc[i] = [1,0]
  elif df['W/L'][i] == "L" and df['a.W/L'][i] == "W":
    df2.loc[i] = [0,1]
  else:
    df2.loc[i] = [9,9]

df = df.drop(['W/L', 'a.W/L'], axis=1)

df = df.drop(['PTS', 'a.PTS'], axis = 1)

# df = df.drop(['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%'], axis = 1)

df = df.drop(['FGM', 'FG%', '3PM', '3P%', 'FTM', 'FT%', 'a.FGM', 'a.FG%', 'a.3PM', 'a.3P%', 'a.FTM', 'a.FT%'], axis = 1)

# df = df.drop(['FGM', '3PM', 'FTM', 'a.FGM', 'a.3PM', 'a.FTM'], axis = 1)

for column in df:
  try:
    if df[column].max() < 1:
      df[column] = df[column] / 1
    elif df[column].max() < 10:
      df[column] /= 10
    elif df[column].max() < 100:
      df[column] /= 100
    elif df[column].max() < 1000:
      df[column] /= 1000
    elif df[column].max() < 10000:
      df[column] /= 10000
    elif df[column].max() < 100000:
      df[column] /= 100000
    elif df[column].max() < 1000000:
      df[column] /= 1000000
    else:
      print('Erro')
  except:
    print('Exception')

df

dfNome, df, df2 = shuffle(dfNome, df, df2)

df2 = df2.astype('float64')
df_treino = df.iloc[:1160]
df_teste = df.iloc[1160:]
df2_treino = df2.iloc[:1160]
df2_teste = df2.iloc[1160:]

entrada_treino = torch.FloatTensor(df_treino.values)
entrada_teste = torch.FloatTensor(df_teste.values)
saida_treino = torch.FloatTensor(df2_treino.values)
saida_teste = torch.FloatTensor(df2_teste.values)

print(entrada_treino.size())
print(saida_treino.size())
input_size = entrada_treino.size()[1]
hidden_size = 42
output_size = saida_treino.size()[1]
modelo = Net(input_size, hidden_size, output_size)
print(modelo)

# Configurações do modelo
criterion = torch.nn.MSELoss() # Mean Square Error
optimizer = torch.optim.SGD(modelo.parameters(), lr = 0.16, momentum = 0.99)


scheduler = ReduceLROnPlateau(optimizer, 'min', patience=500, factor=0.5, verbose=True)


#Treinar o modelo

epochs = 10000 # Quantidade de épocas de treinamento

errors = [] # Criando um array vazio para guardar os erros de cada epoca

# for epoch in range(0, epochs+1):
#   optimizer.zero_grad()
#   # Forward pass
#   y_pred = modelo(entrada_treino)
#   # Compute Loss
#   loss = criterion(y_pred.squeeze(), saida_treino)
#   errors.append(loss.item())
#   if epoch % 1000 == 0:
#     print('Epoch {}: train loss: {}'.format(epoch, loss.item()))
#   # Backward pass
#   loss.backward()
#   optimizer.step()

for epoch in range(0, epochs + 1):
  optimizer.zero_grad()
  y_pred = modelo(entrada_treino)
  loss = criterion(y_pred.squeeze(), saida_treino)
  errors.append(loss.item())
  if epoch % 1000 == 0:
      y_pred_test = modelo(entrada_teste)
      test_loss = criterion(y_pred_test.squeeze(), saida_teste)
      print('Epoch {}: train loss: {} | test loss: {}'.format(epoch, loss.item(), test_loss.item()))
      # Ajustar learning rate dinamicamente
      scheduler.step(test_loss)
  loss.backward()
  optimizer.step()

np.set_printoptions(suppress=True)
np.set_printoptions(threshold=sys.maxsize)
torch.set_printoptions(threshold=sys.maxsize)

# Rodar a rede com os dados de teste, os dados que a rede nunca viu
y_pred = modelo(entrada_teste)
print(torch.round(y_pred, decimals=2)) # valor previsto pela rede
print(saida_teste) # valor real

# Quantidade de erros e acertos
print(y_pred.argmax(1))
print(saida_teste.argmax(1))
erros = torch.count_nonzero(torch.sub(y_pred.argmax(1), saida_teste.argmax(1)))
acertos = y_pred.shape[0] - erros
print(f' Acertos: {acertos} / Erros: {erros}')



df_jogos = pd.read_csv('jogos_noite_final.csv')

df_times = pd.read_csv('time_jogos_final.csv')

# df_jogos = df_jogos.drop(['Unnamed: 0'], axis=1)

# df_times = df_times.drop(['Unnamed: 0'], axis=1)

# df_jogos = df_jogos.drop(['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%'], axis = 1)

df_jogos = df_jogos.drop(['FGM', 'FG%', '3PM', '3P%', 'FTM', 'FT%', 'a.FGM', 'a.FG%', 'a.3PM', 'a.3P%', 'a.FTM', 'a.FT%'], axis = 1)

# df_jogos = df_jogos.drop(['FGM', '3PM', 'FTM', 'a.FGM', 'a.3PM', 'a.FTM'], axis = 1)

for column in df_jogos:
  try:
    if df_jogos[column].max() < 1:
      df_jogos[column] = df_jogos[column] / 1
    elif df_jogos[column].max() < 10:
      df_jogos[column] /= 10
    elif df_jogos[column].max() < 100:
      df_jogos[column] /= 100
    elif df_jogos[column].max() < 1000:
      df_jogos[column] /= 1000
    elif df_jogos[column].max() < 10000:
      df_jogos[column] /= 10000
    elif df_jogos[column].max() < 100000:
      df_jogos[column] /= 100000
    elif df_jogos[column].max() < 1000000:
      df_jogos[column] /= 1000000
    else:
      print('Erro')
  except:
    print('Exception')
    
# jogo1 = shuffle(df_jogos)

jogo1 = torch.FloatTensor(df_jogos.values)

# np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=sys.maxsize)
# torch.set_printoptions(threshold=sys.maxsize)

# Rodar a rede com os dados de teste, os dados que a rede nunca viu
x_pred = modelo(jogo1)
newTensor = torch.round(x_pred, decimals=2)
# print(newTensor) # valor previsto pela rede
#print(saida_teste) # valor real


df_newTensor = pd.DataFrame(newTensor.detach().numpy(), columns=['Home', 'Away'])

print(df_newTensor)

print(x_pred.argmax(1))

df_newTensor.to_csv('rede_result.csv', index=False)

# print(torch.count_nonzero(torch.sub(y_pred.argmax(1), saida_teste.argmax(1))))
