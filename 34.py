s=input("Enter a string:")
str=""
for ch in s:
	if ch in str:
		continue
	else:
		str=str+ch
print(str)