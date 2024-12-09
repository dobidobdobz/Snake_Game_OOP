from turtle import Turtle

# global variable for the amount of movement the snake animation makes
MOVE_DISTANCE = 20

# global variable list of starting positions for snake (each 3 square's of snake body)
STARTING_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]


# creates snake graphics, from square & animates its movement & capabilities
class Snake:

    # initializes class and creates empty snake_list, calls create_snake(), names 1st item in snake_list as variable head
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    # for loop through starting positions tuple to assign start position & calls add_snake()
    def create_snake(self):
        for x in STARTING_POSITIONS:
            self.add_snake(x)

    # creates the snake body part (the squares), setting up new turtle, color, and uses x from for loop in create_snake()
    # to position snake adds it to snake_list
    def add_snake(self, x):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.shape("square")
        new_snake.color("green")
        new_snake.goto(x)
        self.snake_list.append(new_snake)

    # extends the snakes body (adds another square), by calling add_snake(),
    def extend(self):
        # get hold of last item in list position
        self.add_snake(self.snake_list[-1].position())

    # responsible for movement of snake
    def move(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_num - 1].xcor()
            new_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    # turns the snake upward direction
    def up(self):
        # if snake-head is heading down it cannot turn up
        if self.head.heading() != 270:
            # changes direction of snake head (1st square) 90-degree angel
            self.head.setheading(90)

    # turns the snake downward direction
    def down(self):
        # if snake-head is heading up it cannot turn down
        if self.head.heading() != 90:
            # changes direction of snake head (1st square) 270-degree angel
            self.head.setheading(270)

    # turns the snake left
    def left(self):
        # if snake-head is heading right it cannot turn left
        if self.head.heading() != 0:
            # changes direction of snake head (1st square) 180-degree angel
            self.head.setheading(180)

    # turns the snake right
    def right(self):
        # if snake-head is heading left it cannot turn right
        if self.head.heading() != 180:
            # changes direction of snake head (1st square) 0-degree angel
            self.head.setheading(0)

    # resets snake to reposition at center of screen if called
    def reset(self):
        # positions snake in coordinates
        for x in self.snake_list:
            x.goto(1000, 1000)
        # clears list of all items
        self.snake_list.clear()
        # recreates snake(1st 3 initial square's)
        self.create_snake()
        # reassigns 1st square in snake_list as snake self.head
        self.head = self.snake_list[0]

