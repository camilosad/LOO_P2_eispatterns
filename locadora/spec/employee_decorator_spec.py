import unittest
from should_dsl import should
from domain.node.person import Person
from domain.supportive.association_error import AssociationError
from locadora.decorators.client_decorator import ClientDecorator


class ClientDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.an_client_decorator = ClientDecorator()
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should work
        self.an_client_decorator.decorate(self.a_person)
        self.an_client_decorator.decorated |should| be(self.a_person)
        self.an_client_decorator.decorated |should| have(1).decorators
        #should fail
        decorate,_,_ = self.an_client_decorator.decorate('I am not a person')
        decorate |should| equal_to(False)

    def it_generates_register(self):
        self.an_client_decorator.generate_register('123456-7')
        self.an_client_decorator.register |should| equal_to('123456-7')

