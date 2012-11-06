# coding: utf-8

from urllib import urlopen
import re

# Criar um novo ficheiro para guardar os dados
outFile = open('pin.xml','w')

# Coloca a tab <PARLAMENTO> no inicio do ficheiro
outFile.write('<PARLAMENTO>'+'\n')

for i in range(67342,67343):
	# Capturar o url e ler para uma variavel f
	f = urlopen("http://www.parlamento.pt/DeputadoGP/Paginas/DetalheReuniaoPlenaria.aspx?BID=0000"+str(i)).readlines() #incrementa o numero no final do url 
	
	# Coloca a tab de separacao de sessoes
	outFile.write('<sessao>'+'\n') 				
	
	for line in f:
		temp = re.search( r'Reuni.*[0-9]{4}-[0-9]{2}-[0-9]{2}\.', line, re.M|re.I)		# procura em cada linha "ria de (data)."
		if temp: 
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

	outFile.write('</sessao>'+'\n')
# Coloca a tab </PARLAMENTO> no fim do ficheiro
outFile.write('</PARLAMENTO>'+'\n')

# Fechar o ficheiro criado
outFile.close()
