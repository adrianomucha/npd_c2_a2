'''Contains shape classes and does fun things with them
hapes:
Triangle
Square
Circle

Data Atributes:
shape_type
edge_length
nanme
allies
enemies

Methods:
area perimeter updae_edge_length
add_ally
add_enemy
'''
class Square(object):
    shape_type ='square'

    def __init__(self, edge_length, name,allies,enemies):
        self.edge_length=edge_length
        self.name=name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length **2
    def perimeter(self):
        return self.edge_length * 4
    def update_edge_length(self, new_length):
        self.edge_length = new_length
    def add_ally(self, shape_object):
        self.allies.append(shape_object)
    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

class Triangle(object):

    def __init__(self, edge_length, edge_height, name, allies, enemies):
        self.edge_length = edge_length
        self.edge_height = edge_height
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return 0.5 * self.edge_length * self.edge_height

    def perimeter(self):
        return self.edge_length * 3

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

    def edge_height(self, new_height):
        self.edge_height = new_height

class Circle(object):

    def __init__(self, radius, pi, name, allies, enemies):
        self.radius = radius
        self.pi = pi
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return self.radius * 1
   # def update_radius(self, new_radius):
    #    self.radius.append(shape_object)
    def add_ally(self, shape_object):
        self.allies.append(shape_object)
    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)



if __name__=='__main__':
    square_marty = Square(5, "marty", [], [triangle_tom, circle_andrew])
    print("Area: ",square_marty.area())
    print("Update Edge: ",square_marty.update_edge_length(10))
    print("Area: ",square_marty.area())

if __name__ == '__main__':
    triangle_tom = Triangle(2, 2 , "tom", [], [square_marty])
    print("Area:",triangle_tom.area())
    print("Update Edge: ",triangle_tom.update_edge_length(10))
    print("Area: ",triangle_tom.area())

if __name__ == '__main__':
    circle_andrew = Circle(2,3, "Andrew",[triangle_tom], [square_marty])
    print("Area:", circle_andrew.area())
    #print("Update Edge: ", circle_andrew.update_radius(5))
    print("Area: ", circle_andrew.area())
