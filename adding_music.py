import pyxel
import random
from random import randint

class Star(object):
	def __init__(self,x,y):
		self._x = x
		self._y = y
		self._is_alive = True
		self._color = 7

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def is_alive(self):
		return self._is_alive
	
	@property
	def is_alive(self):
		return self._is_alive

	@is_alive.setter
	def is_alive(self,value):
		self._is_alive = value
	
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self,value):
		self._color = value	
	
class Pixel(object):
	def __init__(self,x,y):
		self._x = x
		self._y = y
		self._is_alive = True
		self._color = 8

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def is_alive(self):
		return self._is_alive

	@is_alive.setter
	def is_alive(self,value):
		self._is_alive = value
	
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self,value):
		self._color = value

class App(object):
	def __init__(self, x, y, caption, fps):
		print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
		self._startstars = 20
		self._startpixels = 60

		self.x = int(x / 2)
		self.y = int(y / 2)
		self.points = 0
		self.stars = [Star(random.choice([randint(10,int(x / 2)-20),randint(int(x / 2)+20,x-10)]),random.choice([randint(10,int(y / 2)-20),randint(int(y / 2)+20,y-10)])) for i in range(self._startstars)]
		self.pixels = [Pixel(random.choice([randint(10,int(x / 2)-20),randint(int(x / 2)+20,x-10)]),random.choice([randint(10,int(y / 2)-20),randint(int(y / 2)+20,y-10)])) for i in range(self._startpixels)]
		pyxel.init(x,y, caption = caption, fps = fps)
		pyxel.sound(0).set("e3e3c3f1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr","p","6","vffn fnff vffs vfnn",25,)
		pyxel.sound(1).set("r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ","s","6","nnff vfff vvvv vfff svff vfff vvvv svnn",25,)
		pyxel.sound(2).set("c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1","t","7","n",25,)
		pyxel.sound(3).set("f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1","t","7","n",25,)
		pyxel.sound(4).set("f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25)
		self.play_music()
		pyxel.run(self.update, self.draw)

	def draw_rect(self, x, y, color):
		pyxel.rect(x,y,x+10,y+10,color)

	def draw_pix(self,pixel):
		pyxel.pset(pixel.x, pixel.y, pixel.color)
	
	def draw_star(self, star):
		pyxel.line(star.x - 2, star.y, star.x + 2, star.y, star.color)
		pyxel.line(star.x, star.y - 2, star.x, star.y + 2, star.color)
		pyxel.line(star.x - 2, star.y - 2, star.x + 2, star.y + 2, star.color)
		pyxel.line(star.x - 2, star.y + 2, star.x + 2, star.y - 2, star.color)

	def draw_text(self,points):
		pyxel.text(0,0,"Current points: {}".format(points),10)

	def play_music(self):
		pyxel.play(0, [0, 1], loop=True)
		pyxel.play(1, [2, 3], loop=True)
		pyxel.play(2, 4, loop=True)
        
	def update(self):
		
		if pyxel.btn(pyxel.KEY_UP):
			self.y = (self.y - 1) % (pyxel.height - 10)
		if pyxel.btn(pyxel.KEY_DOWN):
			self.y = (self.y + 1) % (pyxel.height - 10)
		if pyxel.btn(pyxel.KEY_LEFT):
			self.x = (self.x - 1) % (pyxel.width - 10)
		if pyxel.btn(pyxel.KEY_RIGHT):
			self.x = (self.x + 1) % (pyxel.width - 10)
		if pyxel.btn(pyxel.KEY_Q):
			pyxel.quit()

		for pixel in self.pixels:
			if (pixel.x in range(self.x, self.x + 11)) and (pixel.y in range(self.y, self.y + 11)) and pixel.is_alive:
				pixel.is_alive = False
				pixel.color = 0
				self.points += 1


		for star in self.stars:
			x_found = False
			y_found = False
			for x in [star.x + 3,star.x + 2,star.x + 1,star.x,star.x - 1, star.x - 2, star.x - 3]:
				if x in range(self.x, self.x + 10) and star.is_alive:
					x_found = True
					break

			for y in [star.y + 3,star.y + 2,star.y + 1,star.y,star.y - 1, star.y - 2, star.y - 3]:
				if y in range(self.y, self.y + 10) and star.is_alive:
					y_found = True
					break

			if x_found and y_found:
				star.is_alive = False
				star.color = 0
				self.points += 5

		if len([ _ for _ in self.pixels if _.is_alive ]) < self._startpixels:
			if self.x < 11:
				new_X = random.randrange(20,pyxel.width)
			else:
				new_X = random.choice([random.randrange(10,self.x),random.randrange(self.x + 10, pyxel.width)])

			if self.y < 11:
				new_Y = random.randrange(20,pyxel.height)
			else:
				new_Y = random.choice([random.randrange(10,self.y),random.randrange(self.y + 10, pyxel.height)])

			self.pixels.append(Pixel(new_X,new_Y))

		if len([ _ for _ in self.stars if _.is_alive ]) < self._startstars:
			if self.x < 11:
				new_X = random.randrange(20,pyxel.width)
			else:
				new_X = random.choice([random.randrange(10,self.x),random.randrange(self.x + 10, pyxel.width)])

			if self.y < 11:
				new_Y = random.randrange(20,pyxel.height)
			else:
				new_Y = random.choice([random.randrange(10,self.y),random.randrange(self.y + 10, pyxel.height)])
			self.stars.append(Star(new_X,new_Y))

	
	def draw(self):
		pyxel.cls(0)
		self.draw_text(self.points)
		self.draw_rect(self.x, self.y, 11)
		for star in self.stars:
			if star.is_alive:
				self.draw_star(star)

		for pixel in self.pixels:
			if pixel.is_alive:
				self.draw_pix(pixel)




App(160,160,"Stars", 30)