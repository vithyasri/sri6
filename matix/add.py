num = int(input())
temp = num
product = 1;
while(temp != 0):
	product = product * (temp % 10);
	temp = int(temp / 10)
print( product)
