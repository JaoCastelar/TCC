from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

df_final = ['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-', 'a.Team', 'a.Match Up', 'a.Game Date', 'a.W/L', 'a.PTS', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF', 'a.+/-']
df_odds = ['Team', 'a.Team', 'Data', 'CasaAposta', 'Home', 'Away']
df_rede_result = ['Home', 'Away']


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jogos")
def contatos():
    return render_template("jogos.html")

@app.route('/dados')
def get_data():
    # Abra o arquivo CSV
    with open('C:/Users/Castelar/Desktop/Faculdade/TCC/Aplicação/scrapping/infs/base_nba_final.csv', 'r') as arquivo_csv:
        # Leia o CSV usando o módulo csv
        csv_reader = csv.DictReader(arquivo_csv)
        # Converta os dados CSV em uma lista de dicionários
        dados_csv = [linha for linha in csv_reader]
        
    dados_reordenados = [{coluna: linha[coluna] for coluna in df_final} for linha in dados_csv]

    return jsonify(dados_reordenados)

@app.route('/odds')
def get_odds():
    # Abra o arquivo CSV
    with open('C:/Users/Castelar/Desktop/Faculdade/TCC/Aplicação/scrapping/odds/odds.csv', 'r') as arquivo_csv:
        # Leia o CSV usando o módulo csv
        csv_reader = csv.DictReader(arquivo_csv)
        # Converta os dados CSV em uma lista de dicionários
        dados_csv = [linha for linha in csv_reader]
        
        
    dados_reordenados = [{coluna: linha[coluna] for coluna in df_odds} for linha in dados_csv]

    return jsonify(dados_reordenados)

@app.route('/rede_result')
def get_result():
    # Abra o arquivo CSV
    with open('C:/Users/Castelar/Desktop/Faculdade/TCC/Aplicação/scrapping/infs/rede_result.csv', 'r') as arquivo_csv:
        # Leia o CSV usando o módulo csv
        csv_reader = csv.DictReader(arquivo_csv)
        # Converta os dados CSV em uma lista de dicionários
        dados_csv = [linha for linha in csv_reader]
        
    dados_reordenados = [{coluna: linha[coluna] for coluna in df_rede_result} for linha in dados_csv]

    return jsonify(dados_reordenados)

if __name__ == "__main__":
    app.run(debug=True)