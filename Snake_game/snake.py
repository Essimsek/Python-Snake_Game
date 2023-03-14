from turtle import Turtle

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

	def __init__(self):
		self.segments: list[Turtle] = []
		self.create_snakes()

	def create_snakes(self):
		for position in STARTING_COORDINATES:
			self.add_tail(position)

	def add_tail(self, position):
		new_segment = Turtle(shape="square")
		new_segment.color("white")
		new_segment.penup()
		new_segment.goto(position)
		self.segments.append(new_segment)

	def	extend(self):
		position = self.segments[-1].pos()
		self.add_tail(position)

	def move(self):
		for segment_num in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[segment_num - 1].xcor()
			new_y = self.segments[segment_num - 1].ycor()
			self.segments[segment_num].goto(x=new_x, y=new_y)
		self.segments[0].forward(MOVE_DISTANCE)

	def check_collision(self) -> bool:
		x_cor = self.segments[0].xcor()
		y_cor = self.segments[0].ycor()
		if (x_cor > 285 or x_cor < -285) or (y_cor > 285 or y_cor < -285):
			return False
		return True

	def check_tail_collision(self):
		for i in range(1, len(self.segments)):
			if self.segments[0].pos() == self.segments[i].pos():
				print("Collision with tail")
				return False
		return True

	# set the snake's direction
	def up(self):
		if self.segments[0].heading() != 270:
			self.segments[0].setheading(90)

	def down(self):
		if self.segments[0].heading() != 90:
			self.segments[0].setheading(270)

	def right(self):
		if self.segments[0].heading() != 180:
			self.segments[0].setheading(0)

	def left(self):
		if self.segments[0].heading() != 0:
			self.segments[0].setheading(180)
