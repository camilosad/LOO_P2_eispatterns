from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.node.node import Node
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError
from domain.supportive.contract_error import ContractError
from locadora.resources.rent_request import RentRequest
from locadora.resources.rent import Rent
from locadora.decorators.movie_decorator import MovieDecorator
from locadora.decorators.employee_decorator import EmployeeDecorator


class AttendantDecorator(Decorator):
    '''Attendant'''
    decoration_rules = ['should_have_employee_decorator']

    def __init__(self, register):
        Decorator.__init__(self)
        self.description = "An employee with credit analysis skills"
        self.register = register
        self.rent_limit = 0

    @operation(category='business')
    def create_rent_request(self, account, value):
        ''' creates a rent request '''
        rent_request = RentRequest(account, value, self)
        #places the rent_request in the node's input area
        self.decorated.input_area[rent_request.account.number] = rent_request

    #stupid credit analysis, only for demonstration
    @operation(category='business')
    def analyse(self, rent_request_key):
        ''' automatically analyses a rent request '''
        if not self.decorated.input_area.has_key(rent_request_key): return False
        #move the request from the input_area to the processing_area
        self.decorated.transfer(rent_request_key,'input','processing')
        #picks the rent for processing
        rent_request = self.decorated.processing_area[rent_request_key]
        #automatically approves or not
        if not rent_request.account.restricted:
           if rent_request.account.average_credit*4 > rent_request.value:
               rent_request.approved = True
           else:
               rent_request.approved = False
        else:
           rent_request.approved = False
        #transfers the rent to the output_area
        self.decorated.transfer(rent_request_key,'processing','output')

    @operation(category='business')
    def create_rent(self, rent_request):
        ''' creates a rent '''
        rent = Rent(rent_request)
        #puts the new rent on the analyst's output_area, using analyst's register as key
        self.decorated.output_area[rent.rent_request.analyst.register] = rent

    @operation(category='business')
    def move_rent_to_account(self, rent_key, account):
        ''' moves the approved rent to the account '''
        try:
            rent = self.decorated.output_area[rent_key]
            rent |should| be_instance_of(Rent)
        except KeyError:
            raise KeyError("Rent with key %s not found in Analyst's output area" % rent_key)
        except ShouldNotSatisfied:
            raise ContractError('Rent instance expected, instead %s passed' % type(rent))
        try:
            Node.move_resource(rent_key, self.decorated, account.decorated)
        except ShouldNotSatisfied:
            raise ContractError('Bank Account instance expected, instead %s passed' % type(account))
        account.register_credit(rent.rent_request.value)

    def change_rent_limit(self, new_limit):
        self.rent_limit = new_limit

