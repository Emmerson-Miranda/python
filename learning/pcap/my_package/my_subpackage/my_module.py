public_value = 1
__private_value = 2


def greetings(name):
    print('Hi', name, 'from', __name__)


def __private_greetings(name):
    print('Hi', name, 'from', __name__)
