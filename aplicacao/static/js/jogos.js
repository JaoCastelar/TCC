
document.addEventListener('DOMContentLoaded', () => {
    // Selecione elementos da página
    const tabela = document.getElementById('tabela-dados');
    const tbody = tabela.querySelector('tbody');
    const quantidadeLinhasSelect = document.getElementById('quantidade-linhas');
    const paginaAnteriorButton = document.getElementById('pagina-anterior');
    const paginaSeguinteButton = document.getElementById('pagina-seguinte');
    
    const df_final = ['Team', 'Match Up', 'Game Date', 'W/L', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-', 'a.Team', 'a.Match Up', 'a.Game Date', 'a.W/L', 'a.PTS', 'a.FGM', 'a.FGA', 'a.FG%', 'a.3PM', 'a.3PA', 'a.3P%', 'a.FTM', 'a.FTA', 'a.FT%', 'a.OREB', 'a.DREB', 'a.REB', 'a.AST', 'a.STL', 'a.BLK', 'a.TOV', 'a.PF', 'a.+/-']

    let dados = []; // Armazena todos os dados do JSON
    let paginaAtual = 0; // A página atual começa em 0
    let linhasPorPagina = parseInt(quantidadeLinhasSelect.value, 10); // Obtém a quantidade de linhas por página selecionada

    // Função para atualizar a tabela com os dados da página atual
    function atualizarTabela() {
        const inicio = paginaAtual * linhasPorPagina;
        const fim = inicio + linhasPorPagina;
        const dadosPagina = dados.slice(inicio, fim);

        // Limpa a tabela antes de adicionar novas linhas
        tbody.innerHTML = '';

        // Itera pelos dados da página atual e cria as linhas dinamicamente
        dadosPagina.forEach(row => {
            const newRow = tbody.insertRow();
            df_final.forEach(coluna => {
                const cell = newRow.insertCell();
                cell.textContent = row[coluna];
            });
        });
    }

    // Função para atualizar a página e a tabela
    function atualizarPagina() {
        quantidadeLinhasSelect.addEventListener('change', () => {
            linhasPorPagina = parseInt(quantidadeLinhasSelect.value, 10);
            paginaAtual = 0;
            atualizarTabela();
        });

        paginaAnteriorButton.addEventListener('click', () => {
            if (paginaAtual > 0) {
                paginaAtual--;
                atualizarTabela();
            }
        });

        paginaSeguinteButton.addEventListener('click', () => {
            const totalPaginas = Math.ceil(dados.length / linhasPorPagina);
            if (paginaAtual < totalPaginas - 1) {
                paginaAtual++;
                atualizarTabela();
            }
        });
    }

    // Faça uma solicitação AJAX para obter os dados do Flask
    fetch('/dados')
        .then(response => response.json())
        .then(data => {
            dados = data;
            atualizarTabela();
            atualizarPagina();
        })
        .catch(error => console.error('Erro ao carregar os dados:', error));
});
