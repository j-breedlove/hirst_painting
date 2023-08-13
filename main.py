import random
from turtle import Turtle, Screen

# List of predefined RGB colors
color_list = [
    (189, 189, 189),
    (224, 224, 224),
    (173, 173, 173),
    (223, 223, 223),
    (202, 167, 135),
    (144, 52, 97),
    (163, 167, 41),
    (237, 71, 121),
    (237, 83, 60),
    (17, 140, 65),
    (240, 220, 69),
    (225, 119, 162),
    (10, 142, 176),
    (65, 198, 218),
    (23, 169, 129),
    (158, 59, 52),
    (130, 187, 160),
    (109, 41, 85),
    (247, 232, 1),
    (34, 185, 201)
]


def draw_grid(num_rows=10, num_columns=10, circle_radius=20, circle_spacing=50, offset_x=-300, offset_y=-400):
    """
    Draws a grid of circles using the Turtle graphics library.
    
    Parameters:
    - num_rows (int): Number of rows in the grid.
    - num_columns (int): Number of columns in the grid.
    - circle_radius (int): Radius of the circles.
    - circle_spacing (int): Spacing between the circles.
    - offset_x (int): Horizontal offset of the grid.
    - offset_y (int): Vertical offset of the grid.
    """
    artist = Turtle()
    artist.speed("fastest")
    artist.penup()

    for row in range(num_rows):
        for column in range(num_columns):
            x = column * (circle_radius * 2 + circle_spacing) + offset_x
            y = row * (circle_radius * 2 + circle_spacing) + offset_y
            artist.goto(x, y)
            gen_colors = random.choice(color_list)
            artist.pencolor(gen_colors)
            artist.pendown()
            artist.fillcolor(gen_colors)
            artist.begin_fill()
            artist.circle(circle_radius)
            artist.end_fill()
            artist.penup()
    artist.hideturtle()


if __name__ == "__main__":
    Screen().colormode(255)
    draw_grid()
    Screen().exitonclick()
