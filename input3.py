# save file as input3.py
print ("INPUT THREE NUMBER")
A = float(input ("A: "))
B = float(input ("B: "))
C = float(input ("C: "))
x = 5
while True:
	y =A*x*x + B*x + C
	x = x + 1
	print (x,y)
	if (x > 5):
		break
		
