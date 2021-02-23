import demo

import importlib
import runpy


def main():
    message = 'Hello Python3!'
    print(message)
    message = demo.process_data(message)
    print(message)

    # https://docs.python.org/3/library/importlib.html
    importlib.reload(demo)

    # https://docs.python.org/3/library/runpy.html
    runpy.run_module(mod_name='demo')
    runpy.run_path(path_name='demo.py')

    exec(open('demo.py').read())


if __name__ == '__main__':
    main()
    
