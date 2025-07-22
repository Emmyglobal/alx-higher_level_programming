#!/usr/bin/python3
"""Class Base of all other classes in my project
    manage id attributes and avoid duplicating the same code
"""
import json
import csv
import turtle


class Base:
    """Base of all other classes"""
    __nb_objects = 0


    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static methodreturns the JSON string
        representation of list_dictionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("")
            else:
                writer = csv.writer(csvfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height\
                                , obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x,\
                                obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file to a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                instances = []
                for row in reader:
                    row = [int(x) for x in row]
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(id=row[0], width=row[1],\
                                height=row[2], x=row[3], y=row[4])
                    elif cls.__name__ == "Square":
                        obj = cls.create(id=row[0], size=row[1],\
                                x=row[2], y=row[3])
                    instances.append(obj)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangle and Squares"""
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.pensize(2)
        pen.speed(1)

        def draw_shape(pen, x, y, width, height, color):
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(color)
            pen.begin_fill()
            for _ in range(2):
                pen.forward(width)
                pen.right(90)
                pen.forward(height)
                pen.right(90)
            pen.end_fill()

        for rect in list_rectangles:
            draw_shape(pen, rect.x, -rect.y, rect.width, rect.height,\
                     "blue")

        for square in list_squares:
            draw_shape(pen, square.x, -square.y, square.size, square.size, "red")

        turtle.done()
