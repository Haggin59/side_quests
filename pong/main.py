#
import pygame
pygame.init()

WIDTH = 700
HEIGHT = 500
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 75

BALL_RADIUS = 6

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

#Creating paddle class
class Paddle:

    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    #Method for drawing paddle object
    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))

    #Method for moving the paddle
    def move(self, up=True):
        if up and self.y >= self.VEL:
            self.y -= self.VEL
        else:
            if self.y < HEIGHT - self.height:
                 self.y += self.VEL




#creating Ball class
class Ball:

    maxVel = 5

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velx = self.maxVel
        self.vely = 0

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velx
        self.y += self.vely





#Primary draw function for drawing items on the screen
def draw(win, paddles, ball):
    #window fill
    win.fill(BLACK)

    #drawing left & right paddles              
    for paddle in paddles:
        paddle.draw(win)


    #Midline
    pygame.draw.rect(WIN,WHITE,(WIDTH//2 - 1, 0, 2, HEIGHT))

    #drawing ball
    ball.draw(win)

    pygame.display.update()

#function that recieves key strokes and control the movement of paddles on the screen
def paddle_movement_handler(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up = True)
    if keys[pygame.K_s]:
        left_paddle.move(up = False)

    if keys[pygame.K_UP]:
        right_paddle.move(up = True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up = False)

#collision handler
def collision_handler(ball, left_paddle, right_paddle):

    #Collisions with the top and bottom
    if ball.y + ball.radius >= HEIGHT:
        ball.vely *= -1

    elif ball.y - ball.radius <= 0:
        ball.vely *= -1

    #collision with the paddles
    #left paddle
    if ball.velx < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + PADDLE_HEIGHT:
            if ball.x - ball.radius <= left_paddle.x + PADDLE_WIDTH:
                ball.velx *= -1

                y_mid = left_paddle.y + PADDLE_HEIGHT//2
                diif_y = y_mid - ball.y
                f = (PADDLE_HEIGHT/2)/ball.maxVel
                y_vel = diif_y/f
                ball.vely = -1 * y_vel

    #right_paddle
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + PADDLE_HEIGHT:
            if ball.x + ball.radius >= right_paddle.x :
                ball.velx *= -1

                y_mid = right_paddle.y + PADDLE_HEIGHT//2
                diif_y = y_mid - ball.y
                f = (PADDLE_HEIGHT/2)/ball.maxVel
                y_vel = diif_y/f
                ball.vely = -1 * y_vel



def main():
    run = True
    clock = pygame.time.Clock()

    #Paddle objects
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 -PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    while run:
        #limiting FPS
        clock.tick(FPS)

        #drawing items using draw function
        draw(WIN, [left_paddle,right_paddle], ball)

        #looping through various events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        paddle_movement_handler(keys, left_paddle, right_paddle)


        ball.move()
        collision_handler(ball, left_paddle, right_paddle)


    pygame.quit()


if __name__ == '__main__':
    main()








