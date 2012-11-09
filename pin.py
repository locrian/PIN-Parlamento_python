# coding: utf-8

from urllib import urlopen
import re

###########################################################
# ISPGaya 2012-2013                                       #
# PIN - Information Processing                            #
# Ricardo Taboada                                         #
# EI - 2930                                               #
#                                                         #
# This script serves the purpose of extrating relevant	  #
# data from "Assembleia da Republica" dataset using 	  #
# regular expressions and build a valid structured xml    #
# file for further analysis.	                          #
#							  #
###########################################################


# Criar um novo ficheiro para guardar os dados
outFile = open('pin.xml','w')

# Coloca no topo do XML a informação sobre o mesmo
outFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')

# Coloca a tab <PARLAMENTO> no inicio do ficheiro
outFile.write('<PARLAMENTO>\n')

#Inicializa um contador para os urls processados e outro para as sessoes validas
urlCounter = 0
sessionCounter = 0


for i in range(67323,67343):
        
	# Capturar o url para uma variavel "url"
	url = "http://www.parlamento.pt/DeputadoGP/Paginas/DetalheReuniaoPlenaria.aspx?BID=0000"+str(i)
        # Capturar o url e ler para uma variavel f
        #f = urlopen("http://www.parlamento.pt/DeputadoGP/Paginas/DetalheReuniaoPlenaria.aspx?BID=0000"+str(i)).readlines() #incrementa o numero no final do url 
	f = urlopen(url).readlines()
        if f: 
             print url											# Imprime para o ecran o URL que vai ser processado
	     urlCounter += 1										# Incrementa a variavel do contador de urls
             # Coloca a tab de separacao de sessoes
             outFile.write('<sessao>\n') 								# Coloca a tab <sessao> andes de obter os dados da sessao
													# parlamentar
             for line in f:
                temp = re.search( r'Reuni.*[0-9]{4}-[0-9]{2}-[0-9]{2}\.', line, re.M|re.I)		# procura em cada linha "ria de (data)."
                if temp:
			sessionCounter += 1								# se temp contem a data é porque a sessão existe 
                        temp = re.sub(r'.*[\s]', '<data>', temp.group())                                # substitui tudo que nao seja a data pela tag <data>
                        temp = temp.replace('.','</data>')						# substitui "." pela tag </data>
                        outFile.write(temp+'\n')
                temp = re.search( r'Biografia.*?["]\s[h]', line, re.M|re.I)				# procura em cada linha "Biografia (string até " h)"
                if temp: 
                        temp = temp.group().replace('Biografia de ','<nome>')				# substitui "Biografia de " pela tag <nome>
                        temp = temp.replace('" h','</nome>')						# substitui "" h" for </nome>
                        outFile.write(temp+'\n')
                temp = re.search( r'lblGP.*<\/sp', line, re.M|re.I)					# procura em cada linha "lblGP (string até </sp"
                if temp: 
                        temp = temp.group().replace('lblGP">','<partido>')				# substitui "lblGP">" pela tag <partido>
                        temp = temp.replace('</sp','</partido>')					# substitui "</sp" pela tag </partido>
                        outFile.write(temp+'\n')
                temp = re.search( r'Presenca">.*<\/', line, re.M|re.I)					# procura em cada linha "Presenca"> (string até </)"
                if temp:                
                        temp = temp.group().replace('Presenca">','<presenca>')				# substitui "Presenca">" pela tag <presenca>
                        temp = temp.replace('</','</presenca>')			                 	# substitui "</" pela tag </presenca>
                        outFile.write(temp+'\n')
                temp = re.search( r'Motivo">.*<\/s', line, re.M|re.I)					# procura em cada linha "Motivo (string até </s"
                if temp:           
                        temp = temp.group().replace('Motivo">','<motivo>')				# substitui "Motivo">" pela tag <motivo>
                        temp = temp.replace('</s','</motivo>')						# substitui "</s" pela tag </motivo>
                        outFile.write(temp+'\n')	

        outFile.write('</sessao>\n')
# Coloca a tab </PARLAMENTO> no fim do ficheiro
outFile.write('</PARLAMENTO>\n')

# Fechar o ficheiro criado
outFile.close()

print str(urlCounter) + " URL's analisados. " + str(sessionCounter) + " sessoes válidas processadas"
