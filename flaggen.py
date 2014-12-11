import random

class Flag:
    def __init__(self, **kwargs):
        self.mode = kwargs.get('mode', self.random_mode())
        self.bg = kwargs.get('bg', self.random_color())

        if self.mode == 'plain':
            pass
        elif self.mode == 'quarters':
            self.quarterpanels = kwargs.get('quarterpanels', None)
            if self.quarterpanels == None:
                self.quarterpanels = [Flag() for i in range(4)]
        elif self.mode == 'canton':
            self.canton = kwargs.get('canton', None)
            if not self.canton:
                self.canton = Flag()
        elif self.mode == 'cross':
            self.cross = kwargs.get('cross', self.random_color())
        elif self.mode == 'symbol':
            self.symbol = kwargs.get('symbol', self.random_symbol())
            self.symbol_color = kwargs.get('symbolcolor', self.random_color())
        else:
            raise ValueError('invalid mode')

    def random_color(self):
        colors = ['white', 'black',
                  '#cc0033', #red
                  '#ffcc00', #yellow
                  '#009933', #green
                  '#003399', #blue
                  ]
        return random.choice(colors)

    def random_symbol(self):
        return 'disc'

    def random_mode(self):
        modes = [(5, 'plain'),
                 (1, 'quarters'),
                 (1, 'canton'),
                 (5, 'cross'),
                 (5, 'symbol'),]
        total = sum([i[0] for i in modes])
        choice = random.randint(1, total)
        for weight, mode in modes:
            if choice <= weight:
                return mode
            else:
                choice -= weight

