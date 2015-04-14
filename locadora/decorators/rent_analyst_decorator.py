from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.node import Node
from eispatterns.domain.resource.operation import operation
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.supportive.contract_error import ContractError
from locadora.resources.rent_request import RentRequest
from locadora.resources.rent import Rent
from locadora.decorators.movie_decorator import MovieDecorator
from locadora.decorators.client_decorator import ClientDecorator


class RentAnalystDecorator(Decorator):
    '''RentAnalyst'''
    decoration_rules = ['should_have_client_decorator']

    def __init__(self, register):
        Decorator.__init__(self)
        self.description = "An client with rent analysis skills"
        self.register = register
        self.rent_limit = 0

    @operation(category='business')
    def create_rent_request(self, movie, client):
        ''' creates a rent request '''
        rent_request = RentRequest(movie, self, client)
        #places the rent_request in the node's input area
        self.decorated.input_area[rent_request.movie.name] = rent_request

    #stupid rent analysis, only for demonstration
    @operation(category='business')
    def analyse(self, rent_request_key):
        ''' automatically analyses a rent request '''
        if not self.decorated.input_area.has_key(rent_request_key): return False
        #move the request from the input_area to the processing_area
        self.decorated.transfer(rent_request_key,'input','processing')
        #picks the rent for processing
        rent_request = self.decorated.processing_area[rent_request_key]
        #automatically approves or not
        if not rent_request.movie.restricted:
           rent_request.approved = True
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


