"""
PCAP-31-03 1.1 – Import and use modules and packages

    import variants: import, from import, import as, import *
    advanced qualifying for nested modules
    the dir() function
    the sys.path variable
"""
# https://docs.python.org/3.9/library/functions.html#dir

import sys
import my_module
import my_module as my_alias
import learning.pcap.my_package.my_subpackage.my_module as my_alias_pkg
from my_module import greetings
from my_module import greetings as g


def main():
    my_module.greetings('Julio')
    greetings('Cesar')

    my_alias.greetings('Marco')
    g('Antonio')

    my_alias_pkg.greetings('William')

    # https://www.askpython.com/python/examples/find-all-methods-of-class
    print('dir() :', dir())

    print('type(dir(my_alias)) :', type(dir(my_alias)))
    print('dir(my_alias)       :', dir(my_alias))

    print('type(dir(my_alias.__dict__)) :', type(dir(my_alias.__dict__)))
    print('dir(my_alias.__dict__)       :', dir(my_alias.__dict__))


    # https://docs.python.org/3.9/library/sys.html#sys.path  search path for modules
    print('sys.path :', sys.path)


if __name__ == '__main__':
    main()
