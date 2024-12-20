import pygame
import sys
from player import Player
import obstacles
from alien import Alien, Extra
from random import choice, randint
from laser import Laser

class Game:
    def __init__(self):
        # Player Setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # health and score setup
        self.lives = 3
        self.live_surf = pygame.image.load('Graphics\Player.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font("./Font/Pixeled.ttf", 20)

        # obstacle setup
        self.shape = obstacles.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amt = 4
        self.obstacle_x_pos = [num * (screen_width / self.obstacle_amt) for num in range(self.obstacle_amt)]
        self.create_multiple_obstacle(*self.obstacle_x_pos, x_start = screen_width / 15, y_start = 480)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_laser = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
        self.aliens_direction = 1

        # Extra setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # Audio
        music = pygame.mixer.Sound("./Audio/Music.wav")
        music.set_volume(0.2)
        music.play(loops = -1)
        self.laser_sound = pygame.mixer.Sound('./Audio/Laser.wav')
        self.laser_sound.set_volume(0.2)
        self.explosion_sound = pygame.mixer.Sound('./Audio/Explosion.wav')
        self.explosion_sound.set_volume(0.5)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_idx, row in enumerate(self.shape):
            for col_idx, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_idx * self.block_size + offset_x
                    y = y_start + row_idx * self.block_size
                    block = obstacles.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)
    
    def create_multiple_obstacle(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, cols, x_dist = 60, y_dist = 48, x_offset = 70, y_offset = 100):

        for row_idx, row in enumerate(range(rows)):
            for col_idx, col in enumerate(range(cols)):
                x = col_idx * x_dist + x_offset
                y = row_idx * y_dist + y_offset

                if row_idx == 0: 
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_idx <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_pos_check(self):

        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:    
                self.aliens_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.aliens_direction = 1
                self.alien_move_down(2)

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6 , screen_height)
            self.alien_laser.add(laser_sprite)
            self.laser_sound.play()

    def alien_move_down(self, dist):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += dist
    
    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(["right", "left"]), screen_width, ))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        # Player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:

                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # alien collisions
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play()

                # extra collisions
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.score += 500
                    laser.kill()

        # Alien lasers
        if self.alien_laser:
            for laser in self.alien_laser:
                # obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.blocks, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()

        # aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, True):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f'Score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (10, -10))
        screen.blit(score_surf, score_rect)

    def victory_msg(self):
        if not self.aliens.sprites():
            vict_surf = self.font.render('You Won', False, 'white')
            vict_rect = vict_surf.get_rect(center = (screen_width / 2, screen_height / 2))
            screen.blit(vict_surf, vict_rect)
    
    def run(self):
        self.player.update()
        self.alien_laser.update()
        self.extra.update()
        
        self.aliens.update(self.aliens_direction)
        self.alien_pos_check()
        self.extra_alien_timer()
        self.collision_checks()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_laser.draw(screen)
        self.extra.draw(screen)
        self.display_lives()
        self.display_score()
        self.victory_msg()

class CRT:
    def __init__(self):
        self.tv = pygame.image.load("./Graphics/TV.png").convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (screen_width, screen_height))

    def craete_crt_lines(self):
        line_height = 3
        line_amt = int(screen_height / line_height)
        for line in range(line_amt):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (screen_width, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(75,90))
        self.craete_crt_lines()
        screen.blit(self.tv, (0, 0))

if __name__=='__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    crt = CRT()

    ALEINLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALEINLASER, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALEINLASER:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()
        crt.draw()
         
        pygame.display.flip()
        clock.tick(60)