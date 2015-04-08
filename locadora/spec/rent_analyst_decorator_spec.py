import unittest
from should_dsl import should, should_not
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.machine import Machine
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.supportive.contract_error import ContractError
from locadora.resources.rent_request import RentRequest
from locadora.resources.rent import Rent
from locadora.decorators.rent_analyst_decorator import RentAnalystDecorator
from locadora.decorators.movie_decorator import MovieDecorator
from locadora.decorators.employee_decorator import EmployeeDecorator
from locadora.rules.locadora_rule_base import LocadoraRuleBase
from eispatterns.domain.supportive.rule_manager import RuleManager


class RentAnalystDecoratorSpec(unittest.TestCase):

    def setUp(self):
        #set the rule base
        RuleManager.rule_base = LocadoraRuleBase()
        #
        self.a_rent_analyst_decorator = RentAnalystDecorator('12345-6')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()
        self.an_employee = EmployeeDecorator()
        self.a_movie = MovieDecorator('1234567-8')

    def it_decorates_a_person(self):
        #should fail
        decorate, _, _ = self.a_rent_analyst_decorator.decorate(self.a_person)
        decorate |should| equal_to(False)
        #should work
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        self.a_rent_analyst_decorator.decorate(self.a_person)
        self.a_rent_analyst_decorator.decorated |should| be(self.a_person)
        self.a_rent_analyst_decorator.decorated |should| have(2).decorators

    def it_creates_a_rent_request(self):
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        self.a_rent_analyst_decorator.decorate(self.a_person)
        self.a_rent_analyst_decorator.create_rent_request(self.a_movie, self.an_employee)
        self.a_person.input_area |should| contain('1234567-8')

    def it_analyses_a_rent_request(self):
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        #Stub removed, from now on Node really transfers resources internally
        self.a_rent_analyst_decorator.decorate(self.a_person)
        #should approve
        self.a_rent_analyst_decorator.create_rent_request(self.a_movie, self.an_employee)
        self.a_rent_analyst_decorator.analyse(self.a_movie.name)
        self.a_rent_analyst_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(True)
        #should refuse
        self.a_movie.restricted = True
        self.a_rent_analyst_decorator.create_rent_request(self.a_movie, self.an_employee)
        self.a_rent_analyst_decorator.analyse(self.a_movie.name)
        self.a_rent_analyst_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(False)

    def it_creates_a_rent(self):
        an_employee_decorator = EmployeeDecorator()
        an_employee_decorator.decorate(self.a_person)
        rent_request = RentRequest(self.a_movie, self.a_rent_analyst_decorator, self.an_employee)
        self.a_rent_analyst_decorator.decorate(self.a_person)
        self.a_rent_analyst_decorator.decorated.output_area[self.a_movie.name] = rent_request
        #creates a machine to be decorated by the account - will need to check its processing_area
        a_machine = Machine()
        self.a_movie.decorate(a_machine)
        #creates the rent
        self.a_rent_analyst_decorator.create_rent(rent_request)
        #rent key is the analyst's register
        self.a_rent_analyst_decorator.decorated.output_area.values() |should| have_at_least(1).rent
        self.a_rent_analyst_decorator.decorated.output_area |should| include(self.a_rent_analyst_decorator.register)
