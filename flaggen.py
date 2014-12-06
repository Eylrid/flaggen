import random

def random_color():
    return '#'+''.join([random.choice('0123456789abcdef') for i in range(6)])

class Flag:
    def __init__(self, **kwargs):
        self.bg = kwargs.get('bg', random_color())

