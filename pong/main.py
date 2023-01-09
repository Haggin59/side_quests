import pygame
pygame.init()

WIDTH = 700
HEIGHT = 500
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 75

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

#Creating paddle class
class Paddle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    #Method for drawing paddle object
    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))


#Primary draw function for drawing items on the screen
def draw(win, paddles):
    #window fill
    win.fill(BLACK)

    #drawing left & right paddles              
    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    #Paddle objects
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 -PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        #limiting FPS
        clock.tick(FPS)

        #drawing items using draw function
        draw(WIN, [left_paddle,right_paddle])

        #looping through various events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()


if __name__ == '__main__':
    main()








