from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.core_rules import CoreRules


class LocadoraRuleBase(CoreRules):
    @rule('association')
    def should_be_instance_of_filme(self, associated):
        '''Associated object should be instance of Filme Decorator'''
        from locadora.decorators.filme_decorator import FilmeDecorator
        try: associated |should| be_instance_of(FilmeDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_cliente(self, associated):
        '''Associated object should be instance of Filme Decorator'''
        from locadora.decorators.cliente_decorator import ClienteDecorator
        try: associated |should| be_instance_of(ClienteDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_atendente(self, associated):
        '''Associated object should be instance of Atendente Decorator'''
        from locadora.decorators.atendente_decorator import AtendenteDecorator
        try: associated |should| be_instance_of(AtendenteDecorator)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_pedido(self, associated):
        '''Associated object should be instance of Pedido'''
        from locadora.resources.pedido import Pedido
        try: associated |should| be_instance_of(Pedido)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_have_cliente_decorator(self, associated):
        '''Associated object should be previously decorated by Cliente'''
        from locadora.decorators.cliente_decorator import ClienteDecorator
        import eispatterns.domain.supportive.contract_matchers
        try: associated |should| be_decorated_by(ClienteDecorator)
        except ShouldNotSatisfied: return False
        else: return True

