__author__ = "6598477: Jannik Zorn"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__email__ = "jannik@zorn.net"
__task__ = "PRG_8_2"

import random
import string
import tkinter 


class Play():
 
  Title_GAME = "SNAKE GAME"
  Size_BOARD = 800,600

  def __init__(self, master):
    
    self.master = master
    self.head = None
    self.head_position = None
    self.segments = []
    self.segments_positions = []
    self.food = None
    self.food_position = None
    self.direction = None
    self.moved = True
    self.running = False
    
    self.init()

  def init(self):
    self.master.title(self.Title_GAME)
    self.master.bind("w", self.on_up)
    self.master.bind("a", self.on_left)
    self.master.bind("s", self.on_down)
    self.master.bind("d", self.on_right)

    self.canvas = tkinter.Canvas(self.master)
    self.canvas.grid(sticky=tkinter.NSEW)

    self.start_button = tkinter.Button(self.master, text="Start the game", command=self.on_start)
    self.start_button.grid(sticky=tkinter.EW)

    self.master.columnconfigure(0, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.master.resizable(width=False, height=False)
    self.master.geometry("%dx%d" % self.Size_BOARD)

  def on_start(self):
      
    self.restart()
    
    if self.running:
      self.running = False
      self.start_button.configure(text="Start the game")
                                  
    else:
      self.running = True
      self.start_button.configure(text="Stop the game")
      self.start()
                                  
  def restart(self):
        self.canvas.delete(tkinter.ALL)
        self.segments.clear()
        self.segments_positions.clear()
     
  def start(self):
                                  
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()

    self.canvas.create_rectangle(10, 10, width-10, height -10)
    self.direction = random.choice('wasd')
    head_position = [round(width / 2, -1), round(height / 2, -1)]
    self.head = self.canvas.create_text(tuple(head_position), text="[o]" , fill ="blue")
    self.head_position = head_position

    self.spawn_foody()
    self.new()

 
  def spawn_foody(self):
    
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()

    positions = [tuple(self.head_position), self.food_position] + self.segments_positions
    position = round(random.randint(20, width - 20), -1), round(random.randint(20, height - 20), -1)

    while position in positions:
      position = round(random.randint(20, width - 20), -1), round(random.randint(20, height - 20), -1)

    character = "O"
    self.food = self.canvas.create_text(position, text=character, fill= "red")
    self.food_position = position
    self.food_character = character

 
  def new(self):
    
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()
    previous_head_position = tuple(self.head_position)

    if self.direction == "w":
      self.head_position[1] -= 10
    elif self.direction == "a":
      self.head_position[0] -= 10
    elif self.direction == "s":
      self.head_position[1] += 10
    elif self.direction == "d":
      self.head_position[0] += 10

    head_position = tuple(self.head_position)
    if(head_position[0] < 10 or head_position[0] >= width - 10
       or head_position[1] < 10 or head_position[1] >= height - 10 or
       any(segments_position == head_position for segments_position in self.segments_positions)):
      self.game_over()
      return

    if head_position == self.food_position:
      self.canvas.coords(self.food, previous_head_position)
      self.segments.append(self.food)
      self.segments_positions.append(previous_head_position)
      self.spawn_foody()

    if self.segments:
      previous_position = previous_head_position
      for index, (segment, position) in enumerate(zip(self.segments, self.segments_positions)):
        self.canvas.coords(segment, previous_position)
        self.segments_positions[index] = previous_position
        previous_position = position

    self.canvas.coords(self.head, head_position)
    self.moved = True

    move_speed = 100

    if len(self.segments) > 10:
      move_speed = 70

    if len(self.segments) > 15:
      move_speed = 50

    if len(self.segments) > 20:
      move_speed = 45
                                  
    if self.running:
      self.canvas.after(move_speed, self.new)


  def game_over(self):
    
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()
    self.running = False

    self.start_button.configure(text="Start the game")
                                  
    score = len(self.segments) * 10
    self.canvas.create_text(round(width/2), round(height/2), text="Game Over! Your score is: %d" %score)

  def on_up(self, event):
    if self.moved and not self.direction == "s":
      self.direction = "w"
      self.moved = False

  def on_down(self,event):
    if self.moved and not self.direction == "w":
      self.direction = "s"
      self.moved = False

  def on_left(self, event):
    if self.moved and not self.direction == "d":
      self.direction = "a"
      self.moved = False

  def on_right(self, event):
    if self.moved and not self.direction == "a":
      self.direction = "d"
      self.moved = False


def main():
  root = tkinter.Tk()
  Play(root)
  root.mainloop()

if __name__ == "__main__":
  main()

