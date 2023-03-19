from turtle import Turtle
FONT = ("courier", 20, "normal")

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(x=0, y=270)
		self.high_score = 0
		self.score = 0
		self.write_score()

	def update_score(self):
		self.clear()
		self.score += 1
		if self.score > self.high_score:
			self.high_score = self.score

	def write_score(self):
		self.write(f"Score: {self.score}     High Score :{self.high_score}", align="center", font=FONT)

	def reset_scoreboard(self):
		self.score = 0
		self.clear()
		self.write_score()
