# Chapter 10, Batteries Included


## Modules

### Modules Are Programs
> see hello.py

```python
>>> import sys
>>> sys.path.append('<...>/Beginning-Python/book/chap10-Batteries_Included')
>>> import hello
Hello, world!
>>> import hello
>>> hello = reload(hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reload' is not defined
```


## Modules Are Used to Define Things

### Defining a Function in a Module
> see hello2.py

```python
>>> import hello2
>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> hi = hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> hello2.hello()
Hello, world!
```


### Adding Test Code to a Modules
> see hello3.py

```python
>>> import hello3
Hello, world!
>>> hello3.hello()
Hello, world!
```

> see hello4.py
```python
>>> __name__
'__main__'
>>> import hello4
>>> hello4.__name__
'hello4'
>>> hello4.hello()
Hello, world!
>>> hello4.test()
Hello, world!
```

## Make Your Modules Available
### Putting Your Modules in the Right Place
```python
Python 3.6.9 (default, Apr 18 2020, 01:56:04)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys, pprint
>>> pprint.pprint(sys.path)
['',
 '/usr/lib/python36.zip',
 '/usr/lib/python3.6',
 '/usr/lib/python3.6/lib-dynload',
 '<a need-to-know basis>/python3-venv/lib/python3.6/site-packages']  #<< python venv, if not obvious
>>>
...
Python 2.7.17 (default, Apr 15 2020, 17:20:14)
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys, pprint
>>> pprint.pprint(sys.path)
['',
 '/usr/lib/python2.7',
 '/usr/lib/python2.7/plat-x86_64-linux-gnu',
 '/usr/lib/python2.7/lib-tk',
 '/usr/lib/python2.7/lib-old',
 '/usr/lib/python2.7/lib-dynload',
 '/usr/local/lib/python2.7/dist-packages',
 '/usr/lib/python2.7/dist-packages',
 '/usr/lib/python2.7/dist-packages/gtk-2.0',
 '/usr/lib/python2.7/dist-packages/wx-3.0-gtk3']
>>>
```

```bash
[chap10-Batteries_Included] $ cp hello4.py <a need-to-know basis>/python3-venv/lib/python3.6/site-packages/another_hello.py
```
```python
>>> import another_hello
>>> another_hello.hello()
Hello, world!
>>>
```


## Packages
### see constants/__init__.py
```python
>>> import constants
>>> constants.friend
'Jason Hardman'
>>> constants.PI
3.141592653589793
>>>
```


## Exploring Modules
### What's in a Module?
```python
>>> [n for n in dir(copy) if not n.startswith('_')]
['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']
>>> copy.__all__
['Error', 'copy', 'deepcopy']
(python3-venv) me@mycomp:chap10-Batteries_Included$ grep "__all__" /usr/lib/python3.6/copy.py
__all__ = ["Error", "copy", "deepcopy"]
```


### Getting Help with help
```python
>>> help(copy.copy)


Help on function copy in module copy:

copy(x)
    Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
(END)

>>>
>>> print(copy.copy.__doc__)
Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.

>>>
...
(python3-venv) me@mycomp:chap10-Batteries_Included$ head -3 /usr/lib/python3.6/copy.py
"""Generic (shallow and deep) copying operations.

Interface summary:
...
>>> print(copy.__doc__)
Generic (shallow and deep) copying operations.

Interface summary:
...
```


## Documentation
```python
>>> print(range.__doc__)
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
>>>
```


## Use the Source
```python
>>> print(copy.__file__)
/usr/lib/python3.6/copy.py
```


## The Standard Library: A Few Favorites
### sys
```python
>>> pprint.pprint(sys.modules)
{'__main__': <module '__main__' (built-in)>,
 '_codecs': <module '_codecs' (built-in)>,
 '_collections': <module '_collections' (built-in)>,
 '_collections_abc': <module '_collections_abc' from '/usr/lib/python3.6/_collections_abc.py'>,
 '_frozen_importlib': <module '_frozen_importlib' (frozen)>,
 '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>,
 '_functools': <module '_functools' (built-in)>,
 '_heapq': <module '_heapq' (built-in)>,
 '_imp': <module '_imp' (built-in)>,
 '_io': <module 'io' (built-in)>,
 '_locale': <module '_locale' (built-in)>,
 '_operator': <module '_operator' (built-in)>,
 '_signal': <module '_signal' (built-in)>,
 '_sitebuiltins': <module '_sitebuiltins' from '/usr/lib/python3.6/_sitebuiltins.py'>,
 '_sre': <module '_sre' (built-in)>,
 '_stat': <module '_stat' (built-in)>,
 '_sysconfigdata_m_linux_x86_64-linux-gnu': <module '_sysconfigdata_m_linux_x86_64-linux-gnu' from '/usr/lib/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py'>,
 '_thread': <module '_thread' (built-in)>,
 '_warnings': <module '_warnings' (built-in)>,
 '_weakref': <module '_weakref' (built-in)>,
 '_weakrefset': <module '_weakrefset' from '/usr/lib/python3.6/_weakrefset.py'>,
 'abc': <module 'abc' from '/usr/lib/python3.6/abc.py'>,
 'atexit': <module 'atexit' (built-in)>,
 'builtins': <module 'builtins' (built-in)>,
 'codecs': <module 'codecs' from '/usr/lib/python3.6/codecs.py'>,
 'collections': <module 'collections' from '/usr/lib/python3.6/collections/__init__.py'>,
 'collections.abc': <module 'collections.abc' from '/usr/lib/python3.6/collections/abc.py'>,
 'copy': <module 'copy' from '/usr/lib/python3.6/copy.py'>,
 'copyreg': <module 'copyreg' from '/usr/lib/python3.6/copyreg.py'>,
 'encodings': <module 'encodings' from '/usr/lib/python3.6/encodings/__init__.py'>,
 'encodings.aliases': <module 'encodings.aliases' from '/usr/lib/python3.6/encodings/aliases.py'>,
 'encodings.latin_1': <module 'encodings.latin_1' from '/usr/lib/python3.6/encodings/latin_1.py'>,
 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib/python3.6/encodings/utf_8.py'>,
 'enum': <module 'enum' from '/usr/lib/python3.6/enum.py'>,
 'errno': <module 'errno' (built-in)>,
 'functools': <module 'functools' from '/usr/lib/python3.6/functools.py'>,
 'genericpath': <module 'genericpath' from '/usr/lib/python3.6/genericpath.py'>,
 'heapq': <module 'heapq' from '/usr/lib/python3.6/heapq.py'>,
 'io': <module 'io' from '/usr/lib/python3.6/io.py'>,
 'itertools': <module 'itertools' (built-in)>,
 'keyword': <module 'keyword' from '/usr/lib/python3.6/keyword.py'>,
 'marshal': <module 'marshal' (built-in)>,
 'operator': <module 'operator' from '/usr/lib/python3.6/operator.py'>,
 'os': <module 'os' from '/usr/lib/python3.6/os.py'>,
 'os.path': <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>,
 'posix': <module 'posix' (built-in)>,
 'posixpath': <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>,
 'pprint': <module 'pprint' from '/usr/lib/python3.6/pprint.py'>,
 're': <module 're' from '/usr/lib/python3.6/re.py'>,
 'readline': <module 'readline' from '/usr/lib/python3.6/lib-dynload/readline.cpython-36m-x86_64-linux-gnu.so'>,
 'reprlib': <module 'reprlib' from '/usr/lib/python3.6/reprlib.py'>,
 'rlcompleter': <module 'rlcompleter' from '/usr/lib/python3.6/rlcompleter.py'>,
 'site': <module 'site' from '/usr/lib/python3.6/site.py'>,
 'sitecustomize': <module 'sitecustomize' from '/usr/lib/python3.6/sitecustomize.py'>,
 'sre_compile': <module 'sre_compile' from '/usr/lib/python3.6/sre_compile.py'>,
 'sre_constants': <module 'sre_constants' from '/usr/lib/python3.6/sre_constants.py'>,
 'sre_parse': <module 'sre_parse' from '/usr/lib/python3.6/sre_parse.py'>,
 'stat': <module 'stat' from '/usr/lib/python3.6/stat.py'>,
 'sys': <module 'sys' (built-in)>,
 'sysconfig': <module 'sysconfig' from '/usr/lib/python3.6/sysconfig.py'>,
 'types': <module 'types' from '/usr/lib/python3.6/types.py'>,
 'weakref': <module 'weakref' from '/usr/lib/python3.6/weakref.py'>,
 'zipimport': <module 'zipimport' (built-in)>}
>>>
>>> if 'copy' in sys.modules:
...     print('yes')
... else:
...     print('no')
...
yes
```

> see reverseargs.py

```bash
(python3-venv) me@mycomp:chap10-Batteries_Included$ python3 reverseargs.py three two one
one two three
```

### OS
```python
>>> osEnv = os.environ
>>> osEnv['_']
'/home/me/python3-venv/bin/python'
>>> osEnv['SHELL']
'/bin/bash'
>>> osEnv['XDG_CURRENT_DESKTOP']
'X-Cinnamon'
>>>

>>> osSys = os.system
>>> osSys('ls')
Box.py	Line_Characters.py  __pycache__
0
>>> osSys('ls __pycache__')
Box.cpython-36.opt-1.pyc  Line_Characters.cpython-36.opt-1.pyc
0
>>> osSys('pwd')
/home/me/Documents/CodingProjects/python/Beginning-Python/myOwn/jaymatting
0
>>> osSys('grep -i processor /proc/cpuinfo')
processor	: 0
processor	: 1
processor	: 2
processor	: 3
processor	: 4
processor	: 5
processor	: 6
processor	: 7
0
>>> osSys('free -tm')
              total        used        free      shared  buff/cache   available
Mem:           7664        2694         561         835        4409        3836
Swap:          7875         457        7418
Total:        15540        3151        7980
0
>>> osSys('/usr/bin/firefox')  # this opened in the GUI until I killed with ctrl + c
^CExiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.
Exiting due to channel error.
2
>>> import webbrowser
>>> webbrowser.open('https://www.python.org')  # opened this in a tab of current chrome session
True
>>> Opening in existing browser session.
[0623/103137.918723:ERROR:nacl_helper_linux.cc(308)] NaCl helper process running without a sandbox!
Most likely you need to configure your SUID sandbox correctly

>>>
```

### fileinput
> see ./numberlines.py

This will create a backup of the file and prefix every line in the file with "xxx | "
