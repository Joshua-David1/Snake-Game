import turtle


class Snake(object):
    def __init__(self):
        self.turtle_list = []
        self.starting_x = 0
        self.current_head_value = 0
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for i in range(3):
            new_turt = turtle.Turtle(shape='square')
            new_turt.penup()
            new_turt.color('white')
            new_turt.setx(self.starting_x)
            self.starting_x -= 20
            self.turtle_list.append(new_turt)
        self.starting_x = 0

    def move(self):
        for i in range(len(self.turtle_list)-1, 0, -1):
            x_cor, y_cor = self.turtle_list[i-1].xcor(), self.turtle_list[i-1].ycor()
            self.turtle_list[i].setheading(self.turtle_list[i-1].heading())
            self.turtle_list[i].goto(x_cor, y_cor)
        self.head.forward(20)

    def move_up(self):
        if self.current_head_value != 90 and self.current_head_value != 270:
            self.head.setheading(90)
            self.current_head_value = 90

    def move_down(self):
        if self.current_head_value != 270 and self.current_head_value != 90:
            self.head.setheading(270)
            self.current_head_value = 270

    def move_right(self):
        if self.current_head_value != 0 and self.current_head_value != 180:
            self.head.setheading(0)
            self.current_head_value = 0

    def move_left(self):
        if self.current_head_value != 180 and self.current_head_value != 0:
            self.head.setheading(180)
            self.current_head_value = 180

    def add_snake(self):
        new_turt = turtle.Turtle(shape='square')
        new_turt.penup()
        new_turt.color('white')
        self.turtle_list.append(new_turt)

    def collided(self):
        for i in range(len(self.turtle_list)-1, 0, -1):
            if self.head.distance(self.turtle_list[i]) < 14:
                return True
        return None

    def reset_snake(self):
        for i in self.turtle_list:
            i.goto(10000, 10000)
        self.turtle_list.clear()
        self.create_snake()
        self.current_head_value = 0
        self.head = self.turtle_list[0]
