from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.person import Person
from eispatterns.domain.resource.operation import operation
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.association_error import AssociationError


class ClientDecorator(Decorator):
    '''A general purpose Client decorator'''
    decoration_rules = ['should_be_instance_of_person']
    def __init__(self):
        Decorator.__init__(self)
        self.description = "Supplies the basis for representing employes"

    def generate_register(self, register):
        ''' generates the register number for the client '''
        self.register = register

