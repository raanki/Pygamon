import pygame
import pytmx
import pyscroll
from player import Player

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Aventure")
        tmx_data = pytmx.util_pygame.load_pygame('assets/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1
        player_position = tmx_data.get_object_by_name("Player")
        self.player = Player(player_position.x, player_position.y)
        self.group = pyscroll.PyscrollGroup(map_layer, default_layer=4)
        self.group.add(self.player)
        self.walls = []
        self.map = 'world'

        self.enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house.rect = pygame.Rect(self.enter_house.x, self.enter_house.y, self.enter_house.width, self.enter_house.height)

        for obj in tmx_data.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


    def switch_house(self):
        tmx_data = pytmx.util_pygame.load_pygame('assets/House.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1
        self.group = pyscroll.PyscrollGroup(map_layer, default_layer=2)
        self.group.add(self.player)
        self.walls = []
        player_position = tmx_data.get_object_by_name("spawn_house")
        self.player.position = ([player_position.x, player_position.y - 20])

        for obj in tmx_data.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        self.enter_house = tmx_data.get_object_by_name("exit_house")
        self.enter_house.rect = pygame.Rect(self.enter_house.x, self.enter_house.y, self.enter_house.width,
                                            self.enter_house.height)

    def switch_world(self):
        tmx_data = pytmx.util_pygame.load_pygame('assets/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1
        self.group = pyscroll.PyscrollGroup(map_layer, default_layer=2)
        self.group.add(self.player)
        self.walls = []

        for obj in tmx_data.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        self.enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house.rect = pygame.Rect(self.enter_house.x, self.enter_house.y, self.enter_house.width,
                                            self.enter_house.height)
        player_position = tmx_data.get_object_by_name("enter_house_exit")
        self.player.position = ([player_position.x, player_position.y + 20])


    def update(self):
        self.group.update()

        if self.map == 'world' and self.player.feet.colliderect(self.enter_house.rect):
            self.switch_house()
            self.map = 'house'

        if self.map == 'house' and self.player.feet.colliderect(self.enter_house.rect):
            self.map = 'world'
            self.switch_world()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
        pygame.quit()

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")