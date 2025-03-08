import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
BACKGROUND_COLOR = (0, 0, 0)
AGENT_COLOR = (0, 255, 255)  # Blue
RED_AGENT_COLOR = (255, 0, 0)  # Red
TEXT_COLOR = (255, 255, 255)
RESET_TIME = 60000  # 60 seconds (in milliseconds)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame AI Simulation Framework")

# Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)

# Agent class for the simulation
class Agent(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, controls):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.start_x, self.start_y = start_x, start_y
        self.reset_position()
        self.speed = 5
        self.controls = controls  # Dictionary for movement keys

    def reset_position(self):
        """Reset agent to initial position"""
        self.rect.x, self.rect.y = self.start_x, self.start_y

    def update(self, keys):
        """Update the agent's position based on key input."""
        if keys[self.controls['left']] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[self.controls['right']] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
        if keys[self.controls['up']] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.controls['down']] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed

# Setup the agents
blue_agent = Agent(AGENT_COLOR, 100, 100, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN})
red_agent = Agent(RED_AGENT_COLOR, 300, 200, {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s})

# Add agents to sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(blue_agent, red_agent)

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
        blue_agent.reset_position()  # Reset blue agent position
        red_agent.reset_position()  # Reset red agent position
        screen.fill(BACKGROUND_COLOR)  # Clear screen

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Update agents based on user input
    all_sprites.update(keys)

    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)

    # Draw the agents
    all_sprites.draw(screen)

    # Display the frame count as an example text (debug info)
    frame_text = font.render(f"Frame: {pygame.time.get_ticks() // 1000}", True, TEXT_COLOR)
    screen.blit(frame_text, (10, 10))

    # Flip the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()
