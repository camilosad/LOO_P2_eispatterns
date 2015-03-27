from should_dsl import should, ShouldNotSatisfied
from domain.supportive.rule import rule
from domain.supportive.core_rules import CoreRules


class LocadoraRuleBase(CoreRules):
    @rule('association')
    def should_be_instance_of_movie(self, associated):
        '''Associated object should be instance of Movie Decorator'''
        from locadora.decorators.movie_decorator import MovieDecorator
        try: associated |should| be_instance_of(MovieDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_attendant(self, associated):
        '''Associated object should be instance of Attendant Decorator'''
        from locadora.decorators.attendant_decorator import AttendantDecorator
        try: associated |should| be_instance_of(AttendantDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_rent_request(self, associated):
        '''Associated object should be instance of Rent Request'''
        from locadora.resources.rent_request import RentRequest
        try: associated |should| be_instance_of(RentRequest)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_have_client_decorator(self, associated):
        '''Associated object should be previously decorated by Client'''
        from locadora.decorators.client_decorator import ClienteDecorator
        import domain.supportive.contract_matchers
        try: associated |should| be_decorated_by(ClienteDecorator)
        except ShouldNotSatisfied: return False
        else: return True

