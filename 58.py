n=int(input("Enter a number:"))
num=n
sum=0
while n>0:
	p=1
	rem=n%10
	for i in range(1,rem+1):
		p=p*i
	sum=sum+p
	n=n//10
if sum==num:
	print("Strong number")
else:
	print("Not a Strong number")
