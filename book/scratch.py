def checkIndex(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer. if it
    is not an integer, a TyperError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length)
    """
    if not isinstance(key, (int)): raise TypeError
    if key<0: raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start   - the first value in the sequence
        step    - the difference between two adjacent values
        changed - a dictionary of valukes that have been modified by
                  the user
        """
        self.start = start                      # Store the start value
        self.step = step                        # Store the step value
        self.changed = {}                       # No items have been modified
    def __getitem__(self, key):
        """
        Get and item from the arithmetic sequence
        """
        checkIndex(key)
        try: return self.changed[key]           # Modified?
        except KeyError:                        # otherwise...
            return self.start + key*self.step   # ... calculate the value\
    def __setitem__(self, key, value):
        """
        Change an item in the arithmetic sequence.
        """
        checkIndex(key)
        self.changed[key] = value               # Store the changed value


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False


def queens(num, state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


def conflict(state, nextX):  # (2,0,3,1,4), 6
    nextY = len(state)  # 5
    for i in range(nextY):  # i = 2    (0,1,2,3,4)
        if abs(state[i]-nextX) in (0, nextY-i):  # |3-6|=3 in (0, 5-2=3)
            return True
    return False


def queens(num, state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


            ==============
            [ ] Q [ ][ ]
            [ ][ ][ ] Q
             Q [ ][ ][ ]
            [ ][ ] Q [ ]

            ==============
            [ ][ ] Q [ ]
             Q [ ][ ][ ]
            [ ][ ][ ] Q
            [ ] Q [ ][ ]


def conflict_show(state, nextX):
    print(' Entering conflict test')
    print(' state = {}   nextX = {}'.format(state, nextX))
    nextY = len(state)  # 5
    print(" nextY (lenght of state) = {}".format(nextY))
    for i in range(nextY):  # i = 2    (0,1,2,3,4)
        print("  i = {}".format(i))
        if abs(state[i]-nextX) in (0,nextY-i):  # |3-6|=3 in (0, 5-2=3)
            print('   state[i] = {}\n   nextY = {}'.format(state[i], nextY))
            print("   abs(state[i]-nextX) = {}".format(abs(state[i]-nextX)))
            print('   nextY-i = {}'.format((nextY-i)))
            print(' Conflicts positive')
            return True
    print(' Conflicts negative')
    return False


def queens_show(num, state):
    if len(state) == num-1:  # 0 ==
        for pos in range(num):
            print('pos = {}'.format(pos))
            if not conflict_show(state, pos):
                yield pos


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '{}{}{}'.format('[ ]'*pos, ' Q ', '[ ]'*(length-pos-1))
    for pos in solution:
        print(line(pos))


def allTheBoards(num):
    width = num * 3
    bCount = 0
    for cBoard in queens(num):
        bCount += 1
        bCount_fmtd = ' {} '.format(bCount)  # format me some bCount
        print('\n{0:=^{1}}'.format(bCount_fmtd, width))
        prettyprint(cBoard)
    total = '{} total boards'.format(bCount)
    print('\n{0:^{1}}\n'.format(total, width))


GCNTR = {'A': 0, 'B': 0, 'C': 0}
def testme(total=2, nums=(), level=0):
    lcntr = {'a': 0, 'b': 0, 'c': 0}
    for num in range(total):
        lcntr['a'] += 1
        GCNTR['A'] += 1
        print('{2}a-{a} b-{b} c-{c}    A-{A} B-{B} C-{C}'
              ' num {0} nums {1}'.format(num, nums, ' '*level,
                                         **lcntr, **GCNTR))
        if len(nums) == total-1:
            lcntr['b'] += 1
            GCNTR['B'] += 1
            print('{2}a-{a} b-{b} c-{c}    A-{A} B-{B} C-{C}'
                  ' num {0} nums {1}'.format(num, nums, ' '*level,
                                             **lcntr, **GCNTR))
            print('{0}({1},) - b'.format(' '*level, num))
            yield (num,)
        else:
            for result in testme(total, nums + (num,), level+1):
                lcntr['c'] += 1
                GCNTR['C'] += 1
                print('{3}a-{a} b-{b} c-{c}    A-{A} B-{B} C-{C}'
                      ' num {0} nums {1} result {2}'.format(
                                                 num, nums, result, ' '*level,
                                                 **lcntr, **GCNTR))
                print('{0}{1} - c'.format(' '*level, (num,)+result))
                yield (num,) + result

list(testme())


def guess_pin(pin=(1, 2, 3, 4)):
    def bf_pin(numCount=1, total=10, gess=()):
        for num in range(total):
            if len(gess) == numCount-1:
                yield (num,)
            else:
                for result in bf_pin(numCount, total, gess + (num,)):
                    yield (num,) + result
    for guess in bf_pin(numCount=len(pin)):
        if guess == pin:
            print('Pin is {}'.format(guess))
            break


myPin = (3, 2, 1, 1, 4, 5)
guess_pin(myPin)
Pin is (3, 2, 1, 1, 4, 5)


# see https://unicode-table.com/en/#box-drawing
boxTobBot = '━'
print(boxTobBot)
boxTRCorner = '┓'
boxTLCorner = '┏'
boxBRCorner = '┛'
boxBLCorner = '┗'
boxSides = '┃'
print('{0}{1}{2}\n{3}{4}{3}\n{5}{1}{6}'.format(boxTLCorner, boxTobBot*3,
                                               boxTRCorner, boxSides, ' '*3,
                                               boxBLCorner, boxBRCorner))


def drawRectangle(width=2, height=2):
    if width <= 0 or height <= 0:
        raise Exception(TypeError('Width and height must be 1 or more'))
    TLCorner = '┏'
    TobBot = '━'
    TRCorner = '┓'
    Sides = '┃'
    BLCorner = '┗'
    BRCorner = '┛'
    height = height + 1
    width = (width * 2) - 1
    grid = '{}{}{}'
    for line in range(height):
        if line == 0:
            print(grid.format(TLCorner, TobBot*width, TRCorner))
        elif line == (height - 1):
            print(grid.format(BLCorner, TobBot*width, BRCorner))
        else:
            print(grid.format(Sides, ' '*width, Sides))


class Rtangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        try:
            self.width, self.height = size
        except TypeError:
            print('ERROR - Enter two numbers separated by a comma')
    def getSize(self):
        return self.width, self.height
    def doc(self):
        print("""
        This is a test class. rectangle width and height.
        Size is two numbers, separated by commas
        """)
    size = property(fset=setSize, fget=getSize, doc=doc)  # keyword args, in order, are fget, fset, fdel, and doc
