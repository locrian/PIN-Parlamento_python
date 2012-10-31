from urllib import urlopen
import re

# Criar um novo ficheiro para guardar os dados
fileNew = open('pin.xml','w')

# Capturar o url e ler para uma variavel f.
f = urlopen("http://www.parlamento.pt/DeputadoGP/Paginas/DetalheReuniaoPlenaria.aspx?BID=00001").readlines()

tempX = 'Biografia.*?["]\s[h]'

for line in f:
	temp = re.search( r'ria de [0-9]{4}-[0-9]{2}-[0-9]{2}\.', line, re.M|re.I)
	if temp: 
	   temp = temp.group().replace('ria de ','<data>')
	   temp = temp.replace('.','</data>')
	   fileNew.write(temp+'\n')
	temp = re.search( r'Biografia.*?["]\s[h]', line, re.M|re.I)
	if temp: 
	   temp = temp.group().replace('Biografia de ','<nome>')
           temp = temp.replace('" h','</nome>')
	   fileNew.write(temp+'\n')
	temp = re.search( r'lblGP.*<\/sp', line, re.M|re.I)
        if temp: 
           temp = temp.group().replace('lblGP">','<partido>')
           temp = temp.replace('</sp','</partido>')
           fileNew.write(temp+'\n')
	temp = re.search( r'Presenca">.*<', line, re.M|re.I)
        if temp:                
           temp = temp.group().replace('Presenca">','<presenca>')
           temp = temp.replace(')<','</partido>').replace('(','')
           fileNew.write(temp+'\n')
	temp = re.search( r'Motivo">.*<\/s', line, re.M|re.I)
        if temp:                
           temp = temp.group().replace('Motivo">','<motivo>')
           temp = temp.replace('</s','</motivo>')
           fileNew.write(temp+'\n')

	   	


# Fechar o ficheiro criado
fileNew.close()
