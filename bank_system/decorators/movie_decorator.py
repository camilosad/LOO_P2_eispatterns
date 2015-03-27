from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.machine import Machine
from domain.resource.operation import operation
from domain.supportive.association_error import AssociationError


class MovieDecorator(Decorator):
    '''Movie'''
    decoration_rules = ['should_be_instance_of_machine']

    def __init__(self, name):
        Decorator.__init__(self)
        self.description = "A movie"
        #log area for already processed resources
        self.log_area = {}
        #should it mask Machine.tag? decorated.tag = name?
        self.name = name
        self.balance = 0
        self.restricted = False
        self.average_rent = 0
   
    # @operation(category='business')
    # def register_rent(self, value):
    #     ''' Register a rent in the balance '''
    #     self.balance += value

    # @operation(category='business')
    # def send_message_to_account_holder(self, message):
    #     ''' Sends a message to the account holder '''
    #     return message

