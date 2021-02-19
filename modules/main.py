import hello_python

import importlib
import runpy

if __name__ == '__main__':
    print('Hello World')

    # https://docs.python.org/3/library/importlib.html
    importlib.reload(hello_python)

    # https://docs.python.org/3/library/runpy.html
    runpy.run_module(mod_name='hello_python')
    runpy.run_path(path_name='hello_python.py')

    exec(open('hello_python.py').read())
