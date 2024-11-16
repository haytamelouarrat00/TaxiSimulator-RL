import pygame


class BLOCK:
    def __init__(self, screen, height, width, pos):
        self.height = height
        self.width = width
        self.screen = screen
        self.pos = (pos[0], pos[1])

    def draw_block(self):
        pygame.draw.rect(
            self.screen, (0, 0, 0),
            (self.pos[0], self.pos[1], self.width, self.height)
        )

    def get_rect(self):
        """Get the rectangle representing the block."""
        return pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


class TAXI:
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # Red
        self.speed = 5  # Speed of the taxi

    def draw_taxi(self):
        pygame.draw.rect(
            self.screen, self.color,
            (self.x, self.y, self.width, self.height)
        )

    def move(self, dx, dy):
        """Move the taxi by a given amount."""
        self.x += dx
        self.y += dy

    def get_rect(self):
        """Get the rectangle representing the taxi."""
        return pygame.Rect(self.x, self.y, self.width, self.height)


class MAP:
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("TAXI")
        self.clock = pygame.time.Clock()

        # Initialize the taxi
        self.taxi = TAXI(self.window, 4, 9, 17, 26)

    def draw_lines(self):
        YELLOW = (255, 255, 0)
        # Top section
        pygame.draw.line(self.window, YELLOW, (25, 25), (25, 100), 2)
        pygame.draw.line(self.window, YELLOW, (25, 125), (150, 125), 2)
        pygame.draw.line(self.window, YELLOW, (175, 150), (175, 225), 2)
        pygame.draw.line(self.window, YELLOW, (25, 225), (100, 225), 2)
        pygame.draw.line(self.window, YELLOW, (125, 250), (125, 350), 2)
        pygame.draw.line(self.window, YELLOW, (50, 375), (300, 375), 2)
        pygame.draw.line(self.window, YELLOW, (25, 400), (25, 575), 2)
        pygame.draw.line(self.window, YELLOW, (325, 400), (325, 500), 2)
        pygame.draw.line(self.window, YELLOW, (325, 150), (325, 250), 2)

        pygame.draw.line(self.window, YELLOW, (350, 275), (400, 275), 2)
        pygame.draw.line(self.window, YELLOW, (425, 150), (425, 250), 2)
        pygame.draw.line(self.window, YELLOW, (400, 125), (350, 125), 2)

        pygame.draw.line(self.window, YELLOW, (275, 25), (275, 100), 2)
        pygame.draw.line(self.window, YELLOW, (200, 125), (300, 125), 2)
        pygame.draw.line(self.window, YELLOW, (425, 100), (425, 50), 2)
        pygame.draw.line(self.window, YELLOW, (450, 25), (650, 25), 2)
        pygame.draw.line(self.window, YELLOW, (675, 200), (675, 25), 2)
        pygame.draw.line(self.window, YELLOW, (450, 275), (500, 275), 2)
        pygame.draw.line(self.window, YELLOW, (675, 275), (550, 275), 2)
        pygame.draw.line(self.window, YELLOW, (325, 300), (325, 350), 2)
        pygame.draw.line(self.window, YELLOW, (350, 425), (500, 425), 2)
        pygame.draw.line(self.window, YELLOW, (525, 400), (525, 300), 2)
        pygame.draw.line(self.window, YELLOW, (350, 425), (500, 425), 2)
        pygame.draw.line(self.window, YELLOW, (675, 425), (550, 425), 2)
        pygame.draw.line(self.window, YELLOW, (300, 525), (175, 525), 2)
        pygame.draw.line(self.window, YELLOW, (175, 525), (175, 575), 2)
        pygame.draw.line(self.window, YELLOW, (325, 575), (500, 575), 2)
        pygame.draw.line(self.window, YELLOW, (525, 450), (525, 550), 2)
        pygame.draw.line(self.window, YELLOW, (550, 575), (750, 575), 2)
        pygame.draw.line(self.window, YELLOW, (775, 375), (775, 550), 2)
        pygame.draw.line(self.window, YELLOW, (725, 375), (775, 375), 2)
        pygame.draw.line(self.window, YELLOW, (725, 250), (725, 350), 2)
        pygame.draw.line(self.window, YELLOW, (675, 225), (775, 225), 2)
        pygame.draw.line(self.window, YELLOW, (325, 550), (325, 575), 2)

    def check_collision(self, blocks):
        """Check if the taxi collides with any block."""
        taxi_rect = self.taxi.get_rect()
        for block in blocks:
            if taxi_rect.colliderect(block.get_rect()):
                print("Collision detected!")
                return True
        return False

    def run(self):
        # Create BLOCK objects
        blocks = [
            BLOCK(self.window, 100, 200, (50, 0)),
            BLOCK(self.window, 100, 100, (300, 0)),
            BLOCK(self.window, 200, 200, (450, 50)),
            BLOCK(self.window, 200, 100, (700, 0)),
            BLOCK(self.window, 50, 150, (0, 150)),
            BLOCK(self.window, 200, 100, (200, 150)),
            BLOCK(self.window, 100, 100, (150, 250)),
            BLOCK(self.window, 100, 100, (0, 250)),
            BLOCK(self.window, 100, 50, (350, 150)),
            BLOCK(self.window, 100, 150, (350, 300)),
            BLOCK(self.window, 100, 150, (550, 300)),
            BLOCK(self.window, 100, 50, (750, 250)),
            BLOCK(self.window, 200, 100, (50, 400)),
            BLOCK(self.window, 100, 150, (150, 400)),
            BLOCK(self.window, 100, 150, (350, 450)),
            BLOCK(self.window, 100, 150, (550, 450)),
            BLOCK(self.window, 50, 100, (200, 550)),
            BLOCK(self.window, 150, 50, (700, 400))
        ]

        running = True

        # Movement variables
        move_x, move_y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
                    mouse_pos = pygame.mouse.get_pos()  # Get mouse coordinates
                    print(f"Mouse clicked at: {mouse_pos}")
                elif event.type == pygame.KEYDOWN:  # Detect key press
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        move_y = -self.taxi.speed
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        move_y = self.taxi.speed
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        move_x = -self.taxi.speed
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        move_x = self.taxi.speed
                elif event.type == pygame.KEYUP:  # Detect key release
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_s):
                        move_y = 0
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                        move_x = 0

            # Move the taxi
            self.taxi.move(move_x, move_y)

            # Check for collisions
            self.check_collision(blocks)

            # Fill the screen with a background color
            self.window.fill((72, 115, 146))

            # Draw the blocks
            for b in blocks:
                b.draw_block()

            # Draw the yellow lines
            self.draw_lines()

            # Draw the taxi
            self.taxi.draw_taxi()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(self.FPS)

        pygame.quit()


if __name__ == "__main__":
    # Create a MAP instance and run the game
    game_map = MAP()
    game_map.run()
