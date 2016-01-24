def javac(string1):
    flag = 0
    flagc = 0
    flagjava = 0
    temp = string1
    if string1[0].islower() == 0:
        return "Error!"
    for i in range(1,len(string1)):
        #print "flag c is  " + str(flagc)
        if string1[i] == '_' :
            if flagjava > 0 or flag:
                return "Error!"
            elif i == len(string1) - 1:
                return "Error!"
            else:
                temp = temp[:i - flagc] + temp[i + 1 - flagc].upper() + temp[i + 2 - flagc:]
                flagc += 1
                flag = 1
        elif string1[i].isupper():
            if flagc > 0:
                return "Error!"
            else:
                temp = temp[:i + flagjava] + '_' + temp[i + flagjava].lower() + temp[i + 1 +flagjava:]
                flagjava += 1
                #print "hi"
        else:
            flag = 0
    if flag:
        return "Error!"
    return temp

while True:
	try:
		string = raw_input()
		print javac(string)
	except:
		break

#DONE