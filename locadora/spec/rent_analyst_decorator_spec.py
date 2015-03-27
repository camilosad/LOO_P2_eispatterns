import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.node.machine import Machine
from domain.supportive.association_error import AssociationError
from domain.supportive.contract_error import ContractError
from locadora.resources.rent_request import RentRequest
from locadora.resources.rent import Rent
from locadora.decorators.attendant_decorator import AttendantDecorator
from locadora.decorators.bank_account_decorator import MovieDecorator
from locadora.decorators.client_decorator import ClientDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from domain.supportive.rule_manager import RuleManager


class AttendantDecoratorSpec(unittest.TestCase):

    def setUp(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        self.a_attendant_decorator = AttendantDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()
        self.an_account = MovieDecorator('1234567-8')

    def it_decorates_a_person(self):
        #should fail
        decorate, _, _ = self.a_attendant_decorator.decorate(self.a_person)
        decorate |should| equal_to(False)
        #should work
        an_client_decorator = ClientDecorator()
        an_client_decorator.decorate(self.a_person)
        self.a_attendant_decorator.decorate(self.a_person)
        self.a_attendant_decorator.decorated |should| be(self.a_person)
        self.a_attendant_decorator.decorated |should| have(2).decorators

    def it_creates_a_rent_request(self):
        an_client_decorator = ClientDecorator()
        an_client_decorator.decorate(self.a_person)
        self.a_attendant_decorator.decorate(self.a_person)
        self.a_attendant_decorator.create_rent_request(self.an_account, 10000)
        self.a_person.input_area |should| contain('1234567-8')

    def it_analyses_a_rent_request(self):
        an_client_decorator = ClientDecorator()
        an_client_decorator.decorate(self.a_person)
        #Stub removed, from now on Node really transfers resources internally
        self.a_attendant_decorator.decorate(self.a_person)
        self.an_account.average_credit = 5000
        #should approve
        self.a_attendant_decorator.create_rent_request(self.an_account, 10000)
        self.a_attendant_decorator.analyse(self.an_account.number)
        self.a_attendant_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(True)
        #should refuse
        self.a_attendant_decorator.create_rent_request(self.an_account, 50000)
        self.a_attendant_decorator.analyse(self.an_account.number)
        self.a_attendant_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(False)

    def it_creates_a_rent(self):
        an_client_decorator = ClientDecorator()
        an_client_decorator.decorate(self.a_person)
        rent_request = RentRequest(self.an_account, 7000, self.a_attendant_decorator)
        self.a_attendant_decorator.decorate(self.a_person)
        self.a_attendant_decorator.decorated.output_area[self.an_account.number] = rent_request
        #creates a machine to be decorated by the account - will need to check its processing_area
        a_machine = Machine()
        self.an_account.decorate(a_machine)
        #creates the rent
        self.a_attendant_decorator.create_rent(rent_request)
        #rent key is the analyst's register
        self.a_attendant_decorator.decorated.output_area.values() |should| have_at_least(1).rent
        self.a_attendant_decorator.decorated.output_area |should| include(self.a_attendant_decorator.register)

    def it_moves_the_rent_to_an_account(self):
        #prepares the person Node
        an_client_decorator = ClientDecorator()
        an_client_decorator.decorate(self.a_person)
        self.a_attendant_decorator.decorate(self.a_person)
        #prepares a Rent
        rent_request = RentRequest(self.an_account, 7000, self.a_attendant_decorator)
        self.a_attendant_decorator.decorated.output_area[self.an_account.number] = rent_request
        self.a_attendant_decorator.create_rent(rent_request)
        #should go wrong
        passing_a_wrong_key = 'wrong key'
        (self.a_attendant_decorator.move_rent_to_account, passing_a_wrong_key, self.an_account) |should| throw(KeyError)
        passing_a_non_account = 'I am not an account'
        (self.a_attendant_decorator.move_rent_to_account, self.an_account.number, passing_a_non_account) |should| throw(ContractError)
        #prepares the account
        a_machine = Machine()
        self.an_account.decorate(a_machine)
        #should work
        rent_key = self.a_attendant_decorator.register
        self.a_attendant_decorator.move_rent_to_account(rent_key, self.an_account)
        self.an_account.decorated.input_area |should| include(rent_key)
        self.an_account.balance |should| equal_to(7000)

    def it_changes_its_rent_limit(self):
        self.a_attendant_decorator.change_rent_limit(100000)
        self.a_attendant_decorator.rent_limit |should| be(100000)

