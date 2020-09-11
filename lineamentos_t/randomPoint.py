import csv
from random import uniform
from random import seed
from math import sqrt
import matplotlib.pyplot as plt
file = raw_input("Digite o nome do arquivo com os lineamentos\n")

lineamentos = []
limites = [99999999,99999999,0,0]

with open(file, 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    #Elemento de leitura de cada lineamento
    for linha in reader:
        #X minimo
        if limites[0] > float(linha[2]):
        	limites[0] = float(linha[2])
        #Y minimo
        if limites[1] > float(linha[4]):
        	limites[1] = float(linha[4]) 
        #X maximo
        if limites[2] < float(linha[3]):
        	limites[2] = float(linha[3]) 
        #Y maximo
        if limites[3] < float(linha[5]):
        	limites[3] = float(linha[5])

        #Definindo eq. da reta para cada lineamento
        #X no indice 6
        linha.append( float(linha[5]) - float(linha[4]) )

        #Y no indice 7
        linha.append( float(linha[2]) - float(linha[3]) )

        #Sem variaveis no indice 8
        linha.append( (float(linha[3])*float(linha[4])) - (float(linha[2])*float(linha[5])) )

        #Divisor para a distancia entre reta e ponto no indice 9
        linha.append( sqrt( (linha[6]*linha[6])+(linha[7]*linha[7]) ) )

        #Quandidades de pontos que estao descritos pela eq da reta no indice 10
        linha.append(0)

        #Guardando lineamentos + eq
        lineamentos.append(linha)

    #Testar valores para pontos randons
    nPontos = int(raw_input("Digite o numero de pontos aleatorios:\n"))
    distaciaMaxima = float(raw_input("Digite a distancia maxima desejada:\n"))
    pCoencidentesTotais = 0
    pontosRandom = []
    for i in range(nPontos):

    	#Criando os pontos randomicamente
    	seed()
    	pontoRandom = [uniform(limites[0],limites[2]), uniform(limites[1],limites[3])]
    	distancia = 99999999;
    	j = 0;

    	#Verificando se o ponto esta proximo de algum lineamento
    	for linha in lineamentos:
    		#preciso verificar se o ponto esta dentro do segmento de reta desejado
    		if(pontoRandom[0]>=linha[0] || pontoRandom[2]<=linha[0] || pontoRandom[1]>=linha[1] || pontoRandom)

    		dAux = abs( ((linha[6]*pontoRandom[0])+(linha[7]*pontoRandom[1])+linha[8])/linha[9] )

    		if distancia > dAux:
    			distancia = dAux
    			linhaAux = j;

    		j = j + 1
    	
    		
    	#Se a distancia for menor que a esperada marca
    	if distancia < distaciaMaxima:
    		lineamentos[linhaAux][10] = lineamentos[linhaAux][10] + 1
    		pCoencidentesTotais = pCoencidentesTotais + 1;

    	pontosRandom.append([pontoRandom[0], pontoRandom[1], lineamentos[linhaAux][0], distancia])


    vetAux = []
    vetAuxNum = []
    for pontoRandom in pontosRandom:
    	vetAux.append(pontoRandom[2])
    	vetAuxNum.append(pontoRandom[3])



    plt.bar(vetAux, vetAuxNum)
    plt.xlabel("Codigo do lineamento")
    plt.ylabel("Distancia do lineamento mais proximo")
    plt.show()
    

    with open('randomPoint.csv', 'a') as arq:
    	for ponto in pontosRandom:
    		for coluna in ponto:
    			arq.write(str(coluna)+";")
    		arq.write("\n")
    		
    print(pCoencidentesTotais)  