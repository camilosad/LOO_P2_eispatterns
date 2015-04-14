import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from locadora.resources.pedido import Pedido
from locadora.decorators.movie_decorator import MovieDecorator
from locadora.decorators.atendente_decorator import AtendenteDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class PedidoSpec(unittest.TestCase):

    def it_check_associations_with_movie_and_atendente(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        a_movie = MovieDecorator('Winter is coming')
        an_analyst = AtendenteDecorator('abcde-f')
        (Pedido, 'I am not an movie', 123, an_analyst) |should| throw(AssociationError)
        (Pedido, a_movie, 123, 'I am not an analyst') |should| throw(AssociationError)
        (Pedido, a_movie, an_analyst) |should_not| throw(AssociationError)

