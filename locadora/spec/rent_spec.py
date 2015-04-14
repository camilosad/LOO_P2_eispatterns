import unittest
from should_dsl import should, should_not
from eispatterns.domain.supportive.association_error import AssociationError
from locadora.resources.rent_request import RentRequest
from locadora.resources.rent import Rent
from locadora.decorators.rent_analyst_decorator import RentAnalystDecorator
from locadora.decorators.movie_decorator import MovieDecorator
from locadora.decorators.client_decorator import ClientDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class RentSpec(unittest.TestCase):

    def it_check_association_with_rent_request(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        (Rent, 'I am not a rent request') |should| throw(AssociationError)
        a_rent_analyst_decorator = RentAnalystDecorator('12345-6')
        a_movie = MovieDecorator('Winter is coming')
        a_person = ClientDecorator()
        a_rent_request = RentRequest(a_movie, a_rent_analyst_decorator, a_person)
        (Rent, a_rent_request) |should_not| throw(AssociationError)

