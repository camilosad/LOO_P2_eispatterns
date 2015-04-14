import unittest
from should_dsl import should
from eispatterns.domain.node.person import Person
from eispatterns.domain.supportive.association_error import AssociationError
from locadora.decorators.cliente_decorator import ClienteDecorator


class ClienteDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.an_cliente_decorator = ClienteDecorator()
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should work
        self.an_cliente_decorator.decorate(self.a_person)
        self.an_cliente_decorator.decorated |should| be(self.a_person)
        self.an_cliente_decorator.decorated |should| have(1).decorators
        #should fail
        decorate,_,_ = self.an_cliente_decorator.decorate('I am not a person')
        decorate |should| equal_to(False)

    def it_generates_register(self):
        self.an_cliente_decorator.generate_register('123456-7')
        self.an_cliente_decorator.register |should| equal_to('123456-7')

