lst=list(map(int,input("Enter elements into list:").split()))
min=lst[0]
max=lst[0]
for i in range(len(lst)):
	if lst[i]>max:
		max=lst[i]
	if lst[i]<min:
		min=lst[i]
print(f"MAX={max} , MIN={min}")
