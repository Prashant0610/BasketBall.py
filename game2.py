import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Load images
basket_img = pygame.image.load('assets/basket.png')
object_img = pygame.image.load('assets/object.png')

# Basket properties
basket_width = basket_img.get_width()
basket_height = basket_img.get_height()
basket_x = (SCREEN_WIDTH - basket_width) // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 7

# Object properties
object_width = object_img.get_width()
object_height = object_img.get_height()
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height
object_speed = 5

# Game properties
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed

    # Keep basket on screen
    if basket_x < 0:
        basket_x = 0
    if basket_x > SCREEN_WIDTH - basket_width:
        basket_x = SCREEN_WIDTH - basket_width

    # Move object
    object_y += object_speed

    # Check if object is caught
    if (object_y + object_height > basket_y) and (object_x + object_width > basket_x) and (object_x < basket_x + basket_width):
        score += 1
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_y = -object_height
        object_speed += 0.5  # Increase speed after each catch

    # Check if object is missed
    if object_y > SCREEN_HEIGHT:
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_y = -object_height
        object_speed = 5  # Reset speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the basket
    screen.blit(basket_img, (basket_x, basket_y))

    # Draw the object
    screen.blit(object_img, (object_x, object_y))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
