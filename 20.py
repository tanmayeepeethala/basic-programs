a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
if a>b:
	max=a
	min=b
else:
	max=b
	min=a
p=max
for i in range(2,p):
	if max%min==0:
		print(max)
		break
	else:
		max=p*i
	