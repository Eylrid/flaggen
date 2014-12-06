import random

def random_color():
    return '#'+''.join([random.choice('0123456789abcdef') for i in range(6)])

class Flag:
    def __init__(self, **kwargs):
        self.bg = kwargs.get('bg', random_color())

        self.quaterpanels = kwargs.get('quaterpanels', None)
        if self.quaterpanels == None:
            if random.randint(0,4) == 0:
                self.quaterpanels = [Flag() for i in range(random.randint(1,4))]
            else:
                self.quaterpanels = []

        if 'cross' in kwargs:
            self.cross = kwargs['cross']
        elif random.randint(0,4) == 0:
            self.cross = random_color()
        else:
            self.cross = None

