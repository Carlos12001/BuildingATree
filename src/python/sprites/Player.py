import pygame

from python.sprites.AnimatedState import AnimatedState
from python.sprites.EntitySate import EntityState
from python.sprites.Platform import Platform
from python.sprites.StaticState import StaticState


class Player(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, name: str, px: int, py: int, id: int):
        super(Player, self).__init__()
        self.__screen: pygame.Surface = screen
        self.__states_dict: dict = {}
        self.__current_state: EntityState = None
        self.__dx: int = 0
        self.__dy: int = 0
        self.image: pygame.Surface = None

        self.__name: str = name

        self.point = 0
        self.__id: int = id
        self.__tree: str = ""

        self.__shield = 0
        self.__push =  0
        self.__jumping_more = 0

        self.__jumping: bool = False
        self.__speed: int = 4.9
        self.__floor: int = 2000
        self.__floor_max: int = 0
        self.__floor_min: int = 0
        self.__game_over: bool = False

        # Setter images
        self.__set_dict_images()

        # Set position
        self.image = self.__current_state.get_current_sprite()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

    def get_rect_x(self) -> int:
        return self.rect.x

    def get_rect_y(self) -> int:
        return self.rect.y

    def get_name(self) -> str:
        return self.__name

    def get_tree(self) -> str:
        return self.__tree

    def get_game_over(self) -> bool:
        return self.__game_over

    def get_points(self) -> int:
        return self.point

    def get_power(self) -> str:
        result: str = ""

        if self.__jumping_more != 0 :
            result += "JUMP, "
        if self.__shield != 0 :
            result += "SHIELD, "
        if self.__push != 0:
            result += "PUSH  "
        return result

    def get_shield(self) -> int:
        tmp = self.__shield
        self.__shield = 0
        return tmp

    def get_push(self) -> int:
        tmp = self.__push
        self.__push = 0
        return tmp

    def get_image(self):
        return self.image

    def set_current_state(self, key: str):
        self.__current_state = self.__states_dict[key]

    def set_floor(self, floor: int):
        self.__floor = floor

    def set_rect_x(self, rectx: int) -> None:
        self.rect.x += rectx

    def set_rect_y(self, recty: int) -> None:
        self.rect.y += recty

    def set_tree(self, tree: str) -> None:
        self.__tree = tree

    def set_points(self, point: int) -> None:
        self.point += point

    def __set_dict_images(self):
        if self.__id == 0:
            self.__set_dict_player_0()
        elif self.__id == 1:
            self.__set_dict_player_1()
        elif self.__id == 2:
            self.__set_dict_player_2()
        elif self.__id == 3:
            self.__set_dict_player_3()

    def __set_dict_player_0(self):
        # Images
        from python.screen import SceneGame
        walking_image_right: pygame.Surface = (SceneGame.SceneGame.load_out_img("player1Run.png", (500, 80)))
        walking_image_left: pygame.Surface = (SceneGame.SceneGame.load_out_img("player1RunInv.png", (500, 80)))
        number_of_sprites_walking: int = 6

        self.__walking_right_state = AnimatedState(walking_image_right, number_of_sprites_walking,
                                                   600, "walking_right")

        self.__resting_right_state = StaticState(walking_image_right.subsurface(0, 0,
                                                                                walking_image_right.get_width() / number_of_sprites_walking,
                                                                                walking_image_right.get_height()),
                                                 "resting_right")

        self.__states_dict[self.__walking_right_state.get_name()] = self.__walking_right_state
        self.__states_dict[self.__resting_right_state.get_name()] = self.__resting_right_state

        self.__walking_left_state = AnimatedState(walking_image_left, number_of_sprites_walking,
                                                   600, "walking_left")

        self.__resting_left_state = StaticState(walking_image_left.subsurface(0, 0,
                                                                               walking_image_left.get_width() / number_of_sprites_walking,
                                                                               walking_image_left.get_height()),
                                                 "resting_left")

        self.__states_dict[self.__walking_left_state.get_name()] = self.__walking_left_state
        self.__states_dict[self.__resting_left_state.get_name()] = self.__resting_left_state

        self.set_current_state(self.__resting_right_state.get_name())

    def __set_dict_player_1(self):
        # Images
        from python.screen import SceneGame
        walking_image_right: pygame.Surface = (SceneGame.SceneGame.load_out_img("player2Run.png", (500, 80)))
        walking_image_left: pygame.Surface = (SceneGame.SceneGame.load_out_img("player2RunInv.png", (500, 80)))
        number_of_sprites_walking = 6

        self.__walking_right_state = AnimatedState(walking_image_right, number_of_sprites_walking,
                                                   600, "walking_right")

        self.__resting_right_state = StaticState(walking_image_right.subsurface(0, 0,
                                                                                walking_image_right.get_width() / number_of_sprites_walking,
                                                                                walking_image_right.get_height()),
                                                 "resting_right")

        self.__states_dict[self.__walking_right_state.get_name()] = self.__walking_right_state
        self.__states_dict[self.__resting_right_state.get_name()] = self.__resting_right_state

        self.__walking_left_state = AnimatedState(walking_image_left, number_of_sprites_walking,
                                                  600, "walking_left")

        self.__resting_left_state = StaticState(walking_image_left.subsurface(0, 0,
                                                                              walking_image_left.get_width() / number_of_sprites_walking,
                                                                              walking_image_left.get_height()),
                                                "resting_left")

        self.__states_dict[self.__walking_left_state.get_name()] = self.__walking_left_state
        self.__states_dict[self.__resting_left_state.get_name()] = self.__resting_left_state

        self.set_current_state(self.__resting_right_state.get_name())

    def __set_dict_player_2(self):
        # Images
        from python.screen import SceneGame
        walking_image_right: pygame.Surface = SceneGame.SceneGame.load_out_img("player3Run.png", (500, 80))
        walking_image_left: pygame.Surface = (SceneGame.SceneGame.load_out_img("player3RunInv.png", (500, 80)))
        number_of_sprites_walking = 6

        # Dicts

        self.__walking_right_state = AnimatedState(walking_image_right, number_of_sprites_walking,
                                                   600, "walking_right")

        self.__resting_right_state = StaticState(walking_image_right.subsurface(0, 0,
                                                                                walking_image_right.get_width() / number_of_sprites_walking,
                                                                                walking_image_right.get_height()),
                                                 "resting_right")

        self.__states_dict[self.__walking_right_state.get_name()] = self.__walking_right_state
        self.__states_dict[self.__resting_right_state.get_name()] = self.__resting_right_state

        self.__walking_left_state = AnimatedState(walking_image_left, number_of_sprites_walking,
                                                  600, "walking_left")

        self.__resting_left_state = StaticState(walking_image_left.subsurface(0, 0,
                                                                              walking_image_left.get_width() / number_of_sprites_walking,
                                                                              walking_image_left.get_height()),
                                                "resting_left")

        self.__states_dict[self.__walking_left_state.get_name()] = self.__walking_left_state
        self.__states_dict[self.__resting_left_state.get_name()] = self.__resting_left_state

        self.set_current_state(self.__resting_right_state.get_name())

    def __set_dict_player_3(self):
        # Images
        from python.screen import SceneGame
        walking_image_right: pygame.Surface = SceneGame.SceneGame.load_out_img("player4Run.png", (500, 80))
        walking_image_left: pygame.Surface = (SceneGame.SceneGame.load_out_img("player4RunInv.png", (500, 80)))
        number_of_sprites_walking = 6

        self.__walking_right_state = AnimatedState(walking_image_right, number_of_sprites_walking,
                                                   600, "walking_right")

        self.__resting_right_state = StaticState(walking_image_right.subsurface(0, 0,
                                                                                walking_image_right.get_width() / number_of_sprites_walking,
                                                                                walking_image_right.get_height()),
                                                 "resting_right")

        self.__states_dict[self.__walking_right_state.get_name()] = self.__walking_right_state
        self.__states_dict[self.__resting_right_state.get_name()] = self.__resting_right_state

        self.__walking_left_state = AnimatedState(walking_image_left, number_of_sprites_walking,
                                                  600, "walking_left")

        self.__resting_left_state = StaticState(walking_image_left.subsurface(0, 0,
                                                                              walking_image_left.get_width() / number_of_sprites_walking,
                                                                              walking_image_left.get_height()),
                                                "resting_left")

        self.__states_dict[self.__walking_left_state.get_name()] = self.__walking_left_state
        self.__states_dict[self.__resting_left_state.get_name()] = self.__resting_left_state

        self.set_current_state(self.__resting_right_state.get_name())

    def impulse(self, dx, dy) -> None:
        self.__dx = dx
        self.__dy = dy

    def calculate_gravity(self) -> None:
        self.__dy = self.__dy + 0.35

    def jump(self, jump_force):
        self.impulse(self.__dx, -jump_force)

    def key_down(self, key):
        if self.__id == 0:
            self.__key_down_player_0(key)
        elif self.__id == 1:
            self.__key_down_player_1(key)
        elif self.__id == 2:
            self.__key_down_player_2(key)
        elif self.__id == 3:
            self.__key_down_player_3(key)

    def __key_down_player_0(self, key):
        if self.__shield != 0 :
            self.__shield = 100
        if key == pygame.K_w:
            if not self.__jumping:
                self.jump(9)
                self.__jumping = True
                self.__floor = 2000

            elif self.__jumping_more != 0:
                self.jump(10)
                self.__jumping = True
                self.__jumping_more -= 1
                self.__floor = 2000
        if key == pygame.K_s:
            pass
        if key == pygame.K_d and 1400  > self.rect.x + self.__speed:
            self.__dx = self.__speed
            self.set_current_state(self.__walking_right_state.get_name())
            self.__floor = 2000
        if key == pygame.K_a and 0 < self.rect.x - self.__speed:
            self.__dx = -self.__speed
            # Aqui seria left
            self.set_current_state(self.__walking_left_state.get_name())
            self.__floor = 2000

    def __key_down_player_1(self, key):
        if self.__shield != 0 :
            self.__shield = 100
        if key == pygame.K_UP:
            if not self.__jumping:
                self.jump(9)
                self.__jumping = True
                self.__floor = 2000

            elif self.__jumping_more != 0:
                self.jump(10)
                self.__jumping = True
                self.__jumping_more -= 1
                self.__floor = 2000
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_RIGHT and 1400  > self.rect.x + self.__speed:
            self.__dx = self.__speed
            self.set_current_state(self.__walking_right_state.get_name())
            self.__floor = 2000
        if key == pygame.K_LEFT and 0 < self.rect.x - self.__speed:
            self.__dx = -self.__speed
            # Aqui seria left
            self.set_current_state(self.__walking_left_state.get_name())
            self.__floor = 2000

    def __key_down_player_2(self, key):
        if self.__shield != 0 :
            self.__shield = 100
        if key == pygame.K_i:
            if not self.__jumping:
                self.jump(9)
                self.__jumping = True
                self.__floor = 2000

            elif self.__jumping_more != 0:
                self.jump(10)
                self.__jumping = True
                self.__jumping_more -= 1
                self.__floor = 2000

        if key == pygame.K_k:
            pass
        if key == pygame.K_l  and 1400  > self.rect.x + self.__speed:
            self.__dx = self.__speed
            self.set_current_state(self.__walking_right_state.get_name())
            self.__floor = 2000
        if key == pygame.K_j and 0 < self.rect.x - self.__speed:
            self.__dx = -self.__speed
            # Aqui seria left
            self.set_current_state(self.__walking_left_state.get_name())
            self.__floor = 2000

    def __key_down_player_3(self, key):
        if self.__shield != 0 :
            self.__shield = 100
        if key == pygame.K_g:
            if not self.__jumping:
                self.jump(9)
                self.__jumping = True
                self.__floor = 2000

            elif self.__jumping_more != 0:
                self.jump(10)
                self.__jumping = True
                self.__jumping_more -= 1
                self.__floor = 2000
        if key == pygame.K_b:
            pass
        if key == pygame.K_n  and 1400  > self.rect.x + self.__speed:
            self.__dx = self.__speed
            self.set_current_state(self.__walking_right_state.get_name())
            self.__floor = 2000
        if key == pygame.K_v and 0 < self.rect.x - self.__speed:
            self.__dx = -self.__speed
            # Aqui seria left
            self.set_current_state(self.__walking_left_state.get_name())
            self.__floor = 2000

    def key_up(self, key):
        if self.__id == 0:
            self.__key_up_player_0(key)
        elif self.__id == 1:
            self.__key_up_player_1(key)
        elif self.__id == 2:
            self.__key_up_player_2(key)
        elif self.__id == 3:
            self.__key_up_player_3(key)

    def __key_up_player_0(self, key):
        if key == pygame.K_w:
            pass
        if key == pygame.K_s:
            pass
        if key == pygame.K_d:
            if self.__dx > 0:
                self.__dx = 0
                # Aqui seria left
                self.set_current_state(self.__resting_right_state.get_name())
        if key == pygame.K_a:
            if self.__dx < 0:
                self.__dx = 0
                self.set_current_state(self.__resting_left_state.get_name())

    def __key_up_player_1(self, key):
        if key == pygame.K_UP:
            pass
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_RIGHT:
            if self.__dx > 0:
                self.__dx = 0
                # Aqui seria left
                self.set_current_state(self.__resting_right_state.get_name())
        if key == pygame.K_LEFT:
            if self.__dx < 0:
                self.__dx = 0
                self.set_current_state(self.__resting_left_state.get_name())

    def __key_up_player_2(self, key):
        if key == pygame.K_i:
            pass
        if key == pygame.K_k:
            pass
        if key == pygame.K_l:
            if self.__dx > 0:
                self.__dx = 0
                # Aqui seria left
                self.set_current_state(self.__resting_right_state.get_name())
        if key == pygame.K_j:
            if self.__dx < 0:
                self.__dx = 0
                self.set_current_state(self.__resting_left_state.get_name())

    def __key_up_player_3(self, key):
        if key == pygame.K_g:
            pass
        if key == pygame.K_b:
            pass
        if key == pygame.K_n:
            if self.__dx > 0:
                self.__dx = 0
                # Aqui seria left
                self.set_current_state(self.__resting_right_state.get_name())
        if key == pygame.K_v:
            if self.__dx < 0:
                self.__dx = 0
                self.set_current_state(self.__resting_left_state.get_name())

    def update(self, dt):

        self.calculate_gravity()

        self.rect.x += self.__dx
        self.rect.y += self.__dy

        if self.rect.y + self.rect.height > self.__floor:
            self.rect.y = self.__floor - self.rect.height
            self.__jumping = False
            self.__dy = 0

        if self.__floor_max <= self.rect.x:
            self.__floor = 2000

        if self.__floor_min > self.rect.x:
            self.__floor = 2000



        self.__current_state.update(dt=dt)
        self.image = self.__current_state.get_current_sprite()

    def collision(self, power: str=None, floor: list=None):
        if floor is not None:
            self.set_floor(floor[0])
            self.__floor_min = floor[1]
            self.__floor_max = floor[2]
        if power is not None:

            if power == "jumper":
                self.__jumping_more = 4
            elif power == "shield":
                self.__shield = 150
            elif power == "push":
                self.__push = 300


