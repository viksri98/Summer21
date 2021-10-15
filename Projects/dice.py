import numpy as np
from matplotlib import image as mpimage
from matplotlib import pyplot as plt
import random
from matplotlib.backend_bases import MouseButton

dice_img = np.array(mpimage.imread('/home/vikram/Downloads/images/qwe_download.png'))
background = np.ones((600, 600, 4)) * 255

# this function gets the correct die from the dice_img
def get_die(num):
    yinit = 41
    xinit = 26
    xbet = 41
    ybet = 78
    side = 240
    if num == 1:
        return dice_img[yinit:yinit + side, xinit + 12:xinit+12+side, : ]
    if num == 2:
        return dice_img[yinit:yinit + side, xinit + side + xbet:xinit + side * 2 + xbet, : ]
    if num == 3:
        return dice_img[yinit:yinit + side, xinit + 2 * side + 2 * xbet:xinit + side * 3 + xbet * 2, : ]
    if num == 4:
        return dice_img[yinit + side + ybet:yinit + 2 * side + ybet, xinit + 3:xinit + side + 3, : ]
    if num == 5:
        return dice_img[yinit + side + ybet:yinit + 2 * side + ybet, xinit + side + xbet:xinit + side * 2 + xbet, : ]
    return dice_img[yinit + side + ybet:yinit + 2 * side + ybet, xinit + 2 * side + 2 * xbet:xinit + side * 3 + xbet * 2, : ]

# generate two random dice rolls.
def gen_rolls():
	return random.randint(1, 6), random.randint(1, 6)

# display random dice rolls
def display():
	rolls = gen_rolls()
	background[180:420, 55:295, :] = get_die(rolls[0])
	background[180:420, 305:545, :] = get_die(rolls[1])
	plt.imshow(background)
	plt.text(220, 100, "Dice!", fontsize=50)
	plt.draw()

# handle mouse input, if clicked on left regen dice
def on_click(event):
	if event.button is MouseButton.LEFT:
		if event.x < 300:
			print('clicked left')
			display()

plt.connect('button_press_event', on_click)
display()
plt.show()
