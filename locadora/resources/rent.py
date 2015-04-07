from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from domain.supportive.association_error import AssociationError
from domain.supportive.rule import rule
from domain.resource.work_item import WorkItem
from locadora.resources.rent_request import RentRequest
from domain.supportive.rule_manager import RuleManager


class Rent(WorkItem):
    ''' A Rent is generated from a Rent Request '''
    def __init__(self, rent_request):
        WorkItem.__init__(self)
        if not RuleManager.get_instance().check_rule('should_be_instance_of_rent_request', rent_request):
           raise AssociationError('Rent Request instance expected, instead %s passed' % type(rent_request))
        self.rent_request = rent_request
        self.datetime = datetime.now()
 	self.rent_request.movie.register_rent()

