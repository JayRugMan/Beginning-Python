#!/usr/bin/python3
# y = mx + b


class the_equation():
    def __init__(self):
        self.x = 0
        self.m = 3.9  # slope
        self.b = 7.8
        self.y = 7.8

    def update_x(self):
        while True:
            try:
                self.x = input('enter new x:')
                break
            except TypeError:
                print('not a number')
    
    def get_x(self):
        return (self.y - (self.b)) / self.m
    
    def get_y(self):
        return self.m * self.x + (self.b)
    
    def get_m(self):
        return (self.y - (self.b)) / self.x
    
    def get_b(self):
        return self.y - (self.m * self.x)
