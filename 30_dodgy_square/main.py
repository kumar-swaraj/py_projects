import random
import sys

import pygame
from pygame.font import Font
from pygame.time import Clock

RGB = tuple[int, int, int]


class DodgySquare:
    def __init__(self) -> None:
        # Pygame initialization
        pygame.init()
        pygame.mouse.set_visible(False)

        # Screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode(
            size=(self.screen_width, self.screen_height)
        )
        pygame.display.set_caption("Dodgy Square")

        # Colors
        self.WHITE: RGB = (255, 255, 255)
        self.BLACK: RGB = (0, 0, 0)
        self.RED: RGB = (255, 99, 71)
        self.BLUE: RGB = (65, 105, 225)

        # Fonts
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, size=26)

        # Player
        self.player_size: int = 30
        self.player_pos: list[int] = [0, 0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_pos: list[int] = []
        self.enemy_list: list[list[int]] = []
        self.enemy_speed: float = 3  # Low = slow, High = Fast
        self.enemy_frequency: int = 20  # Low = Lots, High = Few (it means on each 20 frame a new enemy will appears so, 3enemies/sec [1sec = 60 frame])

        # Clock
        self.clock: Clock = pygame.time.Clock()

        # Game data
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int = 0

    def create_enemy(self):
        """Creates a new enemy at a random position."""

        enemy_pos = [
            random.randint(0, self.screen_width - self.enemy_size),
            -self.enemy_size,
        ]
        self.enemy_list.append(enemy_pos)

    # Function to update enemy positions
    def update_enemy_positions(self):
        """Check whether it is time to create a new enemy and then does so."""

        if self.frame_count % self.enemy_frequency == 0:
            self.create_enemy()

        # Give each enemy an id
        for idx, enemy_pos in enumerate(self.enemy_list):
            # Simulate gravity until off-screen
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed  # type: ignore # it's because of adding like int = int + float
            else:
                # When the enemy has passed
                self.enemy_list.pop(idx)
                self.score += 1
                self.enemy_speed += 0.1

                # Increase the difficulty each 15 points
                if self.enemy_frequency > 10:
                    if self.score % 15 == 0:
                        self.enemy_frequency -= 2
                        # print(self.score, self.enemy_frequency, sep=' -> ')

    def detect_collision(self, player_pos: list[int], enemy_pos: list[int]) -> bool:
        """Collision detection logic for checking if squares are intercepting."""

        px, py = player_pos
        ex, ey = enemy_pos
        if (px <= ex < (px + self.player_size)) or (ex <= px < (ex + self.enemy_size)):
            if (py <= ey < (py + self.player_size)) or (
                ey <= py < (ey + self.enemy_size)
            ):
                return True
        return False

    # Game over text
    def show_game_over(self):
        """Display game-over text."""

        # Create the text
        game_over_text = self.font.render("Game Over", True, self.WHITE)

        # Make sure the text is centred
        text_width, text_height = game_over_text.get_size()
        coordinates = (
            self.screen_width // 2 - text_width // 2,
            self.screen_height // 2 - text_height // 2,
        )
        self.screen.blit(game_over_text, coordinates)

    # Replay the game
    def replay_game(self):
        """Reset everything to its initial state."""

        # Reset enemies
        self.enemy_list = []
        self.enemy_speed = 3
        self.enemy_frequency = 20

        # Reset game stats
        self.game_over = False
        self.frame_count = 0
        self.score = 0

    def draw_character(self, color: RGB, position: list[int], size: int):
        """Draws a rectangle on the screen."""

        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))

    # Main game loop
    def run(self):
        """Run the game."""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle key events
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_r:
                        self.replay_game()

                # Get the current mouse position
                mouse_pos = pygame.mouse.get_pos()

                # Update the player's position to follow the mouse
                self.player_pos[0] = mouse_pos[0] - self.player_size // 2
                self.player_pos[1] = mouse_pos[1] - self.player_size // 2

                # Make sure the player stays on the screen
                self.player_pos[0] = max(
                    0, min(self.player_pos[0], self.screen_width - self.player_size)
                )
                self.player_pos[1] = max(
                    0, min(self.player_pos[1], self.screen_height - self.player_size)
                )

            if not self.game_over:
                self.update_enemy_positions()

                # Check for collisions
                for enemy_pos in self.enemy_list:
                    if self.detect_collision(self.player_pos, enemy_pos):
                        self.game_over = True
                        break

                # Reset everything for the next frame
                self.screen.fill(self.BLACK)

                # Draw the player
                self.draw_character(self.WHITE, self.player_pos, self.player_size)

                # Draw the enemies
                for enemy_pos in self.enemy_list:
                    if self.score > 100:
                        self.draw_character(self.BLUE, enemy_pos, self.enemy_size)
                    else:
                        self.draw_character(self.RED, enemy_pos, self.enemy_size)

                # Display the score
                score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
                self.screen.blit(score_text, [10, 10])

                # Increment the frame count
                self.frame_count += 1
            else:
                self.show_game_over()

            # Update the display
            pygame.display.update()

            # Frame rate
            self.clock.tick(60)


# Run the game
if __name__ == "__main__":
    game = DodgySquare()
    game.run()
