import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from locadora.resources.pedido import Pedido
from locadora.decorators.filme_decorator import FilmeDecorator
from locadora.decorators.atendente_decorator import AtendenteDecorator
from locadora.decorators.cliente_decorator import ClienteDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class PedidoSpec(unittest.TestCase):

    def it_check_associations_with_filme_and_atendente(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        a_filme = FilmeDecorator('Winter is coming')
        an_atendente = AtendenteDecorator('abcde-f')
        (Pedido, 'I am not an filme', 123, an_atendente) |should| throw(AssociationError)
        (Pedido, a_filme, 123, 'I am not an atendente') |should| throw(AssociationError)
        (Pedido, a_filme, an_atendente) |should_not| throw(AssociationError)

    def it_check_associations_with_filme_and_cliente(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        a_filme = FilmeDecorator('Winter is coming')
        a_client = ClienteDecorator()
        (Pedido, 'I am not an filme', 123, a_client) |should| throw(AssociationError)
        (Pedido, a_filme, 123, 'I am not a client') |should| throw(AssociationError)
        (Pedido, a_filme, a_client) |should_not| throw(AssociationError)

