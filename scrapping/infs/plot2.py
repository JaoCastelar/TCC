import matplotlib.pyplot as plt
import pandas as pd

df_res = pd.read_csv('res.csv')
df_odds = pd.read_csv('../odds/odds.csv')
df_rede = pd.read_csv('rede_result copy 3 61.csv')


md_oddHome = 0
md_oddAway = 0
md_oddsHome = []
md_oddsAway = []

oL, oC = df_odds.shape

for i in range(oL):
    if i % 7 == 0:
        for j in range(i+7):
            md_oddHome = float(df_odds['Home'][j])
            md_oddAway = float(df_odds['Away'][j])
        
        md_oddsHome.append((md_oddHome/7))
        md_oddsAway.append((md_oddAway/7))

# for i in range(70):
#     print('Home: {:.2f}'.format(md_oddsHome[i]), '\nAway: {:.2f}'.format(md_oddsAway[i]), '\n')
    

l, c = df_rede.shape

acerto = 0
erro = 0
total = 0

dados = []
jogo = []

for i in range(l):
    if ((float(df_rede['Home'][i]) > float(df_rede['Away'][i])) and  (md_oddsAway[i] < md_oddsHome[i])) or ((float(df_rede['Home'][i]) < float(df_rede['Away'][i])) and  (md_oddsAway[i] > md_oddsHome[i])):
        jogo.append(i)
        if ((float(df_rede['Home'][i]) > float(df_rede['Away'][i])) and (int(df_res['Team'][i]) > int(df_res['a.Team'][i]))) and (md_oddsAway[i] < md_oddsHome[i]):
            acerto += 1
            dados.append(1)
            # jogo.append(i)
        elif ((float(df_rede['Home'][i]) < float(df_rede['Away'][i])) and (int(df_res['Team'][i]) < int(df_res['a.Team'][i]))) and (md_oddsAway[i] > md_oddsHome[i]):
            acerto += 1
            dados.append(1)
            # jogo.append(i)
        else: 
            erro += 1
            dados.append(0)
            # jogo.append(i)
        total += 1
    else : 
        dados.append(2)
                

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
ax.set_title('Acerto do modelo sobre a casa de aposta')

# Exibir o gráfico
plt.show()
        
# print(df_rede)
# print(df_res)
        
print('Acertos: ',acerto, '\nErros: ', erro, '\nAcurácia: {:.2f}%'.format(((acerto*100)/total)))

# indices = range(jogo)

# Plotando o gráfico de dispersão
for i, valor in enumerate(dados):
    if valor == 1:
        plt.scatter(i, valor, marker='o', color='green')
    elif valor == 2:
        plt.scatter(i, valor, marker='o', color='white')
    else:
        plt.scatter(i, valor, marker='x', color='red')

# Configurando os rótulos do eixo x
plt.xticks(jogo)

# Configurando os rótulos do eixo y
plt.yticks([0, 1], ['Erro', 'Acerto'])

# Adicionando uma linha separando os acertos e erros
# plt.axhline(y=0.5, color='black', linestyle='--')

# Exibindo o gráfico
plt.show()