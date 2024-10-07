import pdb
import os
import inspect

class SilentPdb(pdb.Pdb):
    def __init__(self):
        super().__init__(stdout=open(os.devnull, 'w'))

silent_pdb = SilentPdb()

def goto(line: int, relative: bool = False):
    try:
        original_line = line
        line = int(line + inspect.currentframe().f_back.f_lineno if relative else line)
        assert line > 0
    except (TypeError, ValueError, AssertionError):
        raise ValueError(f'Invalid line number: {original_line}')
    silent_pdb.set_trace(commands=['r', 'n', f'j {line}', 'c'])
