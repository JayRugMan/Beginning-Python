### Chapter 9, Magic Methods, Properties, and Iterators


# Constructors
>>> f = FooBar()
>>> f.init()
^^ Without Constructors || vv with Constructors
>>> f = FooBar()
>>> class FooBar:
...     def __init__(self):  # vs def init(self):
...         self.somevar = 42
...
>>>
>>> f = FooBar()
>>> f.somevar
42

>>> class FooBar:
...     def __init__(self, value=42):
...         self.somevar = value
...
>>> f = FooBar()
>>> f.somevar
42
>>> f = FooBar('This is a constructor argument')
>>> f.somevar
'This is a constructor argument'


 # Overriding Methods in General, and the Constructor in Particular
 >>> class A:
...     def hello(self):
...         print("Hello, I'm A.")
...
>>> class B(A):
...     pass
...
>>> a = A()
>>> b = B()
>>> a.hello()
Hello, I'm A.
>>> b.hello()
Hello, I'm A.

>>> class B(A):
...     def hello(self):
...         print("Hello, I'm B.")
...
>>> b = B()
>>> b.hello()
Hello, I'm B.

>>> class Bird:
...     def __init__(self):
...         self.hungry = True
...     def eat(self):
...         if self.hungry:
...             print('Aaaaaaaah...')
...             self.hungry = False
...         else:
...             print('No, Thanks!')
...
>>> b = Bird()
>>> b.eat()
Aaaaaaaah...
>>> b.eat()
No, Thanks!
>>>
>>> class SongBird(Bird):
...     def __init__(self):
...         self.sound = 'Squack!'
...     def sing(self):
...         print(self.sound)
...
>>> sb = SongBird()
>>> sb.sing()
Squack!
>>> sb.eat()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in eat
AttributeError: 'SongBird' object has no attribute 'hungry'


# Calling the Unbound Superclass Constructor
>>> class SongBird(Bird):
...     def __init__(self):
...         Bird.__init__(self)  # <<<< Difference
...         self.sound = 'Squawk!'
...     def sing(self):
...         print(self.sound)
...
>>> sb = SongBird()
>>> sb.sing()
Squawk!
>>> sb.eat()
Aaaaaaaah...
>>> sb.eat()
No, Thanks!


# Using the super Function
>>> class Bird:
...     def __init__(self):
...         self.hunger = True
...     def eat(self):
...         if self.hunger:
...             print('Aaaaaah...')
...             self.hunger = False
...         else:
...             print('No, thanks!')
...
>>> class SongBird(Bird):
...     def __init__(self):
...         super().__init__()  # <<<<< Difference
...         self.sound = 'SQUAWK!'
...     def sing(self):
...         print(self.sound)
...
>>> sb = SongBird()
>>> sb.sing()
SQUAWK!
>>> sb.eat()
Aaaaaah...
>>> sb.eat()
No, thanks!


# Item Access
# The Basic Sequence and Mapping Protocol
>>> def checkIndex(key):
...     """
...     Is the given key an acceptable index?
...     To be acceptable, the key should be a non-negative integer. if it
...     is not an integer, a TyperError is raised; if it is negative, an
...     IndexError is raised (since the sequence is of infinite length)
...     """
...     if not isinstance(key, (int)): raise TypeError
...     if key<0: raise IndexError
...
>>>
>>> class ArithmeticSequence:
...     def __init__(self, start=0, step=1):
...         """
...         Initialize the arithmetic sequence.
...         start   - the first value in the sequence
...         step    - the difference between two adjacent values
...         changed - a dictionary of valukes that have been modified by
...                   the user
...         """
...         self.start = start                      # Store the start value
...         self.step = step                        # Store the step value
...         self.changed = {}                       # No items have been modified
...     def __getitem__(self, key):
...         """
...         Get and item from the arithmetic sequence
...         """
...         checkIndex(key)
...         try: return self.changed[key]           # Modified?
...         except KeyError:                        # otherwise...
...             return self.start + key*self.step   # ... calculate the value\
...     def __setitem__(self, key, value):
...         """
...         Change an item in the arithmetic sequence.
...         """
...         checkIndex(key)
...         self.changed[key] = value               # Store the changed value
...
>>> s = ArithmeticSequence(1, 2)
>>> s[4]
9
>>> s[0]
1
>>> s[2]
5
>>> s[3]
7
>>> s[4]
9
>>> s[4] = 2
>>> s[4]
2
>>> s[5]
11
>>> s[22]
45
>>> t = ArithmeticSequence()
>>> t[14]
14
>>> t[14] = 3
>>> for i in range(19):
...     print(t[i])
...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
3
15
16
17
18
>>> for i in range(19):
...     print(s[i])
...
1
3
5
7
2
11
13
15
17
19
21
23
25
27
29
31
33
35
37
>>> del s[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: __delitem__
>>> s["four"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 17, in __getitem__
  File "<stdin>", line 8, in checkIndex
TypeError
>>> s[-42]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 17, in __getitem__
  File "<stdin>", line 9, in checkIndex
IndexError


# Subclassing list, dict, and str
>>> class CounterList(list):
...     def __init__(self, *args):
...         super().__init__(*args)
...         self.counter = 0
...     def __getitem__(self, index):
...         self.counter +=1
...         return super().__getitem__(index)
...
>>> cl = CounterList(range(10))
>>> cl
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> cl.reverse()
>>> cl
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> del cl[3:6]
>>> cl
[9, 8, 7, 3, 2, 1, 0]
>>> cl.counter
0
>>> cl[4] + cl[2]
9
>>> cl.counter
2
>>> cl[0]
9
>>> cl.counter
3


# Properties
>>> class Rectangle:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def setSize(self, size):
...         self.width, self.height = size
...     def getSize(self):
...         return self.width, self.height
...
>>> r = Rectangle()
>>> r.width = 10
>>> r.height = 5
>>> r.getSize()
(10, 5)
>>> r.setSize((150, 100))
>>> r.width
150

# The property Function
>>> __metaclass__ = type
>>> class Rectangle:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def setSize(self, size):
...         self.width, self.height = size
...     def getSize(self):
...         return self.width, self.height
...     size = property(getSize, setSize)  # <<< difference
...
>>> r = Rectangle()
>>> r.width = 10
>>> r.height = 5
>>> r.size
(10, 5)
>>> r.size = 150, 100
>>> r.width
150
>>> class Square:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def blahJack(self, size):  # Set
...         try:
...             self.width, self.height = size
...         except TypeError:
...             print('Error, enter two numbers separated by a comma.')
...     def booJack(self):  # Get
...         return self.width, self.height
...     size = property(booJack, blahJack)
...
>>> s = Square()
>>> s.width = 13
>>> s.height = 29
>>> s.size
(13, 29)
>>> s.size = 149, 10
>>> s.width
149

>>> class Rtangle:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def setSize(self, size):
...         try:
...             self.width, self.height = size
...         except TypeError:
...             print('ERROR - Enter two numbers separated by a comma')
...     def getSize(self):
...         return self.width, self.height
...     size = property(fset=setSize)  # keyword args, in order, are fget, fset, fdel, and doc
...
>>> r = Rtangle()
>>> r.width = 14
>>> r.height = 20
>>> r.size = 2
ERROR - Enter two numbers separated by a comma
>>> r.size = 2, 4
>>> r.size
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: unreadable attribute
>>> r.width
2
>>> r.height
4
>>> class Rtangle:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def setSize(self, size):
...         try:
...             self.width, self.height = size
...         except TypeError:
...             print('ERROR - Enter two numbers separated by a comma')
...     def getSize(self):
...         return self.width, self.height
...     def doc(self):
...         """
...         This is a test class. rectangle width and height.
...         Size is two numbers, separated by commas
...         """
...     size = property(fset=setSize, fget=getSize, doc=doc)  # keyword args, in order, are fget, fset, fdel, and doc
...
>>> r = Rtangle()
>>> r.doc()

        This is a test class. rectangle width and height.
        Size is two numbers, separated by commas



# Static Methods and Class Methods
>>> __metaclass__ = type
>>> class MyClass:
...     def smeth():
...         print('This is a static method')
...     smeth = staticmethod(smeth)
...     def cmeth(cls):
...         print('This is a class method of {}'.format(cls))
...     cmeth = classmethod(cmeth)
...
>>> mc = MyClass()
>>> mc.smeth()
This is a static method
>>> mc.cmeth()

>>> __metaclass__ = type
>>> class MyClass:
...     @staticmethod
...     def smeth():
...         print('This is a static method.')
...     @classmethod
...     def cmeth(cls):
...         print('This is a class method of', cls)
...
>>> MyClass.smeth()
This is a static method.
>>> MyClass.cmeth()
This is a class method of <class '__main__.MyClass'>
>>>


# __getattr__, __setattr__, and Friends
>>> class Rectangle:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def __setattr__(self, name, value):
...         if name == 'size':
...             self.width, self.height = value
...         else:
...             self.__dict__[name] = value
...     def __getattr__(self, name):
...         if name == 'size':
...             return self.width, self.height
...         else:
...             raise AttributeError
...
>>> t = Rectangle()
>>> t
<__main__.Rectangle object at 0x7f100c1a1518>
>>> t.height
0
>>> t.width
0
>>> t.size
(0, 0)
>>> t.size = 5, 6
>>> t.size
(5, 6)
>>> t.width
5
>>> t.height
6
>>> t.fun = 4, 3
>>> t.fun
(4, 3)


# Iterators
>>> class Fibs:
...     def __init__(self):
...         self.a = 0
...         self.b = 1
...     def __next__(self):  # Python 2, this is "def next(self):"
...         self.a, self.b = self.b, self.a+self.b
...         return self.a
...     def __iter__(self):
...         return self
...
>>> fibs = Fibs()
>>> for f in fibs:
...     if f > 1000:
...         print(f)
...         break
...
1597
>>> for f in fibs:
...     if f > 10000:
...         print(f)
...         break
...
10946
>>> for f in fibs:
...     if f < 10000:
...         print(f)
...     else:
...         break
...
>>> for f in fibs:
...     if f > 3:
...         print(f)
...         break
...
46368
>>> fibs = Fibs()
>>> for f in fibs:
...     if f < 100:
...         print(f)
...     else:
...         break
...
1
1
2
3
5
8
13
21
34
55
89
>>> fibs.a = 0
>>> fibs.b = 1
>>> for f in fibs:
...     if f < 100:
...         print(f)
...     else:
...         break
...
1
1
2
3
5
8
13
21
34
55
89
>>> for f in fibs:
...     if f < 100:
...         print(f)
...     else:
...         break
...
>>> fibs.__init__()
>>> for f in fibs:
...     if f < 100:
...         print(f)
...     else:
...         break
...
1
1
2
3
5
8
13
21
34
55
89

>>> it = iter([1, 2, 3])
>>> next(it)  # python2, it's it.next()
1
>>> next(it)
2
>>> next(it)
3


# Making Sequences from Iterators
>>> class TestIterator:
...     value = 0
...     def __next__(self):
...         self.value += 1
...         if self.value > 10: raise StopIteration
...         return self.value
...     def __iter__(self):
...         return self
...
>>> ti = TestIterator()
>>> list(ti)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Generators
>>> nested = [[1,2], [3, 4], [5]]
>>> def flatten(nested):
...     for sublist in nested:
...         for element in sublist:
...             yield element
...
>>> for num in flatten(nested):
...     print(num)
...
1
2
3
4
5
>>> list(flatten(nested))
[1, 2, 3, 4, 5]


# A Recursive Generator
>>> def flatten(nested):
...     try:
...         for sublist in nested:
...             for element in flatten(sublist):
...                yield element
...     except TypeError:
...         yield nested
...
>>> flatten([[[1],2],3,4,[5,[6,7]],8])
<generator object flatten at 0x7f3a85704888>
>>> list(flatten([[[1],2],3,4,[5,[6,7]],8]))
[1, 2, 3, 4, 5, 6, 7, 8]

>>> def flatten(nested):
...     try:
...         # Don't iterate over string-like objects
...         try: nested + ''
...         except TypeError: pass
...         else: raise TypeError
...         for sublist in nested:
...             for element in flatten(sublist):
...                 yield element
...     except TypeError:
...         yield nested
...
>>> list(flatten(['foo', ['bar', ['baz']]]))
['foo', 'bar', 'baz']
>>> list(flatten([['one', [2]], 'three']))
['one', 2, 'three']


# Generators in General
>>> def simple_generator():
...     yield 1
...
>>> simple_generator
<function simple_generator at 0x7efdaa56e378>
>>> simple_generator()
<generator object simple_generator at 0x7efdaa552990>


# Generator Methods
>>> def repeater(value):
...     while True:
...         new = (yield value)
...         if new is not None: value = new
...
>>> r = repeater(42)
>>> next(r)
42
>>> r.send("Hello, World!")
'Hello, World!'
>>> r = repeater(42)
>>> r.send("Hello, World!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator
>>> r.send(None)
42
>>> r.send("Hello, World!")
'Hello, World!'


# Simulating Generators
>>> def flatten(nested):
...     result = []
...     try:
...         # Don't iterate over string-like objects
...         try: nested + ''
...         except TypeError: pass
...         else: raise TypeError
...         for sublist in nested:
...             for element in flatten(sublist):
...                 result.append(element)
...     except TypeError:
...         result.append(nested)
...     return result
...
>>> list(flatten(['foo', ['bar', ['baz']]]))
['foo', 'bar', 'baz']


## The Eight Queens

# Generators and Backtracking
#Pseudocode
for each possibility at level 1:
    for each possibility at level 2:
        ...
            for each possibility at level n:
                is it viable?


# The Problem
#Place 8 queens on a chess board is such a way that no two can capture
#eachother


# State Representation
#Eight queens - one on each row, so tuple state[0] == 3 means queen on
#row 1 is in column 4


# Finding Conflict
>>> def conflict(state, nextX):
...     nextY = len(state)
...     for i in range(nextY):
...         if abs(state[i]-nextX) in (0, nextY-i):
...             return True
...     return False
...
>>>


# The Base Case
>>> def conflict(state, nextX):
...     nextY = len(state)
...     for i in range(nextY):
...         if abs(state[i]-nextX) in (0,nextY-i):
...             return True
...     return False
...
>>> def queens(num, state):
...     if len(state) == num-1:
...         for pos in range(num):
...             if not conflict(state, pos):
...                 yield pos
...
>>> list(queens(4, (1, 3, 0)))
[2]


# The Recursive Case
>>> def conflict(state, nextX):
...     nextY = len(state)
...     for i in range(nextY):
...         if abs(state[i]-nextX) in (0,nextY-i):
...             return True
...     return False
...
>>>
>>> def queens(num=8, state=()):
...     for pos in range(num):
...         if not conflict(state, pos):
...             if len(state) == num-1:
...                 yield (pos,)
...             else:
...                 for result in queens(num, state + (pos,)):
...                     yield (pos,) + result
...
>>> list(queens(4))
[(1, 3, 0, 2), (2, 0, 3, 1)]
>>> list(queens(5))
[(0, 2, 4, 1, 3), (0, 3, 1, 4, 2), (1, 3, 0, 2, 4), (1, 4, 2, 0, 3), (2, 0, 3, 1, 4), (2, 4, 1, 3, 0), (3, 0, 2, 4, 1), (3, 1, 4, 2, 0), (4, 1, 3, 0, 2), (4, 2, 0, 3, 1)]
>>> list(queens(6))
[(1, 3, 5, 0, 2, 4), (2, 5, 1, 4, 0, 3), (3, 0, 4, 1, 5, 2), (4, 2, 0, 5, 3, 1)]
>>> list(queens(7))
[(0, 2, 4, 6, 1, 3, 5), (0, 3, 6, 2, 5, 1, 4), (0, 4, 1, 5, 2, 6, 3), (0, 5, 3, 1, 6, 4, 2), (1, 3, 0, 6, 4, 2, 5), (1, 3, 5, 0, 2, 4, 6), (1, 4, 0, 3, 6, 2, 5), (1, 4, 2, 0, 6, 3, 5), (1, 4, 6, 3, 0, 2, 5), (1, 5, 2, 6, 3, 0, 4), (1, 6, 4, 2, 0, 5, 3), (2, 0, 5, 1, 4, 6, 3), (2, 0, 5, 3, 1, 6, 4), (2, 4, 6, 1, 3, 5, 0), (2, 5, 1, 4, 0, 3, 6), (2, 6, 1, 3, 5, 0, 4), (2, 6, 3, 0, 4, 1, 5), (3, 0, 2, 5, 1, 6, 4), (3, 0, 4, 1, 5, 2, 6), (3, 1, 6, 4, 2, 0, 5), (3, 5, 0, 2, 4, 6, 1), (3, 6, 2, 5, 1, 4, 0), (3, 6, 4, 1, 5, 0, 2), (4, 0, 3, 6, 2, 5, 1), (4, 0, 5, 3, 1, 6, 2), (4, 1, 5, 2, 6, 3, 0), (4, 2, 0, 5, 3, 1, 6), (4, 6, 1, 3, 5, 0, 2), (4, 6, 1, 5, 2, 0, 3), (5, 0, 2, 4, 6, 1, 3), (5, 1, 4, 0, 3, 6, 2), (5, 2, 0, 3, 6, 4, 1), (5, 2, 4, 6, 0, 3, 1), (5, 2, 6, 3, 0, 4, 1), (5, 3, 1, 6, 4, 2, 0), (5, 3, 6, 0, 2, 4, 1), (6, 1, 3, 5, 0, 2, 4), (6, 2, 5, 1, 4, 0, 3), (6, 3, 0, 4, 1, 5, 2), (6, 4, 2, 0, 5, 3, 1)]
>>> list(queens(8))
[(0, 4, 7, 5, 2, 6, 1, 3), (0, 5, 7, 2, 6, 3, 1, 4), (0, 6, 3, 5, 7, 1, 4, 2), (0, 6, 4, 7, 1, 3, 5, 2), (1, 3, 5, 7, 2, 0, 6, 4), (1, 4, 6, 0, 2, 7, 5, 3), (1, 4, 6, 3, 0, 7, 5, 2), (1, 5, 0, 6, 3, 7, 2, 4), (1, 5, 7, 2, 0, 3, 6, 4), (1, 6, 2, 5, 7, 4, 0, 3), (1, 6, 4, 7, 0, 3, 5, 2), (1, 7, 5, 0, 2, 4, 6, 3), (2, 0, 6, 4, 7, 1, 3, 5), (2, 4, 1, 7, 0, 6, 3, 5), (2, 4, 1, 7, 5, 3, 6, 0), (2, 4, 6, 0, 3, 1, 7, 5), (2, 4, 7, 3, 0, 6, 1, 5), (2, 5, 1, 4, 7, 0, 6, 3), (2, 5, 1, 6, 0, 3, 7, 4), (2, 5, 1, 6, 4, 0, 7, 3), (2, 5, 3, 0, 7, 4, 6, 1), (2, 5, 3, 1, 7, 4, 6, 0), (2, 5, 7, 0, 3, 6, 4, 1), (2, 5, 7, 0, 4, 6, 1, 3), (2, 5, 7, 1, 3, 0, 6, 4), (2, 6, 1, 7, 4, 0, 3, 5), (2, 6, 1, 7, 5, 3, 0, 4), (2, 7, 3, 6, 0, 5, 1, 4), (3, 0, 4, 7, 1, 6, 2, 5), (3, 0, 4, 7, 5, 2, 6, 1), (3, 1, 4, 7, 5, 0, 2, 6), (3, 1, 6, 2, 5, 7, 0, 4), (3, 1, 6, 2, 5, 7, 4, 0), (3, 1, 6, 4, 0, 7, 5, 2), (3, 1, 7, 4, 6, 0, 2, 5), (3, 1, 7, 5, 0, 2, 4, 6), (3, 5, 0, 4, 1, 7, 2, 6), (3, 5, 7, 1, 6, 0, 2, 4), (3, 5, 7, 2, 0, 6, 4, 1), (3, 6, 0, 7, 4, 1, 5, 2), (3, 6, 2, 7, 1, 4, 0, 5), (3, 6, 4, 1, 5, 0, 2, 7), (3, 6, 4, 2, 0, 5, 7, 1), (3, 7, 0, 2, 5, 1, 6, 4), (3, 7, 0, 4, 6, 1, 5, 2), (3, 7, 4, 2, 0, 6, 1, 5), (4, 0, 3, 5, 7, 1, 6, 2), (4, 0, 7, 3, 1, 6, 2, 5), (4, 0, 7, 5, 2, 6, 1, 3), (4, 1, 3, 5, 7, 2, 0, 6), (4, 1, 3, 6, 2, 7, 5, 0), (4, 1, 5, 0, 6, 3, 7, 2), (4, 1, 7, 0, 3, 6, 2, 5), (4, 2, 0, 5, 7, 1, 3, 6), (4, 2, 0, 6, 1, 7, 5, 3), (4, 2, 7, 3, 6, 0, 5, 1), (4, 6, 0, 2, 7, 5, 3, 1), (4, 6, 0, 3, 1, 7, 5, 2), (4, 6, 1, 3, 7, 0, 2, 5), (4, 6, 1, 5, 2, 0, 3, 7), (4, 6, 1, 5, 2, 0, 7, 3), (4, 6, 3, 0, 2, 7, 5, 1), (4, 7, 3, 0, 2, 5, 1, 6), (4, 7, 3, 0, 6, 1, 5, 2), (5, 0, 4, 1, 7, 2, 6, 3), (5, 1, 6, 0, 2, 4, 7, 3), (5, 1, 6, 0, 3, 7, 4, 2), (5, 2, 0, 6, 4, 7, 1, 3), (5, 2, 0, 7, 3, 1, 6, 4), (5, 2, 0, 7, 4, 1, 3, 6), (5, 2, 4, 6, 0, 3, 1, 7), (5, 2, 4, 7, 0, 3, 1, 6), (5, 2, 6, 1, 3, 7, 0, 4), (5, 2, 6, 1, 7, 4, 0, 3), (5, 2, 6, 3, 0, 7, 1, 4), (5, 3, 0, 4, 7, 1, 6, 2), (5, 3, 1, 7, 4, 6, 0, 2), (5, 3, 6, 0, 2, 4, 1, 7), (5, 3, 6, 0, 7, 1, 4, 2), (5, 7, 1, 3, 0, 6, 4, 2), (6, 0, 2, 7, 5, 3, 1, 4), (6, 1, 3, 0, 7, 4, 2, 5), (6, 1, 5, 2, 0, 3, 7, 4), (6, 2, 0, 5, 7, 4, 1, 3), (6, 2, 7, 1, 4, 0, 5, 3), (6, 3, 1, 4, 7, 0, 2, 5), (6, 3, 1, 7, 5, 0, 2, 4), (6, 4, 2, 0, 5, 7, 1, 3), (7, 1, 3, 0, 6, 4, 2, 5), (7, 1, 4, 2, 0, 6, 3, 5), (7, 2, 0, 5, 1, 4, 6, 3), (7, 3, 0, 2, 5, 1, 6, 4)]
>>> len(list(queens(8)))
92


# Wrapping It Up
>>> def conflict(state, nextX):
...     nextY = len(state)
...     for i in range(nextY):
...         if abs(state[i]-nextX) in (0, nextY-i):
...             return True
...     return False
...
>>>
>>> def queens(num=8, state=()):
...     for pos in range(num):
...         if not conflict(state, pos):
...             if len(state) == num-1:
...                 yield (pos,)
...             else:
...                 for result in queens(num, state + (pos,)):
...                     yield (pos,) + result
...
>>>
>>> def prettyprint(solution):
...     def line(pos, length=len(solution)):
...         return '{}{}{}'.format('[ ]'*pos, ' Q ', '[ ]'*(length-pos-1))
...     for pos in solution:
...         print(line(pos))
...
>>>
>>> def allTheBoards(num):
...     width = num * 3
...     bCount = 0
...     for cBoard in queens(num):
...         bCount += 1
...         bCount_fmtd = ' {} '.format(bCount)  # format me some bCount
...         print('\n{0:=^{1}}'.format(bCount_fmtd, width))
...         prettyprint(cBoard)
...     total = '{} total boards'.format(bCount)
...     print('\n{0:^{1}}\n'.format(total, width))
...
>>> allTheBoards(1)

 1
 Q

1 total boards

>>> allTheBoards(2)

0 total boards

>>> allTheBoards(3)

0 total boards

>>> allTheBoards(4)

==== 1 =====
[ ] Q [ ][ ]
[ ][ ][ ] Q
 Q [ ][ ][ ]
[ ][ ] Q [ ]

==== 2 =====
[ ][ ] Q [ ]
 Q [ ][ ][ ]
[ ][ ][ ] Q
[ ] Q [ ][ ]

2 total boards

>>> allTheBoards(5)

====== 1 ======
 Q [ ][ ][ ][ ]
[ ][ ] Q [ ][ ]
[ ][ ][ ][ ] Q
[ ] Q [ ][ ][ ]
[ ][ ][ ] Q [ ]

====== 2 ======
 Q [ ][ ][ ][ ]
[ ][ ][ ] Q [ ]
[ ] Q [ ][ ][ ]
[ ][ ][ ][ ] Q
[ ][ ] Q [ ][ ]

====== 3 ======
[ ] Q [ ][ ][ ]
[ ][ ][ ] Q [ ]
 Q [ ][ ][ ][ ]
[ ][ ] Q [ ][ ]
[ ][ ][ ][ ] Q

====== 4 ======
[ ] Q [ ][ ][ ]
[ ][ ][ ][ ] Q
[ ][ ] Q [ ][ ]
 Q [ ][ ][ ][ ]
[ ][ ][ ] Q [ ]

====== 5 ======
[ ][ ] Q [ ][ ]
 Q [ ][ ][ ][ ]
[ ][ ][ ] Q [ ]
[ ] Q [ ][ ][ ]
[ ][ ][ ][ ] Q

====== 6 ======
[ ][ ] Q [ ][ ]
[ ][ ][ ][ ] Q
[ ] Q [ ][ ][ ]
[ ][ ][ ] Q [ ]
 Q [ ][ ][ ][ ]

====== 7 ======
[ ][ ][ ] Q [ ]
 Q [ ][ ][ ][ ]
[ ][ ] Q [ ][ ]
[ ][ ][ ][ ] Q
[ ] Q [ ][ ][ ]

====== 8 ======
[ ][ ][ ] Q [ ]
[ ] Q [ ][ ][ ]
[ ][ ][ ][ ] Q
[ ][ ] Q [ ][ ]
 Q [ ][ ][ ][ ]

====== 9 ======
[ ][ ][ ][ ] Q
[ ] Q [ ][ ][ ]
[ ][ ][ ] Q [ ]
 Q [ ][ ][ ][ ]
[ ][ ] Q [ ][ ]

===== 10 ======
[ ][ ][ ][ ] Q
[ ][ ] Q [ ][ ]
 Q [ ][ ][ ][ ]
[ ][ ][ ] Q [ ]
[ ] Q [ ][ ][ ]

10 total boards

>>> allTheBoards(6)

======= 1 ========
[ ] Q [ ][ ][ ][ ]
[ ][ ][ ] Q [ ][ ]
[ ][ ][ ][ ][ ] Q
 Q [ ][ ][ ][ ][ ]
[ ][ ] Q [ ][ ][ ]
[ ][ ][ ][ ] Q [ ]

======= 2 ========width
[ ][ ] Q [ ][ ][ ]
[ ][ ][ ][ ][ ] Q
[ ] Q [ ][ ][ ][ ]
[ ][ ][ ][ ] Q [ ]
 Q [ ][ ][ ][ ][ ]
[ ][ ][ ] Q [ ][ ]

======= 3 ========
[ ][ ][ ] Q [ ][ ]
 Q [ ][ ][ ][ ][ ]
[ ][ ][ ][ ] Q [ ]
[ ] Q [ ][ ][ ][ ]
[ ][ ][ ][ ][ ] Q
[ ][ ] Q [ ][ ][ ]

======= 4 ========
[ ][ ][ ][ ] Q [ ]
[ ][ ] Q [ ][ ][ ]
 Q [ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ] Q
[ ][ ][ ] Q [ ][ ]
[ ] Q [ ][ ][ ][ ]

  4 total boards
>>> allTheBoards(8)
>>> def drawRectangle(width=2, height=2):
...     if width <= 0 or height <= 0:
...         raise Exception(TypeError('Width and height must be 1 or more'))
...     TLCorner = '┏'
...     TobBot = '━'
...     TRCorner = '┓'
...     Sides = '┃'
...     BLCorner = '┗'
...     BRCorner = '┛'
...     height = height + 1
...     width = (width * 2) - 1
...     grid = '{}{}{}'
...     for line in range(height):
...         if line == 0:
...             print(grid.format(TLCorner, TobBot*width, TRCorner))
...         elif line == (height - 1):
...             print(grid.format(BLCorner, TobBot*width, BRCorner))
...         else:
...             print(grid.format(Sides, ' '*width, Sides))
...
>>>

  ========== 1 ===========
   Q [ ][ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ] Q [ ][ ][ ]
  [ ][ ][ ][ ][ ][ ][ ] Q
  [ ][ ][ ][ ][ ] Q [ ][ ]
  [ ][ ] Q [ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ][ ] Q [ ]
  [ ] Q [ ][ ][ ][ ][ ][ ]
  [ ][ ][ ] Q [ ][ ][ ][ ]

  ========== 2 ===========
   Q [ ][ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ] Q [ ][ ]
  [ ][ ][ ][ ][ ][ ][ ] Q
  [ ][ ] Q [ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ][ ] Q [ ]
  [ ][ ][ ] Q [ ][ ][ ][ ]
  [ ] Q [ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ] Q [ ][ ][ ]

  ========== 3 ===========
   Q [ ][ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ][ ] Q [ ]
  [ ][ ][ ] Q [ ][ ][ ][ ]
  [ ][ ][ ][ ][ ] Q [ ][ ]
  [ ][ ][ ][ ][ ][ ][ ] Q
  [ ] Q [ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ] Q [ ][ ][ ]
  [ ][ ] Q [ ][ ][ ][ ][ ]

  ========== 4 ===========
   Q [ ][ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ][ ] Q [ ]
  [ ][ ][ ][ ] Q [ ][ ][ ]
  [ ][ ][ ][ ][ ][ ][ ] Q
  [ ] Q [ ][ ][ ][ ][ ][ ]
  [ ][ ][ ] Q [ ][ ][ ][ ]
  [ ][ ][ ][ ][ ] Q [ ][ ]
  [ ][ ] Q [ ][ ][ ][ ][ ]

...

========== 91 ==========
[ ][ ][ ][ ][ ][ ][ ] Q
[ ][ ] Q [ ][ ][ ][ ][ ]
 Q [ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ] Q [ ][ ]
[ ] Q [ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ] Q [ ][ ][ ]
[ ][ ][ ][ ][ ][ ] Q [ ]
[ ][ ][ ] Q [ ][ ][ ][ ]

========== 92 ==========
[ ][ ][ ][ ][ ][ ][ ] Q
[ ][ ][ ] Q [ ][ ][ ][ ]
 Q [ ][ ][ ][ ][ ][ ][ ]
[ ][ ] Q [ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ] Q [ ][ ]
[ ] Q [ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ] Q [ ]
[ ][ ][ ][ ] Q [ ][ ][ ]

    92 total boards

>>>

>>> import random
>>> prettyprint(random.choice(list(queens(8))))
  [ ] Q [ ][ ][ ][ ][ ][ ]
  [ ][ ][ ][ ][ ][ ] Q [ ]
  [ ][ ][ ][ ] Q [ ][ ][ ]
  [ ][ ][ ][ ][ ][ ][ ] Q
   Q [ ][ ][ ][ ][ ][ ][ ]
  [ ][ ][ ] Q [ ][ ][ ][ ]
  [ ][ ][ ][ ][ ] Q [ ][ ]
  [ ][ ] Q [ ][ ][ ][ ][ ]



# Bonus
>>> def drawRectangle(width=2, height=2):
...     if width <= 0 or height <= 0:
...         raise Exception(TypeError('Width and height must be 1 or more'))
...     TLCorner = '┏'
...     TobBot = '━'
...     TRCorner = '┓'
...     Sides = '┃'
...     BLCorner = '┗'
...     BRCorner = '┛'
...     height = height + 1
...     width = (width * 2) - 1
...     grid = '{}{}{}'
...     for line in range(height):
...         if line == 0:
...             print(grid.format(TLCorner, TobBot*width, TRCorner))
...         elif line == (height - 1):
...             print(grid.format(BLCorner, TobBot*width, BRCorner))
...         else:
...             print(grid.format(Sides, ' '*width, Sides))
...
>>> class Rtangle:
...     def __init__(self):
...         self.width = 0
...         self.height = 0
...     def setSize(self, size):
...         try:
...             self.width, self.height = size
...         except TypeError:
...             print('ERROR - Enter two numbers separated by a comma')
...     def getSize(self):
...         return self.width, self.height
...     def doc(self):
...         print("""
...         This is a test class. rectangle width and height.
...         Size is two numbers, separated by commas
...         """)
...     size = property(fset=setSize, fget=getSize, doc=doc)  # keyword args, in order, are fget, fset, fdel, and doc
...
>>> r = Rtangle()
>>> r.width = 3
>>> r.height = 3
>>> drawRectangle(*r.size)
┏━━━━━┓
┃     ┃
┃     ┃
┗━━━━━┛
>>> r.size = 20, 10
>>> drawRectangle(*r.size)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                       ┃
┃                                       ┃
┃                                       ┃
┃                                       ┃
┃                                       ┃
┃                                       ┃
┃                                       ┃
┃                                       ┃
┃                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
>>> r.doc()

        This is a test class. rectangle width and height.
        Size is two numbers, separated by commas

>>>
