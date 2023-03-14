import random
from turtle import Turtle

COORDINATE_LIST = [i for i in range(-280, 300, 20)]

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.color("blue")
		self.shapesize(0.5, 0.5)
		self.x_cor = random.choice(COORDINATE_LIST)
		self.y_cor = random.choice(COORDINATE_LIST)
		self.goto(x=self.x_cor, y=self.y_cor)
		self.count = 0

	def generate_new_food(self):
		self.x_cor = random.choice(COORDINATE_LIST)
		self.y_cor = random.choice(COORDINATE_LIST)
		self.goto(x=self.x_cor, y=self.y_cor)
		self.count += 1
