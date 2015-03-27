from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from domain.supportive.association_error import AssociationError
from domain.resource.work_item import WorkItem
from domain.supportive.rule_manager import RuleManager


class RentRequest(WorkItem):
    ''' A Rent Request has a movie, a date and time, and an associated attendant '''
    def __init__(self, movie, attendant):
        WorkItem.__init__(self)
        self.movie = movie
        self.approved = False
        self.datetime = datetime.now()
        if not RuleManager.get_instance().check_rule('should_be_instance_of_movie', account):
           raise AssociationError('Movie instance expected, instead %s passed' % type(account))
        self.account = account
        if not RuleManager.get_instance().check_rule('should_be_instance_of_attendant', analyst):
            raise AssociationError('Attendant instance expected, instead %s passed' % type(analyst))

