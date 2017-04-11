str='Hello World'
count=0
findChar = 'h'
for i in range(len(str)):
	if(str[i].lower()==findChar.lower()):
		count+=1
print('number of iterations ' + findChar + ' char is ', count)