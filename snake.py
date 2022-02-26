from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.co_ordinates = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake body"""
        for index in range(0,3):
            snake_body = Turtle("circle")
            snake_body.penup()
            snake_body.color("pink")
            snake_body.goto(self.co_ordinates[index])
            self.segments.append(snake_body)
    
    def move(self):
        """Moves the snake forward"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        
    def up(self):
        """Moves snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves snake left"""
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        """Moves snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def increase_snake_size(self):
        """Increases size of snake body"""
        new_seg = Turtle("circle")
        new_seg.penup()
        new_seg.color("pink")
        new_seg.goto(self.segments[len(self.segments)-1].xcor(),self.segments[len(self.segments)-1].ycor() )
        self.segments.append(new_seg)
