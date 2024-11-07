import turtle
import random

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        Polygon.__init__(self, num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        size = self.size
        for _ in range(self.num_levels):
            turtle.penup()
            turtle.forward(size*(1-self.reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-self.reduction_ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            turtle.goto(self.location[0], self.location[1])
            turtle.setheading(self.orientation)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()
            for _ in range(self.num_sides):
                turtle.forward(size)
                turtle.left(360 / self.num_sides)
            size *= self.reduction_ratio

class PolygonArt:
    def __init__(self, unit_of_polygon, art_type):
        self.unit_of_polygon = unit_of_polygon
        self.art_type = art_type

    def run(self):
        if self.art_type in [1, 5]:  # Triangles
            num_sides_options = [3]
        elif self.art_type in [2, 6]:  # Squares
            num_sides_options = [4]
        elif self.art_type in [3, 7]:  # Pentagons
            num_sides_options = [5]
        elif self.art_type in [4, 8, 9]:  # Mixed shapes
            num_sides_options = [3, 4, 5]

        for _ in range(self.unit_of_polygon):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            border_size = random.randint(1, 10)
            num_sides = random.choice(num_sides_options)

            if self.art_type >= 5:  # Use EmbeddedPolygon for art_type 5-9
                num_levels = random.randint(3, 7)
                reduction_ratio = 0.6
                embedded_polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                embedded_polygon.draw()
            else:
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon.draw()

if __name__ == "__main__":
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)

    art_type = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
    num_polygons = 30
    art = PolygonArt(num_polygons, art_type)
    art.run()

    turtle.done()