import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from locadora.resources.pedido import Pedido
from locadora.resources.aluguel import Aluguel
from locadora.decorators.atendente_decorator import AtendenteDecorator
from locadora.decorators.movie_decorator import MovieDecorator
from locadora.decorators.client_decorator import ClientDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class AluguelSpec(unittest.TestCase):

    def it_check_association_with_pedido(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        (Aluguel, 'I am not a aluguel request') |should| throw(AssociationError)
        a_atendente_decorator = AtendenteDecorator('12345-6')
        a_movie = MovieDecorator('Winter is coming')
        a_person = ClientDecorator()
        a_pedido = Pedido(a_movie, a_atendente_decorator, a_person)
        (Aluguel, a_pedido) |should_not| throw(AssociationError)

