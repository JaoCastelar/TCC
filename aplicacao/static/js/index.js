document.addEventListener("DOMContentLoaded", function () {
    fetch(`/odds`)
        .then(response => response.json())
        .then(data => {
            fetch(`/rede_result`)
                .then(response => response.json())
                .then(data2 => {
                    var outputDiv = document.getElementById(`jogos`);
                    outputDiv.innerHTML = ``;
        
                    var numberOfDivs = Math.ceil(data.length / 7);
        
                    for (var i = 0; i < numberOfDivs; i++) {
                        
                        var anchor = document.createElement(`a`);
        
                        anchor.href = `#res`
        
                        var div = document.createElement(`div`);
        
                        var confronto = document.createElement('div');
        
                        var dataConfronto = document.createElement('div');
                        
                        for (var j = i * 7; j < Math.min((i + 1) * 7, data.length); j++) {
                            
                            var linha = data[j];
        
                            
                            // Pegue as duas últimas colunas
                            var coluna1 = Object.keys(linha)[Object.keys(linha).length - 2];
                            var coluna2 = Object.keys(linha)[Object.keys(linha).length - 1];
        
                            var date = Object.keys(linha)[Object.keys(linha).length - 4];
                            
                            if (j % 7 == 0) {
                                dataConfronto.innerHTML += linha[date];
                                
                                confronto.innerText += linha[coluna1] + "\n" + ` x ` + "\n" + linha[coluna2] + "\n";
                                confronto.id = `${i}`;

                                let idConf = confronto.id
                                
                                div.addEventListener(`click`, function () {
                                    // console.log(idConf);
                                    pegaValores(idConf, data, data2)
                                });

                            }
                        
                        }
        
                        div.appendChild(confronto);
                        div.appendChild(dataConfronto);
                        
                        anchor.appendChild(div);
        
                        outputDiv.appendChild(anchor);
                    }
                })
                .catch(error => {
                    console.error(`Erro ao carregar os dados do CSV:`, error);
                });        
        })
        .catch(error => {
            console.error(`Erro ao carregar os dados do CSV:`, error);
        });

    
});

function pegaValores(id, data, data2) {

    var div = parseInt(id) * 7
    
    var parada = div + 7

    var res = document.getElementById(`res_cont`);

    if (res.childElementCount > 0) {
        while (res.childElementCount > 0) {     
            res.removeChild(res.firstChild);
        }
    }
    
    for (let i = div; i < parada; i++) {
        
        var linha = data[i];
        var linha2 = data2[id];
      
        var img = document.createElement(`img`);

        if (res.childElementCount == 0) {
            
            img.src = `../static/img/Rede NBA.png`;

            var textCasa = 'Rede NBA';

            var coluna1 = Object.keys(linha2)[Object.keys(linha2).length - 1];
            var coluna2 = Object.keys(linha2)[Object.keys(linha2).length - 2];

            var odd1 = document.createTextNode(linha2[coluna1]);
            var odd2 = document.createTextNode(linha2[coluna2]);

            i -= 1

        } else {

            var casa = Object.keys(linha)[Object.keys(linha).length - 5];
            var coluna1 = Object.keys(linha)[Object.keys(linha).length - 3];
            var coluna2 = Object.keys(linha)[Object.keys(linha).length - 6];

            var textCasa = linha[casa];
            var odd1 = document.createTextNode(linha[coluna1]);
            var odd2 = document.createTextNode(linha[coluna2]);

            if (textCasa == `bet365`) {
    
                img.src = `../static/img/${textCasa}.png`;
                
            }else if (textCasa == `1xBet`) {
                
                img.src = `../static/img/${textCasa}.png`;
                
            }else if (textCasa == `Betano.br`) {
    
                img.src = `../static/img/${textCasa}.png`;
                
            }else if (textCasa == `Betfair`) {
                
                img.src = `../static/img/${textCasa}.png`;
                
            }else if (textCasa == `Marsbet`) {
                
                img.src = `../static/img/${textCasa}.png`;
                
            }else if (textCasa == `Novibet`) {
    
                img.src = `../static/img/${textCasa}.png`;
                
            }else if (textCasa == `Parimatch`) {
                
                img.src = `../static/img/${textCasa}.png`;
                
            }
        }


        img.className = `logoBet`;
        img.alt = `${textCasa}`;
        img.title = `${textCasa}`

        var casas = document.createElement(`div`);
        casas.id = `casa`
        var odds = document.createElement(`div`);
        odds.id = `odds`
        odds.className = 'odds';

        var divodd1 = document.createElement('div');
        divodd1.id = `odd1${i}${id}`;
        let idDiv1 = divodd1.id
        var divodd2 = document.createElement('div');
        divodd2.id = `odd2${i}${id}`;
        let idDiv2 = divodd2.id

        divodd1.appendChild(odd1);
        divodd2.appendChild(odd2);
        
        var casasLine = document.createElement(`div`);
        casasLine.className = `casasLine`
        casasLine.id = `casasLine`

        casas.appendChild(img);

        odds.appendChild(divodd1);
        odds.appendChild(divodd2);

        casasLine.appendChild(casas);
        casasLine.appendChild(odds);

        res.appendChild(casasLine); 

        corOdd(idDiv1, idDiv2);
        
    }

}

function corOdd(odd1, odd2) {
    
    let style1 = document.getElementById(odd1)
    let style2 = document.getElementById(odd2)
    
    let res = document.getElementById('res_cont')

    
    if (res.childElementCount === 1) {
        if (parseFloat(style1.innerHTML) > parseFloat(style2.innerHTML)) {
            style1.style.backgroundColor = 'green';
            style1.style.color = 'white';
            
            style2.style.backgroundColor = 'red';
            style2.style.color = 'white';
            
            style1.innerHTML = 'W'
            style2.innerHTML = 'L'
            
        } else {
            style1.style.backgroundColor = 'red';
            style1.style.color = 'white';
            
            style2.style.backgroundColor = 'green';
            style2.style.color = 'white';

            style1.innerHTML = 'L'
            style2.innerHTML = 'W'

        }
    } else {
        if (parseFloat(style1.innerHTML) < parseFloat(style2.innerHTML)) {
            style1.style.backgroundColor = 'green';
            style1.style.color = 'white';
            
            style2.style.backgroundColor = 'red';
            style2.style.color = 'white';
        } else {
            style1.style.backgroundColor = 'red';
            style1.style.color = 'white';
    
            style2.style.backgroundColor = 'green';
            style2.style.color = 'white';
        }
    }


}