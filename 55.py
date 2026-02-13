n=int(input("Enter range:"))
num=1
for i in range(1,n+1):
	for j in range(n-i):
		print(" ",end="")
	for k in range(i):
		print(num,end=" ")
		num=num+1
	print()