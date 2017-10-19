from graphics import *
def main():
	win = GraphWin('BOX', 500, 500) # give title and dimensions
	win.yUp() # make right side up coordinates!


	l1 = Line(Point(250, 50), Point(250,300)) # set endpoints
	l1.setWidth(500)
	l1.setFill("#3D5A92")
	l1.draw(win)
	
	l2 = Line(Point(250, 50), Point(250,250)) # set endpoints
	l2.setWidth(100)
	l2.setFill("#FF6E00")
	l2.draw(win)
	
	l3 = Circle(Point(289, 140),5) # set endpoints
	l3.setWidth(2)
	l3.setFill("#8B6914")
	l3.draw(win)
	
	l4 = Line(Point(0, 550), Point(550,550)) # set endpoints
	l4.setWidth(500)
	l4.setFill("#ACE7FF")
	l4.draw(win)

	l5 = Circle(Point(500, 500),40) # set endpoints
	l5.setFill("#FFF600")
	l5.draw(win)
	
	label = Text(Point(250, 180), 'Im a self aware door')
	label.draw(win)
	
	
	message = Text(Point(win.getWidth()/2, 20), 'click anywhere to quit.')
	message.draw(win)
	win.getMouse()
	win.close()
main()
