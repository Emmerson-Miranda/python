"""
PCAP-31-03 2.1 – Handle errors using Python-defined exceptions
    except, except:-except, except:-else:, except (e1, e2)
    the hierarchy of exceptions
    raise, raise ex
    assert
    event classes
    except E as e
    the arg property
"""
from enum import Enum

"""
https://docs.python.org/3/library/exceptions.html

BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""


class UseCaseEnum(Enum):
    Nothing = 0
    ZeroDivision = 1
    Assert = 2
    FileNotFound = 3
    Raise = 4
    InvalidNumber = 5


def error(option):
    try:
        print("-" * 80)
        print('try block option', option)
        if option == UseCaseEnum.ZeroDivision:
            x = 5 / 0
        elif option == UseCaseEnum.Assert:
            assert 1 == 2, 'Assert error value 1 expected 2'
        elif option == UseCaseEnum.FileNotFound:
            f = open('file_not_exist.txt', 'r')
            f.close()
        elif option == UseCaseEnum.Raise:
            raise Exception("This exception is raised by raise statement")
        elif option == UseCaseEnum.InvalidNumber:
            i = int('a')
        else:
            print('option not handle', option)
    except ZeroDivisionError as e:
        print('except ZeroDivisionError block:', e)
    except ArithmeticError as e:
        print('except ArithmeticError block:', e)
    except (AssertionError, FileNotFoundError) as e:
        print('except block:', type(e), e)
        print('\targs:', e.args)
    except Exception as e:
        print('except Exception block:', type(e), e)
    else:
        print('else block')
    finally:
        print('finally block')


if __name__ == '__main__':
    error(UseCaseEnum.Nothing)
    error(UseCaseEnum.ZeroDivision)
    error(UseCaseEnum.Assert)
    error(UseCaseEnum.FileNotFound)
    error(UseCaseEnum.Raise)
    error(UseCaseEnum.InvalidNumber)
