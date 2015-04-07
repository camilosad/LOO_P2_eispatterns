from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.machine import Machine
from domain.resource.operation import operation
from domain.supportive.association_error import AssociationError


class MovieDecorator(Decorator):
    '''Movie'''
    decoration_rules = ['should_be_instance_of_machine']

    def __init__(self, name):
        Decorator.__init__(self)
        self.description = "A movie"
        self.name = name
	    self.restricted = False

    @operation(category='business')
    def register_credit(self):
	    self.restricted = True
