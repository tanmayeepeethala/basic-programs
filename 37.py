lst=list(map(int,input("Enter elements into list:").split()))
sum=0
l=len(lst)
for i in lst:
	sum=sum+i
avg=sum/l
print(f"Average={avg}")