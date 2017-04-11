str='Hello World'
str1 = ""
for i in range(len(str)):
	count=0
	if(str1.find(str[i])==-1):
		for j in range(len(str)):
				if(str[j]==str[i]):
					count+=1
					str1 = str1 + str[i]
		print('number of iterations'+str[i],count)
		
			
				


