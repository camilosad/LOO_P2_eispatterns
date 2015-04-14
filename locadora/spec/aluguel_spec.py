import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from locadora.resources.pedido import Pedido
from locadora.resources.aluguel import Aluguel
from locadora.decorators.atendente_decorator import AtendenteDecorator
from locadora.decorators.filme_decorator import FilmeDecorator
from locadora.decorators.cliente_decorator import ClienteDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class AluguelSpec(unittest.TestCase):

    def it_check_association_with_pedido(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        (Aluguel, 'I am not a pedido') |should| throw(AssociationError)
        a_atendente_decorator = AtendenteDecorator('12345-6')
        a_filme = FilmeDecorator('Winter is coming')
        a_person = ClienteDecorator()
        a_pedido = Pedido(a_filme, a_atendente_decorator, a_person)
        (Aluguel, a_pedido) |should_not| throw(AssociationError)

