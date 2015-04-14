import unittest
from should_dsl import should, should_not
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.machine import Machine
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.supportive.contract_error import ContractError
from locadora.resources.pedido import Pedido
from locadora.resources.aluguel import Aluguel
from locadora.decorators.atendente_decorator import AtendenteDecorator
from locadora.decorators.filme_decorator import FilmeDecorator
from locadora.decorators.cliente_decorator import ClienteDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class AtendenteDecoratorSpec(unittest.TestCase):

    def setUp(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        self.a_atendente_decorator = AtendenteDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()
        self.an_cliente = ClienteDecorator()
        self.a_filme = FilmeDecorator('1234567-8')

    def it_decorates_a_person(self):
        #should fail
        decorate, _, _ = self.a_atendente_decorator.decorate(self.a_person)
        decorate |should| equal_to(False)
        #should work
        an_cliente_decorator = ClienteDecorator()
        an_cliente_decorator.decorate(self.a_person)
        self.a_atendente_decorator.decorate(self.a_person)
        self.a_atendente_decorator.decorated |should| be(self.a_person)
        self.a_atendente_decorator.decorated |should| have(2).decorators

    def it_creates_a_pedido(self):
        an_cliente_decorator = ClienteDecorator()
        an_cliente_decorator.decorate(self.a_person)
        self.a_atendente_decorator.decorate(self.a_person)
        self.a_atendente_decorator.create_pedido(self.a_filme, self.an_cliente)
        self.a_person.input_area |should| contain('1234567-8')

    def it_analyses_a_pedido(self):
        an_cliente_decorator = ClienteDecorator()
        an_cliente_decorator.decorate(self.a_person)
        #Stub removed, from now on Node really transfers resources internally
        self.a_atendente_decorator.decorate(self.a_person)
        #should approve
        self.a_atendente_decorator.create_pedido(self.a_filme, self.an_cliente)
        self.a_atendente_decorator.analyse(self.a_filme.name)
        self.a_atendente_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(True)
        #should refuse
        self.a_filme.restricted = True
        self.a_atendente_decorator.create_pedido(self.a_filme, self.an_cliente)
        self.a_atendente_decorator.analyse(self.a_filme.name)
        self.a_atendente_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(False)

    def it_creates_a_aluguel(self):
        an_cliente_decorator = ClienteDecorator()
        an_cliente_decorator.decorate(self.a_person)
        pedido = Pedido(self.a_filme, self.a_atendente_decorator, self.an_cliente)
        self.a_atendente_decorator.decorate(self.a_person)
        self.a_atendente_decorator.decorated.output_area[self.a_filme.name] = pedido
        #creates a machine to be decorated by the account - will need to check its processing_area
        a_machine = Machine()
        self.a_filme.decorate(a_machine)
        #creates the aluguel
        self.a_atendente_decorator.create_aluguel(pedido)
        #aluguel key is the analyst's register
        self.a_atendente_decorator.decorated.output_area.values() |should| have_at_least(1).aluguel
        self.a_atendente_decorator.decorated.output_area |should| include(self.a_atendente_decorator.register)
