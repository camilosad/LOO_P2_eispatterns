import unittest
from should_dsl import should, should_not
from eispatterns.domain.node.machine import Machine
from locadora.decorators.filme_decorator import FilmeDecorator
from eispatterns.domain.supportive.association_error import AssociationError


class FilmeDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_filme_decorator = FilmeDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_machine = Machine()

    def it_decorates_a_machine(self):
        #should work
        self.a_filme_decorator.decorate(self.a_machine)
        self.a_filme_decorator.decorated |should| be(self.a_machine)
        self.a_filme_decorator.decorated |should| have(1).decorators
        #should fail
        decorate, _, _ = self.a_filme_decorator.decorate('I am not a machine')
        decorate |should| equal_to(False)
