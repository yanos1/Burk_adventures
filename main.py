import pygame
import os
import random

pygame.init()
win_width = 1000
win_height = 500
win = pygame.display.set_mode((win_width, win_height))

bg_img = pygame.transform.scale(pygame.image.load("desert_BG.png"), (1000,500))

standing_picture = pygame.image.load(os.path.join("Hero", "Standing.png"))

right_pictures = [pygame.image.load(os.path.join("Hero", "R1.png")),
                  pygame.image.load(os.path.join("Hero", "R2.png")),
                  pygame.image.load(os.path.join("Hero", "R3.png")),
                  pygame.image.load(os.path.join("Hero", "R4.png")),
                  pygame.image.load(os.path.join("Hero", "R5.png")),
                  pygame.image.load(os.path.join("Hero", "R6.png")),
                  pygame.image.load(os.path.join("Hero", "R7.png")),
                  pygame.image.load(os.path.join("Hero", "R8.png")),
                  pygame.image.load(os.path.join("Hero", "R9.png")),
                   ]
left_pictures = [pygame.image.load(os.path.join("Hero", "L1.png")),
                 pygame.image.load(os.path.join("Hero", "L2.png")),
                 pygame.image.load(os.path.join("Hero", "L3.png")),
                 pygame.image.load(os.path.join("Hero", "L4.png")),
                 pygame.image.load(os.path.join("Hero", "L5.png")),
                 pygame.image.load(os.path.join("Hero", "L6.png")),
                 pygame.image.load(os.path.join("Hero", "L7.png")),
                 pygame.image.load(os.path.join("Hero", "L8.png")),
                 pygame.image.load(os.path.join("Hero", "L9.png")),
                  ]
left_enemy = [pygame.image.load(os.path.join("Enemy", "EL1.png")),
              pygame.image.load(os.path.join("Enemy", "EL2.png")),
              pygame.image.load(os.path.join("Enemy", "EL3.png")),
              pygame.image.load(os.path.join("Enemy", "EL4.png")),
              pygame.image.load(os.path.join("Enemy", "EL5.png")),
              pygame.image.load(os.path.join("Enemy", "EL6.png")),
              pygame.image.load(os.path.join("Enemy", "EL7.png")),
              pygame.image.load(os.path.join("Enemy", "EL8.png")),
              pygame.image.load(os.path.join("Enemy", "EL9.png")),
              pygame.image.load(os.path.join("Enemy", "EL10.png")),
              pygame.image.load(os.path.join("Enemy", "EL11.png"))
              ]
right_enemy = [pygame.image.load(os.path.join("Enemy", "ER1.png")),
               pygame.image.load(os.path.join("Enemy", "ER2.png")),
               pygame.image.load(os.path.join("Enemy", "ER3.png")),
               pygame.image.load(os.path.join("Enemy", "ER4.png")),
               pygame.image.load(os.path.join("Enemy", "ER5.png")),
               pygame.image.load(os.path.join("Enemy", "ER6.png")),
               pygame.image.load(os.path.join("Enemy", "ER7.png")),
               pygame.image.load(os.path.join("Enemy", "ER8.png")),
               pygame.image.load(os.path.join("Enemy", "ER9.png")),
               pygame.image.load(os.path.join("Enemy", "ER10.png")),
               pygame.image.load(os.path.join("Enemy", "ER11.png")),
               ]

right_enemy2 = [pygame.image.load(os.path.join("Enemy2", "NER_1.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_2.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_3.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_4.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_5.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_6.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_7.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_8.png")),
                pygame.image.load(os.path.join("Enemy2", "NER_9.png")),
                ]

left_enemy2 = [pygame.image.load(os.path.join("Enemy2", "NEL_1.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_2.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_3.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_4.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_5.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_6.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_7.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_8.png")),
               pygame.image.load(os.path.join("Enemy2", "NEL_9.png")),
               ]
spawn_enemy_img = [pygame.image.load(os.path.join("Enemy2", "EF_1.png")),
                   pygame.image.load(os.path.join("Enemy2", "EF_1.png")),
                   pygame.image.load(os.path.join("Enemy2", "EF_1.png")),
                   pygame.image.load(os.path.join("Enemy2", "EF_1.png")),
                   ]
enemy_shoot_left_img = [pygame.image.load(os.path.join("Enemy2.shoot", "ESL1.png")),
                        pygame.image.load(os.path.join("Enemy2.shoot", "ESL2.png")),
                        pygame.image.load(os.path.join("Enemy2.shoot", "ESL3.png")),
                        pygame.image.load(os.path.join("Enemy2.shoot", "ESL4.png")),
                        pygame.image.load(os.path.join("Enemy2.shoot", "ESL5.png")),
                        pygame.image.load(os.path.join("Enemy2.shoot", "ESL6.png")),
                        pygame.image.load(os.path.join("Enemy2.shoot", "ESL7.png"))
                        ]
enemy_shoot_right_img = [pygame.image.load(os.path.join("Enemy2.shoot", "ESR1.png")),
                         pygame.image.load(os.path.join("Enemy2.shoot", "ESR2.png")),
                         pygame.image.load(os.path.join("Enemy2.shoot", "ESR3.png")),
                         pygame.image.load(os.path.join("Enemy2.shoot", "ESR4.png")),
                         pygame.image.load(os.path.join("Enemy2.shoot", "ESR5.png")),
                         pygame.image.load(os.path.join("Enemy2.shoot", "ESR6.png")),
                         pygame.image.load(os.path.join("Enemy2.shoot", "ESR7.png"))
                         ]
enemy_bullet = pygame.transform.scale(pygame.image.load(os.path.join("enemy.bullet", "enemy.bullet.png")), (22, 22))
bullet_image = pygame.transform.scale(pygame.image.load(os.path.join("Bullet", "bullet3.png")), (14, 14))
bullet_image_left = pygame.transform.scale(pygame.image.load(os.path.join("Bullet", "bullet_left.png")), (14, 14))
pygame.display.set_caption("Failure")

run = True


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 10
        self.face_right = True
        self.face_left = False
        self.jump = False
        self.vel_y = 10
        self.step_index = 0
        self.bullets = []
        self.cool_down_count = 0
        self.health = 130
        self.hitbox = (self.x + 10, self.y + 5, 26, 40)
        self.health_bar_red = (50, 40 , 70, 8)
        self.health_bar_green = (50, 40, self.health, 8)
        self.lives = 1
        self.alive = True
        self.kills = 0
        self.level = 1

    def move_hero(self, user_input):
        if user_input[pygame.K_RIGHT] and self.x < 965:
            self.x += self.vel_x
            self.face_right = True
            self.face_left = False
        elif user_input[pygame.K_LEFT] and self.x > 0:
            self.face_left = True
            self.face_right = False
            self.x -= self.vel_x

        else:
            self.step_index = 0

    def draw_hero(self, win):
        if self.step_index >= 9:
            self.step_index = 0

        if self.face_left:
            win.blit(left_pictures[self.step_index], (self.x, self.y))
            self.step_index += 1

        elif self.face_right:
            win.blit(right_pictures[self.step_index], (self.x, self.y))
            self.step_index += 1

        self.hitbox = (self.x + 10, self.y + 5, 26, 40)

        self.health_bar_red = (110, 40, 130, 19)
        self.health_bar_green = (110, 40, self.health, 19)
        pygame.draw.rect(win, (255, 64, 64), self.health_bar_red, 0)
        pygame.draw.rect(win, (127, 255, 0), self.health_bar_green, 0)

    def jump_motion(self, user_input):
        if user_input[pygame.K_UP] and self.jump is False:
            self.jump = True

        if self.jump is True:
            self.y -= self.vel_y*2
            self.vel_y -= 1

        if self.vel_y < -10:
            self.vel_y = 10
            self.jump = False

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def cool_down(self):
        if self.cool_down_count == 10:
            self.cool_down_count = 0
        if self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):

        self.cool_down()
        if user_input[pygame.K_SPACE] and self.cool_down_count == 0:
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in player.bullets:
            bullet.move_bullet()
            if bullet.off_screen():
                self.bullets.remove(bullet)


    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets:
                if enemy.hitbox[0] < bullet.x < enemy.hitbox[2] + enemy.hitbox[0] and enemy.hitbox [1] < bullet.y < enemy.hitbox[3] + enemy.hitbox[1]:
                    enemy.health -= 10
                    self.bullets.remove(bullet)
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                        self.kills += 1

        for enemy2 in enemies2:
            for bullet in self.bullets:
                if enemy2.hitbox[0] < bullet.x < enemy2.hitbox[2] + enemy2.hitbox[0] and enemy2.hitbox[1] < bullet.y < enemy2.hitbox[3] + enemy2.hitbox[1]:
                    enemy2.health -= 7
                    self.bullets.remove(bullet)
                    if enemy2.health <= 0:
                        enemies2.remove(enemy2)
                        self.kills += 1

    def level_up(self):
        if self.kills == 5:
            self.level = 1
        elif self.kills == 10:
            self.level = 2
        elif self.kills == 15:
            self.level = 3
        elif self.kills == 20:
            self.level = 4
        elif self.kills == 25:
            self.level = 5
        elif self.kills == 30:
            self.level = 6


class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.step_index_enemy = 0
        self.direction = direction
        self.hitbox = (self.x + 15, self.y + 10, 25, 50)
        self.health_bar_red = (self.x -8, self.y - 10, 70, 8)
        self.health_bar_green = (self.x -8, self.y - 10, 70, 8)
        self.health = 70
        self.enemy_timer = 0

    def draw(self, win):
        if self.step_index_enemy == 33:
            self.step_index_enemy = 0

        self.hitbox = (self.x + 15, self.y + 10, 25, 50)
        self.health_bar_red = (self.x -8 , self.y - 10, 70, 8)
        self.health_bar_green = (self.x - 8, self.y - 10, self.health, 8)
        pygame.draw.rect(win, (255,64, 64), self.health_bar_red, 0)
        pygame.draw.rect(win, (127, 255, 0), self.health_bar_green, 0)

        if self.direction == "left":
            win.blit(left_enemy[self.step_index_enemy//3], (self.x, self.y))
            self.step_index_enemy += 1

        if self.direction == "right":
            win.blit(right_enemy[self.step_index_enemy // 3], (self.x, self.y))
            self.step_index_enemy += 1

    def move(self):
        if self.direction == "right":
            self.x += 3

        if self.direction == "left":
            self.x -= 3

    def off_screen(self):
        return not(self.x>= -50 and self.x <= 1000)

    def hit(self):
        for enemy in enemies:
            if player.hitbox[0] < enemy.hitbox[0] < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy.hitbox[1] < player.hitbox[1] + player.hitbox[3]:
                if player.health > 0:
                    player.health -= 1

                if player.health == 1 and player.lives > 0:
                    player.lives -= 1
                    player.health = 130

                elif player.health == 1 and player.lives == 0:
                    player.alive = False


class Enemy2:
    def __init__(self, x, y, direction, name):
        self.x = x
        self.y = y
        self.step_index_enemy2 = 0
        self.direction = direction
        self.name = name
        self.hitbox = (self.x + 15, self.y + 10, 25, 50)
        self.health_bar_red = (self.x -8, self.y - 10, 70, 8)
        self.health_bar_green = (self.x -8, self.y - 10, 70, 8)
        self.health = 70
        self.spawned = True
        self.vel_y = 10
        self.fire = False
        self.shoot_step_index = 0
        self.shoot_cd = 0



    def spawn(self):
        if self.spawned:
            win.blit(spawn_enemy_img[0], (self.x, self.y))
            self.y += self.vel_y
        if self.y == 380:
            self.vel_y = 0
            self.spawned = False

    def draw(self, win):
        if self.y == 380:
            if self.step_index_enemy2 == 27:
                self.step_index_enemy2 = 0

            self.hitbox = (self.x + 15, self.y + 10, 25, 50)
            self.health_bar_red = (self.x -8 , self.y - 10, 70, 8)
            self.health_bar_green = (self.x - 8, self.y - 10, self.health, 8)
            pygame.draw.rect(win, (255,64, 64), self.health_bar_red, 0)
            pygame.draw.rect(win, (127, 255, 0), self.health_bar_green, 0)

        if self.y == 380 and self.fire is False:
            if self.direction == "left":
                win.blit(left_enemy2[self.step_index_enemy2//3], (self.x, self.y))
                self.step_index_enemy2 += 1

            if self.direction == "right":
                win.blit(right_enemy2[self.step_index_enemy2 // 3], (self.x, self.y))
                self.step_index_enemy2 += 1

    def move(self):
        if self.y == 380 and self.fire is False:
            if self.direction == "right":
                self.x += 3

            if self.direction == "left":
                self.x -= 3

    def off_screen(self):
        return not(self.x>= -50 and self.x <= 1000)

    def hit(self):
        for enemy2 in enemies2:
            if player.hitbox[0] < enemy2.hitbox[0] < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy2.hitbox[1] < player.hitbox[1] + player.hitbox[3]:
                if player.health > 0:
                    player.health -= 1

                if player.health == 1 and player.lives > 0:
                    player.lives -= 1
                    player.health = 130

                elif player.health == 1 and player.lives == 0:
                    player.alive = False

    def shoot(self):
        self.shoot_cd += 1
        if 200 < self.shoot_cd <= 217 and self.direction == "left":
            self.fire = True
            win.blit(enemy_shoot_left_img[self.shoot_step_index//3], (self.x, self.y))
            if self.shoot_cd == 216:
                e_bullet = EnemyBullet(self.x, self.y)
                ebullets.append(e_bullet)

        elif 200 < self.shoot_cd <= 217 and self.direction == "right":
            self.fire = True
            win.blit(enemy_shoot_right_img[self.shoot_step_index//3], (self.x, self.y))
            if self.shoot_cd == 216:
                e_bullet = EnemyBullet(self.x, self.y)
                ebullets.append(e_bullet)

        if self.shoot_cd == 216:
            self.shoot_cd = 0
            self.fire = False
        if self.shoot_step_index == 18:
            self.shoot_step_index = 0
        self.shoot_step_index += 1


class EnemyBullet:
    def __init__(self, x, y):
        self.x = enemy2.x - 17
        self.y = enemy2.y + 17
        left_or_right = (10, -10)
        self.a = random.choice(left_or_right)


    def draw_enemy_bullet(self):

        if enemy2.name == "chris" and enemies2[0].direction == "left":
            win.blit(enemy_bullet, (enemy2.x - 18, self.y))
        elif enemy2.name == "chris" and enemies2[0].direction == "right":
            win.blit(enemy_bullet, (enemy2.x + 18, self.y))
        elif enemy2.name == "leo" and enemies2[1].direction == "left":
            win.blit(enemy_bullet, (enemy2.x - 18, self.y))
        elif enemy2.name == "leo" and enemies2[1].direction == "right":
            win.blit(enemy_bullet, (enemy2.x - 18, self.y))



    def move_bullet(self):

        self.x += self.a


    def off_screen(self):

        return not (self.x > 0 and self.x < 1000)




class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        if self.direction == 1:
            win.blit(bullet_image, (self.x, self.y))

        if self.direction == -1:
            win.blit(bullet_image_left, (self.x, self.y))

    def move_bullet(self):
        if self.direction == 1:
            self.x += 10
        elif self.direction == -1:
            self.x -= 10

    def off_screen(self):

        return not(self.x > 0 and self.x < 1000)


player = Hero(150, 380)
enemies = []
enemies2 = []
ebullets = []


def draw_game():
    if player.alive:
        win.blit(bg_img, (0, 0))
        player.draw_hero(win)
    pygame.time.delay(25)
    pygame.display.update()
    font = pygame.font.Font('freesansbold.ttf', 26)
    text = font.render("Health: ", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (15, 37)
    win.blit(text, textRect.center)
    font1 = pygame.font.Font('freesansbold.ttf', 26)
    text1 = font1.render('Lives: ' + str(player.lives) + ' | | Kills: ' + str(player.kills) + " | | Level: " +
                         str(player.level), True, (0, 0, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (15,63)
    win.blit(text1, textRect1.center)

    for bullet in player.bullets:
        bullet.draw_bullet()
    for enemy in enemies:
        enemy.draw(win)
        if enemy.off_screen() and enemy.direction == "left":
            enemy.direction = "right"
        elif enemy.off_screen() and enemy.direction == "right":
            enemy.direction = "left"

    for enemy2 in enemies2:
        enemy2.draw(win)
        if enemy2.off_screen() and enemy2.direction == "left":
            enemy2.direction = "right"
        elif enemy2.off_screen() and enemy2.direction == "right":
            enemy2.direction = "left"

    if player.alive is False:
        win.fill((0, 0, 0))
        enemies.clear()
        enemies2.clear()
        font2 = pygame.font.Font('freesansbold.ttf', 40)
        text2 = font2.render("You died! Press R to start again!", True, (255, 255, 255))
        textRect2 = text2.get_rect()
        textRect2.center = (170, 250)
        win.blit(text2, textRect2.center)
        if user_input[pygame.K_r]:
            enemies.clear()
            enemies2.clear()
            player.alive = True
            player.health = 130
            player.lives = 1
            player.kills = 0
            player.level = 1

while run:
    user_input = pygame.key.get_pressed()

    pygame.display.update()

    draw_game()

    player.move_hero(user_input)

    player.jump_motion(user_input)

    player.shoot()

    player.hit()

    player.level_up()



    rand_number = random.randrange(1, 100)
    rand_number2 = random.randrange(40, win_width)
    if rand_number == 1 and player.level == 1:
        enemy = Enemy(rand_number2 - player.x, 380, "right")
        enemies.append(enemy)
    elif rand_number in (2, 3) and player.level == 2:
        enemy = Enemy(rand_number2 - player.x, 380, "left")
        enemies.append(enemy)

    elif rand_number in (4, 5, 6) and player.level == 3 and len(enemies2) <= 2:
        enemy = Enemy(rand_number2 - player.x, 380, "right")
        enemies.append(enemy)
        enemy2 = Enemy2(rand_number2, -30, "left", "chris")
        enemies2.append(enemy2)

    elif rand_number in (4, 5, 6) and player.level == 4 and len(enemies2) <= 4:
        enemy2 = Enemy2(rand_number2 - player.x, -30, "right", "chris")
        enemies2.append(enemy2)
        enemy3 = Enemy2(rand_number2, -30, "left", "leo")
        enemies2.append(enemy3)

    print(enemies)


    for enemy in enemies:
        enemy.move()
        enemy.hit()

    for enemy2 in enemies2:
        enemy2.move()
        enemy2.hit()
        enemy2.spawn()
        enemy2.shoot()

    for enemy2 in enemies2:
        for e_bullet in ebullets:
            e_bullet.draw_enemy_bullet()
            e_bullet.move_bullet()
    for e_bullet in ebullets:
        if e_bullet.off_screen():
            ebullets.remove(e_bullet)


    for e_bullet in ebullets:
         if e_bullet.x == player.x:
             player.health -= 15
             ebullets.remove(e_bullet)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




