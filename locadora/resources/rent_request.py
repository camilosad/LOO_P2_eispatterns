from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.resource.work_item import WorkItem
from eispatterns.domain.supportive.rule_manager import RuleManager


class RentRequest(WorkItem):
    ''' A Rent Request has a movie, a date and time, and an associated analyst '''
    def __init__(self, movie, analyst, client):
        WorkItem.__init__(self)
        self.approved = False
        self.datetime = datetime.now()
        if not RuleManager.get_instance().check_rule('should_be_instance_of_movie', movie):
           raise AssociationError('Movie instance expected, instead %s passed' % type(movie))
        self.movie = movie
        if not RuleManager.get_instance().check_rule('should_be_instance_of_atendente', analyst):
            raise AssociationError('Rent Analyst instance expected, instead %s passed' % type(analyst))
        self.analyst = analyst
        if not RuleManager.get_instance().check_rule('should_be_instance_of_client', client):
            raise AssociationError('Client instance expected, instead %s passed' % type(client))
        self.client = client
