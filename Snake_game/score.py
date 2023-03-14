from turtle import Turtle
FONT = ("courier", 20, "normal")

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(x=0, y=270)
		self.score = 0
		self.write(arg=f"Score: {self.score}", align="center", font=FONT)

	def update_score(self):
		self.clear()
		self.score += 1

	def write_score(self):
		self.update_score()
		self.write(f"Score: {self.score}", align="center", font=FONT)

	def game_over(self):
		self.goto(x=0, y=0)
		self.write(arg="Game Over", align="center", font=FONT)
