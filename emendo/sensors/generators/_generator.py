# Imports
from . import GeneratorConfig
from . import BaseGenerator, SplineGenerator

# Implementations
class Generator(BaseGenerator):
    '''
    Generator API for emendo sensor simulation
    '''

    def __init__(self, config: GeneratorConfig):
        self.config = config
    
        self._gen = SplineGenerator(config)


    def position(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `position` method')
    
    def velocity(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `velocity` method')
    
    def acceleration(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `acceleration` method')
    
    def attitude(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `attitude` method')
    
    def magnetic(self, start: float, freq: float, duration: float):
        raise NotImplementedError('Subclasses must implement `magnetic` method')