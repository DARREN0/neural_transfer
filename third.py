from math import sqrt

def isprime(x):
	if x==1: return 0
	k=int(sqrt(x))
	for j in range (2,k+1):
		if x%j==0:return 0
	return 1


def prime(num):
	if num==1: 
		return 2
	k=1
	i=1
	while(k<num):
		i+=2
		if(isprime(i)==True):
			k+=1
	return i

def monisen(num):
	k=0
	i=1
	t=0
	while(k<num):
		t=prime(i)
		if(isprime(2**t-1)==True):
			k+=1
		i+=1
	return 2**t-1

num = int(input("默尼森数:"))
print(monisen(num))

print("git test")
