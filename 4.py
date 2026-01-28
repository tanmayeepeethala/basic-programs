a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b and a<c or a<b and a>c:
	x=a
elif b>a and b<c or b<a and b>c:
	x=b
elif c>a and c<b or c<a and c>b:
	x=c
print(x)                                                                                                                                                                                                                                                                                                                                                                                    