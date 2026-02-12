def palindrome(n):
	num=0
	numb=n
	while n>0:
		rem=n%10
		num=num*10+rem
		n=n//10
	if num==numb:
		print("Palindrome")
	else:
		print("Not a Palindrome")
n=int(input("Enter a number:"))
palindrome(n)