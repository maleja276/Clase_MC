import sys 
# a o b son pares

a= input("inserte el numero a: ")

if a % 2 == 0:

	print("a:%d es par" % a)
	
else:
	print("a:%d es impar" % a)

b= input("Inserte el numero b: ")

if b % 2 == 0:

	print("b:%d es par" % b)
	
else:
	print("b:%d es impar" % b)

# Divisores de a y b 

x= 1
divisoresa=[]
divisoresb=[]

while True: 
	if a % x == 0:
		divisoresa.append(x)
		x+=1
	elif x > a:
		break	
	else:
		x+=1
    	
print("Los divisores de a son %s" % divisoresa)

y=1
while True: 
	if b % y == 0:
		divisoresb.append(y)
		y+=1
	elif y > b:
		break	
	else:
		y+=1
    	
print("Los divisores de b son %s" % divisoresb)

x= 1
num= 1

#Maximo comun divisor entre a y b 

while True:
	if a % x == 0 and b % x == 0:
		num=x
		x+=1
	elif x > a or x > b :
		break
	else:
		x+=1
print("El maximo comun divisor es: %s " % num)


	
	
	
