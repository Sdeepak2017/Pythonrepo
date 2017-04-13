a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
dict={}
if(a>10 and b<250):
	c=a+b
	dict['add']= c
	print("sum of a+b",dict['add'])
elif(a>50 and b<300):
	c=b*a
	dict['multiply']= c
	print("product of a and b",dict['multiply'])
else:
	print("please enter the value within 10-1000")
