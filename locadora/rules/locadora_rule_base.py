from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.core_rules import CoreRules


class LocadoraRuleBase(CoreRules):
    @rule('association')
    def should_be_instance_of_movie(self, associated):
        '''Associated object should be instance of Movie Decorator'''
        from locadora.decorators.movie_decorator import MovieDecorator
        try: associated |should| be_instance_of(MovieDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_client(self, associated):
        '''Associated object should be instance of Movie Decorator'''
        from locadora.decorators.client_decorator import ClientDecorator
        try: associated |should| be_instance_of(ClientDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_rent_analyst(self, associated):
        '''Associated object should be instance of Rent Analyst Decorator'''
        from locadora.decorators.rent_analyst_decorator import RentAnalystDecorator
        try: associated |should| be_instance_of(RentAnalystDecorator)
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
        from locadora.decorators.client_decorator import ClientDecorator
        import eispatterns.domain.supportive.contract_matchers
        try: associated |should| be_decorated_by(ClientDecorator)
        except ShouldNotSatisfied: return False
        else: return True

