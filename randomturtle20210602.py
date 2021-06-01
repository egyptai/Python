Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> import random
>>> t.shape("turtle")
>>> t.speed(0)
>>> for x in range(500):
	a = random.randint(1, 360)
	t.setheading(a)
	t.forward(10)

	
>>> 