import pygame

pygame.init()

running = True
root: pygame.SurfaceType = pygame.display.set_mode(screenSize := (500, 500))
pygame.display.set_caption("Ping Pong")


class Paddle:
    def __init__(self, *, color=(255, 255, 255), size=(100, 10), y=465):
        self.dimensions = [
            (screenSize[0] - size[0]) // 2, y, size[0], size[1]
        ]
        self.color = color

    def move(self, change):
        if 0 <= self.dimensions[0] + change <= screenSize[0] - self.dimensions[2]:
            self.dimensions[0] += change

    def draw(self):
        pygame.draw.rect(root, self.color, self.dimensions)


class Ball:
    def __init__(self, *, color=(255, 255, 255), dimensions):
        self.dimensions = dimensions
        self.color = color
        self.dir = [0, 0]

    def draw(self):
        self.dimensions[0] += self.dir[0]
        self.dimensions[1] += self.dir[1]

        pygame.draw.rect(root, self.color, self.dimensions)

    def checkCollision(self, object):
        objDimensions = object.dimensions
        dimensions = self.dimensions

        if objDimensions[2] <= dimensions[2] + dimensions[3]/2 <= objDimensions[2] + objDimensions[3]:
            return True

        if dimensions[0] + dimensions[2] >= objDimensions[0] and dimensions[0] <= objDimensions[0] + objDimensions[2]:  # Find X
            if dimensions[1] + dimensions[3] == objDimensions[1]:  # Find Y
                return True


pad = Paddle(color=(40, 26, 13))
pad2 = Paddle(color=(40, 26, 13), y=25)
ball = Ball(dimensions=[screenSize[0] // 2, screenSize[1] // 2, 10, 10], color=(255, 0, 0))
ball.dir = [1, 1]
clock = pygame.time.Clock()
score = [0, 0]

while running:
    clock.tick(300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball.checkCollision(pad):
        ball.dir[1] = -ball.dir[1]
    elif ball.checkCollision(pad2):
        ball.dir[1] = -ball.dir[1]

    if ball.dimensions[0] <= 0:
        ball.dir[0] = 1
    elif ball.dimensions[0] >= screenSize[1]:
        ball.dir[0] = -1
    elif ball.dimensions[1] <= 0:
        ball.dir[1] = 1
        score[1] += 1
        ball.dimensions = [screenSize[0] // 2, screenSize[1] // 2, 10, 10]
    elif ball.dimensions[1] >= screenSize[1]:
        ball.dir[1] = -1
        score[0] += 1
        ball.dimensions = [screenSize[0] // 2, screenSize[1] // 2, 10, 10]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pad.move(-3)
    elif keys[pygame.K_RIGHT]:
        pad.move(3)
    if keys[pygame.K_a]:
        pad2.move(-3)
    elif keys[pygame.K_d]:
        pad2.move(3)
	
    
    #if ball.dimensions[0] + ball.dimensions[0]/2 < pad2.dimensions[0] + pad2.dimensions[0]/2:
    #    pad2.move(-3)
    #elif ball.dimensions[0] + ball.dimensions[0]/2 > pad2.dimensions[0] + pad2.dimensions[0]/2:
    #    pad2.move(3)

    root.fill((0, 0, 0))
    pad.draw()
    pad2.draw()
    ball.draw()

    pygame.display.update()
    pygame.display.set_caption(f"Ping Pong (Up: {score[0]} Down: {score[1]})")
