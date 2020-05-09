from Tkinter import *
import tkFont
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

win = Tk()
v = IntVar()
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')


def redLED():
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	
	
def greenLED():
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	
	
def blueLED():
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	
	
def quitProgram():
	print("Program has been closed.")	
	GPIO.cleanup()
	win.quit()


win.title("LED GUI")
win.geometry('300x350')

Radiobutton(win, text = "Red", variable = v, value = 1, command = redLED, padx = 20, font = myFont).pack(anchor = W)
Radiobutton(win, text = "Green", variable = v, value = 2, command = greenLED, padx = 20, font = myFont).pack(anchor = W)
Radiobutton(win, text = "Blue", variable = v, value = 3, command = blueLED, padx = 20, font = myFont).pack(anchor = W)

Button(win, text = "Quit", font = myFont, command = quitProgram, height = 2, width = 6).pack(side = BOTTOM)

win.mainloop()
