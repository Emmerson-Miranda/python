"""
PCAP-31-02 2.2 – Extend the Python exceptions hierarchy with self-defined exceptions

    self-defined exceptions
    defining and using self-defined exceptions
"""


class CustomException(Exception):

    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(self.message)


def main():
    try:
        i = int('a')
    except Exception as e:
        raise CustomException('custom_value', e) from e  # set e as __cause__


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(type(e), e)
