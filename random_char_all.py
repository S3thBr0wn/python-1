# save this file as random_int.py
from random import randint
def randlist(r, usedlist,done):
	sum = 0
	alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","`","[","]",":","'",".","/","~","!","@","#","$","%","^","&","*","(",")","_","+","|","<",">","?"]
	
	usedlist[r] = 1
	c = alpha[r]

	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	#print (c, usedlist," sum ",sum)
	if sum == 81:
		done = True
	return c, usedlist, done
	
def main():
	#initial variables
	used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	done = False #boolean
	######################
	while done == False:
		r = randint(0,80) # make a random number
		c,used,done = randlist(r,used,done)
	
		#print (used)
		print(c,end="")
main()

