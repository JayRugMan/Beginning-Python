#!/usr/bin/python3
# y = mx + b


class the_equation():
    def __init__(self):
        ##JH self.x = 0
        self.m = 3.9  # slope
        self.b = 7.8
        self.equation = f'y = {self.m}x + {self.b}'
        ##JH self.y = self.b
        ##JH self.xi = -1 * self.b / self.m  

    ##JH def update_x(self):
    ##JH     while True:
    ##JH         self.x = input('enter new x: ')
    ##JH         try:
    ##JH             self.x = float(self.x)
    ##JH             break
    ##JH         except TypeError:
    ##JH             print('not a number')
    ##JH 
    ##JH def update_y(self):
    ##JH     while True:
    ##JH         self.y = input('enter new y: ')
    ##JH         try:
    ##JH             self.y = float(self.y)
    ##JH             break
    ##JH         except ValueError:
    ##JH             print('not a number')
    
    def solve_x(self):
        while True:
            y = input('Enter y: ')
            try:
                y = float(y)
                return (y - (self.b)) / self.m
            except ValueError:
                print('not a number')
    
    def solve_y(self):
        while True:
            x = input('Enter x: ')
            try:
                x = float(x)
                return self.m * x + (self.b)
            except ValueError:
                print('not a number')

    def calc_b(self):
        while True:
            x,y = input('enter "x,y": ').split(',')
            try:
                x = float(x)
                y = float(y)
                self.b = y - (self.m * x)
                self.equation = f'y = {self.m}x + {self.b}'
                print('Updated b to {}'.format(self.get_b()))
                break
            except ValueError:
                print('not a number')


    def update_b(self):
        while True:
            self.b = input('enter new b: ')
            try:
                self.b = float(self.b)
                self.equation = f'y = {self.m}x + {self.b}'
                break
            except ValueError:
                print('not a number')

    def update_m(self):
        while True:
            self.m = input('enter new m: ')
            try:
                self.m = float(self.m)
                self.equation = f'y = {self.m}x + {self.b}'
                break
            except ValueError:
                print('not a number')
    
    def get_m(self):
        return self.m
    
    def get_b(self):
        return self.b


def display_menu(line):
    the_menu = ''' -- MENU --
 y = mx + b
 {}

 sx - solve for x
 sy - solve for y
 cb - recalculate b (requires x and y input)
 gm - get m
 gb - get b
 um - update m
 ub - update b
 q - quit
 '''.format(line.equation)
    print(the_menu)

the_line = the_equation()

menu_items = ['sx', 'sy', 'cb', 'gm', 'gb', 'um', 'ub', 'q']
output_str = '\n  --- {} = {} --- \n'

while True:
    display_menu(the_line)
    while True:
        selection = input(': ')
        if selection in menu_items:
            break
    if selection == 'sx':
        print(output_str.format('x', the_line.solve_x()))
    elif selection == 'sy':
        print(output_str.format('y', the_line.solve_y()))
    elif selection == 'cb':
        the_line.calc_b()
    elif selection == 'gm':
        print(output_str.format('m', the_line.get_m()))
    elif selection == 'gb':
        print(output_str.format('b', the_line.get_b()))
    elif selection == 'um':
        the_line.update_m()
    elif selection == 'ub':
        the_line.update_b()
    elif selection == 'q':
        break
