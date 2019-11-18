#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape

screen_width = 400
screen_height = 400

letters = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


#set up screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)

# Make the screen aware of the new file
wn.bgpic("tree.gif")
#create apple turtle
apple = trtl.Turtle()
apple.up()

#create writer turtle
active_apple = trtl.Turtle()



# given a turtle, set that turtle to be shaped by the image file



def reset_apple(active_apple):
  length_list = len(letters)
  if(length_list != 0):
    index = rand.randint(0,length_list)
    active_apple.goto(rand.randint(-200,200), rand.randint(-200,200))
    draw_apple(active_apple, letters.pop(index))

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()



def apple_fall():
  apple.up()
  apple.goto(0,-150)
  apple.clear()
  apple.ht()
reset_apple(apple)
def draw_letter(active_apple, letter):
  active_apple.color("white")
  active_apple.goto(0,150)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  
draw_apple(active_apple)
wn.onkeypress(apple_fall, "a")
wn.listen()
trtl.mainloop()