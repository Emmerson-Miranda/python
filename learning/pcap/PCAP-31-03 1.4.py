"""
PCAP-31-03 1.4 – Discover host platform properties using the platform module

    functions: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple()
"""

import os
import platform
import sys


def main(name):

    print('Caller : ', name)
    print('Module : ', __name__)

    print('platform.machine              :', platform.machine())  # x86_64
    print('platform.processor            :', platform.processor())  # i386
    print('platform.system               :', platform.system())  # Darwin
    print('platform.version              :', platform.version())  # Darwin Kernel Version 22.4.0:...; root:xnu-8796.101.5...
    print('platform.python_implementation:', platform.python_implementation())  # CPython
    print('platform.python_version_tuple :', platform.python_version_tuple())  # ('3', '9', '16')
    print('platform.uname                :', platform.uname())
    """
    uname_result(
      system='Darwin', 
      node='owl.local', 
      release='22.4.0', 
      version='Darwin Kernel Version 22.4.0: Mon Mar  6 21:00:17 PST 2023; root:xnu-8796.101.5~3/RELEASE_X86_64', 
      machine='x86_64')
    """

    print('os.uname                      :', os.uname())
    """
    os.uname: posix.uname_result(
      sysname='Darwin', 
      nodename='owl.local', 
      release='22.4.0', 
      version='Darwin Kernel Version 22.4.0: Mon Mar  6 21:00:17 PST 2023; root:xnu-8796.101.5~3/RELEASE_X86_64', 
      machine='x86_64')
    """

    print('os.name                       :', os.name)
    """
    os.name: posix
    """

    print('os.urandom                    :', os.urandom(4))

    folder = './os_mkdir'
    if os.path.exists(folder):
        try:
            print('Deleting', folder)
            if os.path.isfile(folder):
                os.remove(folder)
            else:
                os.rmdir(folder)
        except PermissionError as pe:
            print('PermissionError', folder, os.strerror(pe.errno))
            print(pe)

    if not os.path.exists(folder):
        print('Creating folder', folder)
        os.mkdir(folder)

    print('os.listdir:', os.listdir('.'))

    with os.scandir(os.getcwd()) as it:
        scan_list = [entry.name for entry in it if not entry.name.endswith('.py') and entry.is_file()]
        print('os.scandir(os.getcwd())', scan_list)

    print('os.system(mkdir -p ...)     :', os.system(f'mkdir -p {folder}')) # for more power use subprocess
    print('sys.argv[0]                 :', sys.argv[0])
    print('os.path.dirname(sys.argv[0]):', os.path.dirname(sys.argv[0]))
    print('os.getcwd()                 :', os.getcwd())
    print('os.path.abspath(__file__)   :', os.path.abspath(__file__))
    print('os.path.dirname(os.path.abspath(__file__))  :', os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    main(__name__)
