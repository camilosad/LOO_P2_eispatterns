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
    def should_be_instance_of_atendente(self, associated):
        '''Associated object should be instance of Aluguel Analyst Decorator'''
        from locadora.decorators.atendente_decorator import AtendenteDecorator
        try: associated |should| be_instance_of(AtendenteDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_pedido(self, associated):
        '''Associated object should be instance of Aluguel Request'''
        from locadora.resources.pedido import Pedido
        try: associated |should| be_instance_of(Pedido)
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

