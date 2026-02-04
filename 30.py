s=input("Enter a string:")
vl="aeiouAEIOU"
v=0
c=0
for ch in s:
	if ch in s:
		if ch in vl:
			v=v+1
		elif ch>='a' and ch<='z' or ch>='A' and ch<='Z':
			c=c+1
print("VOWLES:",v)
print("CONSONANTS:",c)
		
