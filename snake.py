import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)
        self.x = pos[0]
        self.y = pos[1]

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
        dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}
        # if self.direction == 'RIGHT':

        self.x += dx[self.direction]
        self.y += dy[self.direction]
        self.x = self.val(self.x)
        self.y = self.val(self.y)
        pos = (self.x,self.y)
        temp_cell = self.game.get_cell(pos)
        if temp_cell.color != consts.back_color and temp_cell.color != consts.fruit_color:
            self.game.kill(self)
        elif temp_cell.color != consts.back_color:
            temp_cell.set_color(self.color)
            self.cells.append(pos)
        else:
            self.game.get_cell(self.cells[0]).set_color(consts.back_color)
            self.cells.pop(0)
            temp_cell.set_color(self.color)
            self.cells.append(pos)



    def handle(self, keys):
        # print(len(keys))
        mark = 0
        for i in range(len(keys)):
            if "i" in self.keys:
                if self.direction == 'LEFT' and keys[i] == 'l' and self.keys['l'] == "RIGHT":
                    pass
                elif self.direction == 'RIGHT' and keys[i] == 'j' and self.keys['j'] == "LEFT":
                    pass
                elif self.direction == 'UP' and keys[i] == 'k' and self.keys['k'] == "DOWN":
                    pass
                elif self.direction == 'DOWN' and keys[i] == 'i' and self.keys['i'] == "UP":
                    pass
                else:
                    if keys[i] == 'l' and self.keys['l'] == "RIGHT":
                        self.direction = 'RIGHT'
                        return
                    elif keys[i] == 'j' and self.keys['j'] == "LEFT":
                        self.direction = 'LEFT'
                        return
                    elif keys[i] == 'k' and self.keys['k'] == "DOWN":
                        self.direction = 'DOWN'
                        return
                    elif keys[i] == 'i' and self.keys["i"] == "UP":
                        self.direction = 'UP'
                        return
                #   print(self.direction)
                mark = 1
                # return mark
            else:
                if self.direction == 'LEFT' and keys[i] == 'd':
                    pass
                elif self.direction == 'RIGHT' and keys[i] == 'a':
                    pass
                elif self.direction == 'UP' and keys[i] == 's':
                    pass
                elif self.direction == 'DOWN' and keys[i] == 'w':
                    pass
                else:
                    if keys[i] == 'd':
                        self.direction = 'RIGHT'
                        return
                    elif keys[i] == 'a':
                        self.direction = 'LEFT'
                        return
                    elif keys[i] == 's':
                        self.direction = 'DOWN'
                        return
                    elif keys[i] == 'w':
                        self.direction = 'UP'
                        return
                # print(self.direction)
                #     mark = 1
                #     return mark
                break

