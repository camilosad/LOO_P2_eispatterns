from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.resource.work_item import WorkItem
from eispatterns.domain.supportive.rule_manager import RuleManager


class RentRequest(WorkItem):
    ''' A Rent Request has a movie, a date and time, and an associated analyst '''
    def __init__(self, movie, analyst, employee):
        WorkItem.__init__(self)
        self.approved = False
        self.datetime = datetime.now()
        if not RuleManager.get_instance().check_rule('should_be_instance_of_movie', movie):
           raise AssociationError('Movie instance expected, instead %s passed' % type(movie))
        self.movie = movie
        if not RuleManager.get_instance().check_rule('should_be_instance_of_rent_analyst', analyst):
            raise AssociationError('Rent Analyst instance expected, instead %s passed' % type(analyst))
        self.analyst = analyst
        if not RuleManager.get_instance().check_rule('should_be_instance_of_employee', employee):
            raise AssociationError('Employee instance expected, instead %s passed' % type(employee))
        self.employee = employee
