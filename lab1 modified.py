import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
BACKGROUND_COLOR = (0, 0, 0)
AGENT_COLOR = (0, 255, 255)  # Blue
TEXT_COLOR = (255, 255, 255)
RESET_TIME = 60000  # 60 seconds (in milliseconds)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame AI Simulation Framework")

# Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 40)

# Agent class for the simulation
class Agent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(AGENT_COLOR)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = 5

    def reset_position(self):
        """Reset agent to initial position"""
        self.rect.x, self.rect.y = 300, 300

    def update(self, keys):
        """Update the agent's position based on key input."""
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed

# Setup the agent and sprite group
agent = Agent()
all_sprites = pygame.sprite.Group()
all_sprites.add(agent)

# Main loop
running = True
start_time = pygame.time.get_ticks()  # Track start time
while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if 60 seconds have passed
    if pygame.time.get_ticks() - start_time >= RESET_TIME:
        start_time = pygame.time.get_ticks()  # Reset timer
        agent.reset_position()  # Reset agent position
        screen.fill(BACKGROUND_COLOR)  # Clear screen

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Update the agent based on user input
    all_sprites.update(keys)

    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)

    # Draw the agent
    all_sprites.draw(screen)

    # Display the frame count as an example text (debug info)
    frame_text = font.render(f"Frame: {pygame.time.get_ticks() // 1000}", True, TEXT_COLOR)
    screen.blit(frame_text, (10, 10))

    # Flip the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()
