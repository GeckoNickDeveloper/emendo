# Imports
from . import GeneratorConfig

# Implementations
class BaseGenerator():
    '''
    Generator interface for emendo sensor simulation
    '''

    def __init__(self, config: GeneratorConfig):
        self.config = config