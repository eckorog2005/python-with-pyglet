import pyglet

window = pyglet.window.Window(640,480)

MIN_LABEL_Y = 0
MAX_LABEL_Y = 480
MIN_LABEL_X = 0
MAX_LABEL_X = 640
x = 1
y = 1
COORDS_PER_SECOND = 100

label = pyglet.text.Label('UFC on FOX 5!', font_size=18, x=10, y=20)

@window.event
def on_draw():
	window.clear()
	label.draw()

ycoord = 20
xcoord = 10
	
def update(dt):
	global ycoord
	global xcoord
	global x
	global y
	tempy = label.y
	tempx = label.x
	if y == 1:
		ycoord += COORDS_PER_SECOND * dt
	else:
		ycoord -= COORDS_PER_SECOND * dt
	if x == 1:
		xcoord += COORDS_PER_SECOND * dt
	else:
		xcoord -= COORDS_PER_SECOND * dt
	label.y = int(ycoord)
	label.x = int(xcoord)
	if label.y > (MAX_LABEL_Y - label.content_height):
		label.y = ycoord = tempy
		y = 0
	if label.x > (MAX_LABEL_X - label.content_width):
		label.x = xcoord = tempx
		x = 0
	if label.y < MIN_LABEL_Y:
		label.y = ycoord = tempy
		y = 1
	if label.x < MIN_LABEL_X:
		label.x = xcoord = tempx
		x = 1
		
pyglet.clock.schedule_interval(update, 1/60.0)
	
pyglet.app.run()
