import pygame
import random
import sys # This is where all the relevant modules are imported. Ideally this works, when it didn't, I did it manually.
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # This determines the screen size on which the images will be displayed.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Randomized Animated Instances")
clock = pygame.time.Clock()
class MovingImage(pygame.sprite.Sprite): # This is where the classes are defined that will be used throughout the code.
    def __init__(self, base_image):
        super().__init__()
        self.image = base_image.copy()
        random_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.image.fill(random_color, special_flags=pygame.BLEND_RGBA_MULT)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-100, -40)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 100)
        self.speed_x = random.randint(2, 6)
        self.speed_y = random.randint(-2, 2)
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(50, SCREEN_HEIGHT - 100)
            self.speed_x = random.randint(2, 6)
base_surface = pygame.image.load('mercedes.jpg').convert_alpha() # This is where the image is loaded and the different attributes are assigned to the image.
base_surface = pygame.transform.scale(base_surface, (50, 50))
all_sprites = pygame.sprite.Group()
for _ in range(15):
    new_instance = MovingImage(base_surface)
    all_sprites.add(new_instance)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60) # This actually displays the modified Mercedes sprites to create what is seen when one runs the code.
pygame.quit()
sys.exit()

# For this week's assignment I decided to make images of a Mercedes Formula 1 racing car move all over the place. As per the assignment, I implemented varying speeds and colors using GeminiAI. I manually imported pygame, since the regular import at the top of the code was not working.