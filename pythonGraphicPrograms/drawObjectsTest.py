import graphics
from graphics import *


def main():
    print("\n***** Graphics Test *****\n")
    print("This program generates a window\nwith some shapes drawn in.\n")
    # Open a graphics window
    win = graphics.GraphWin('Shapes')

    # Draw a red circle centered at point (100, 100) with radius 30
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)

    # Put a textual label in the center of the circle
    label = Text(center, "Red Circle")
    label.draw(win)

    # Draw a square using a Rectangle object
    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)

    # Draw an oval using the Oval object
    oval = Oval(Point(20, 150), Point(180, 199))
    oval.draw(win)

    # Wait for the user input to terminate the program
    input("Press any key to terminate the program")
    print("\n***** End of Program *****\n")


if __name__ == '__main__':
    main()
