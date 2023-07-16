"""
PCAP-31-03 1.5 – Create and use user-defined modules and packages

    idea and rationale;
    the __pycache__ directory
    the __name__ variable
    public and private variables
    the __init__.py file
    searching for/through modules/packages
    nested packages vs. directory trees

"""
import os
import sys
import my_module
import my_package.my_subpackage.my_module

print('my_module.public_value  :', my_module.public_value)
print('my_package.my_subpackage.my_module.public_value :', my_package.my_subpackage.my_module.public_value)
print("os.listdir('.')         :", os.listdir('.'))

print('IMPORT STATEMENT SEARCH ORDER')
# https://docs.python.org/3/tutorial/modules.html#the-module-search-path
print('sys.builtin_module_names:', sys.builtin_module_names)
print('sys.path (original)     :', sys.path)

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
print("os.getenv('PYTHONPATH') :", os.getenv('PYTHONPATH')) # default search path for module files.

sys.path.insert(0, '../modules')
print('sys.path (after sys.path.insert)  :', sys.path)
