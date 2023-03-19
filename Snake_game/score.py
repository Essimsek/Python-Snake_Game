from turtle import Turtle
FONT = ("courier", 20, "normal")

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.high_score_file = open("high_score.txt", "r+")
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(x=0, y=270)
		self.high_score = int(self.high_score_file.read())
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
		self.high_score_file.seek(0)
		self.high_score_file.truncate()
		self.high_score_file.write(str(self.high_score))
