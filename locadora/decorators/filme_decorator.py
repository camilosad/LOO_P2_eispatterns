
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.machine import Machine
from eispatterns.domain.resource.operation import operation
from eispatterns.domain.supportive.association_error import AssociationError

class FilmeDecorator(Decorator):
    '''Filme'''
    decoration_rules = ['should_be_instance_of_machine']

    def __init__(self, name):
        Decorator.__init__(self)
        self.description = "Any description"
        self.name = name
        self.restricted = False

    @operation(category='business')
    def register_filme_aluguel(self):
        ''' Atualiza status do filme para indisponivel '''
        self.restricted = True
