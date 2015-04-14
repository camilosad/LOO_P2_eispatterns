from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.person import Person
from eispatterns.domain.resource.operation import operation
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.association_error import AssociationError


class ClienteDecorator(Decorator):
    '''A general purpose Cliente decorator'''
    decoration_rules = ['should_be_instance_of_person']
    def __init__(self):
        Decorator.__init__(self)
        self.name = "Any client"

    def generate_register(self, register):
        ''' generates the register number for the cliente '''
        self.register = register

