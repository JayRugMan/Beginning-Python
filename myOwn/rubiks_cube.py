#!/usr/bin/python3
'''This is a digital rubik's cube'''


class The_Cube():
    def __init__(self):
        '''Initializes sides'''
        rgw = {'red': 'south', 'green': 'up', 'white': 'east'}
        rgy = {'red': 'south', 'green': 'up', 'yellow': 'west'}
        rbw = {'red': 'south', 'blue': 'down', 'white': 'east'}
        rby = {'red': 'south', 'blue': 'down', 'yellow': 'west'}
        ogw = {'orange': 'north', 'green': 'up', 'white': 'east'}
        ogy = {'orange': 'north', 'green': 'up', 'yellow': 'west'}
        obw = {'orange': 'north', 'blue': 'down', 'white': 'east'}
        oby = {'orange': 'north', 'blue': 'down', 'yellow': 'west'}
        self.cube = [rgw, rbw, ogw, ogy, rby, rgy, obw, oby]
    def get_face(self, face):
        '''Takes a face, either north, south, east,
        west, up, or down and returns four colors'''
        face_output = []
        for block in self.cube:
            for color, fce in block.items():
                if fce == face:
                    face_output.append(color)
        print('{} {}\n{} {}'.format(*face_output))
    def rotate_face(self, face, direction):
        '''Shifts cube values based on the provided "face" and
        "direction" (either clockwise or counter-clockwise) to
        simulate rotating the face of the cube'''
        
