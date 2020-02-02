#Getting and parsing the data from the log file;
with open('log.txt', 'r') as file:
		file_content = file.read()
lines =	file_content.split('\n')

msgs = list()
dates = list()
loglevels = list()
sessionIds = list()
bussinessIds = list()
requestIds = list()

for ind,line in enumerate(lines):
	thingy = line.split('\'')
	msgs.append(thingy[1])
	partsOfLine = thingy[0].split(' ')
	dates.append(partsOfLine[0]+ ' ' +partsOfLine[1])
	loglevels.append(partsOfLine[2])
	sessionIds.append(partsOfLine[3].split(':')[1])
	bussinessIds.append(partsOfLine[4].split(':')[1])
	requestIds.append(partsOfLine[5].split(':')[1])
#	print ("DATE = " + dates[ind] + "\nLOGLEVEl = " + loglevels[ind] + "\nSESSION-ID = " 
#		+ sessionIds[ind] + "\nBUSINESS-ID = " + bussinessIds[ind]+ "\nREQUEST-ID = " +requestIds[ind]+ "\nMSG = " +msgs[ind] +"\n")

def choosenOption(arg):
	if arg == 'q':
		print ('You chose to quit.')
		return

	ret = 0
	if arg == 'l':
		ret = selectLogLevel()		
	if arg == 's':
		ret = selectSessionId()
	if arg == 'b':
		ret = selectBusinessId()
	if arg == 'd':
		ret = selectDateWithin()	
	if ret == 0:
			print ("No such log lines found, try again.\n")
	
	init()

			


def init():
	choosenOption(input("What do you wish to do? \n:q - exit \n:l - Check logs by loglevel \n:b - Check logs by business id"
		"\n:s - Check logs by session id \n:d - Check logs in date range.\n"))

def selectLogLevel():
	val = input("Insert the Loglevel you want:")
	num = 0
	for i, loglevel in enumerate(loglevels):
		if loglevel.upper() ==val.upper():
			num = num+1
			print ("DATE = " + dates[i] + "\nLOGLEVEl = " + loglevels[i] + "\nSESSION-ID = " 
			+ sessionIds[i] + "\nBUSINESS-ID = " + bussinessIds[i]+ "\nREQUEST-ID = " +requestIds[i]+ "\nMSG = " +msgs[i] +"\n")
	return num

def selectSessionId():
	val = input("Insert the session id you want:")
	num = 0
	for i, sessionId in enumerate(sessionIds):
		if sessionId == val:
			num = num+1
			print ("DATE = " + dates[i] + "\nLOGLEVEl = " + loglevels[i] + "\nSESSION-ID = " 
			+ sessionIds[i] + "\nBUSINESS-ID = " + bussinessIds[i]+ "\nREQUEST-ID = " +requestIds[i]+ "\nMSG = " +msgs[i] +"\n")				
	return num

def selectBusinessId():
	val = input("Insert the bussiness id you want:")
	num = 0
	for i, bussinessId in enumerate(bussinessIds):
		if businessId == val:
			num = num+1
			print ("DATE = " + dates[i] + "\nLOGLEVEl = " + loglevels[i] + "\nSESSION-ID = " 
			+ sessionIds[i] + "\nBUSINESS-ID = " + bussinessIds[i]+ "\nREQUEST-ID = " +requestIds[i]+ "\nMSG = " +msgs[i] +"\n")
	return num

def selectDateWithin():
	#TODO


#Starting the whole juju
init()
