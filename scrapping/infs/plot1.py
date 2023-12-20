import matplotlib.pyplot as plt
import pandas as pd

df_res = pd.read_csv('res.csv')
df_rede = pd.read_csv('rede_result copy 3 61.csv')

l, c = df_rede.shape

acerto = 0
erro = 0

dados = []

for i in range(l):
    if (float(df_rede['Home'][i]) > float(df_rede['Away'][i])) and (int(df_res['Team'][i]) > int(df_res['a.Team'][i])):
        acerto += 1
        dados.append(1)
    elif (float(df_rede['Home'][i]) < float(df_rede['Away'][i])) and (int(df_res['Team'][i]) < int(df_res['a.Team'][i])):
        acerto += 1
        dados.append(1)
    else: 
        erro += 1
        dados.append(0)

# Criar um gráfico de barras
labels = ['Acertos', 'Erros']
values = [acerto, erro]

fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=['green', 'red'])

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')


# Adicionar rótulos e título
ax.set_ylabel('Quantidade')
ax.set_title('Acertos e Erros do modelo')

# Exibir o gráfico
plt.show()
        
# print(df_rede)
# print(df_res)
        
print('Acertos: ',acerto, '\nErros: ', erro, '\nAcurácia: {:.2f}%'.format(((acerto*100)/70)))

indices = range(len(dados))

# Plotando o gráfico de dispersão
for i, valor in enumerate(dados):
    if valor == 1:
        plt.scatter(i, valor, marker='o', color='green')
    else:
        plt.scatter(i, valor, marker='x', color='red')

# Configurando os rótulos do eixo y
plt.yticks([0, 1], ['Erro', 'Acerto'])

# Exibindo o gráfico
plt.show()