## gotolibr

A simple library that allows you to use `goto` in Python.

It's implemented using the `commands` argument of `pdb.set_trace`, which was added in Python 3.14.

### Installation

Python 3.14 or higher is required for this library to function properly.

```
$ python3 -m pip install gotolibr
```

### How to use

First, import the library:

```python
from gotolibr import goto
```

Jump to an absolute line number:

```python
goto(1)
```

Jump to a relative line number:

```python
goto(-1, relative=True)
```

### Example

```python
from gotolibr import goto

a = 0
a += 1
print(a)
if a > 5:
    goto(4, relative=True)
else:
    goto(4)

print('Finish')
```
