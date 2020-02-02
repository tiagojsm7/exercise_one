#Getting the data from the log file;

with open('log.txt', 'r') as file:
	file_content = file.read()


lines = file_content.split('\n')
for line in lines:
	thingy = line.split('\'')
	msg = thingy[1]
	partsOfLine = thingy[0].split(' ')
	date = partsOfLine[0]+ ' ' +partsOfLine[1]
	loglevel = partsOfLine[2]
	sessionId = partsOfLine[3]
	bussinessId = partsOfLine[4]
	requestId = partsOfLine[5]
	print ("DATE = " + date)
	print ("LOGLEVE = " + loglevel)
	print ("MSG = " + msg)


