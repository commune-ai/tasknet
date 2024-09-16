import commune as c

class Task(c.Vali):
    def __init__(self, 
                 name = 'adding', 
                 path = './data', 
                 role = 'miner'
                 ):
        self.name = name
        self.path = c.resolve_path(path + '/' + name)
        self.set_role(role)

    def score(self, module):
        assert module.generate(1,2) == 3
        return 1
    
    def generate(self, a, b):
        return a + b
    
    def set_role(self, role):
        if role == 'validator':
            c.Vali(path=self.path, score=self.score)
        elif role == 'miner':
            pass
        else:
            raise ValueError('mode must be either miner or validator')
        self.role = role
        return {'role': role, 'path': self.path}
    

    def __str__(self):
        return self.role
    
    def __repr__(self):
        return f'{self.role}(name={self.name} path={self.path})'
    
    
    def test(self):
        miner = Task(role='miner')
        validator = Task(role='validator')
        assert self.score(miner) == 1
        print('Task test passed')
        return {'miner': miner, 'validator': validator}