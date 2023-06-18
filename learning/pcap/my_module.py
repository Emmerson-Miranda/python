public_value = 10
__private_value = 20


def greetings(name):
    print('Hi', name, 'from', __name__)


def __private_greetings(name):
    print('Hi', name, 'from', __name__)
