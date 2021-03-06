from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.base.decorator import Decorator
from eispatterns.domain.node.person import Person
from eispatterns.domain.node.node import Node
from eispatterns.domain.resource.operation import operation
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.supportive.contract_error import ContractError
from locadora.resources.pedido import Pedido
from locadora.resources.aluguel import Aluguel
from locadora.decorators.filme_decorator import FilmeDecorator
from locadora.decorators.cliente_decorator import ClienteDecorator


class AtendenteDecorator(Decorator):
    '''Atendente'''
    decoration_rules = ['should_have_cliente_decorator']

    def __init__(self, register):
        Decorator.__init__(self)
        self.register = register
        self.aluguel_limit = 0

    @operation(category='business')
    def create_pedido(self, filme, cliente):
        ''' creates a aluguel request '''
        pedido = Pedido(filme, self, cliente)
        #places the pedido in the node's input area
        self.decorated.input_area[pedido.filme.name] = pedido

    #stupid aluguel analysis, only for demonstration
    @operation(category='business')
    def analyse(self, pedido_key):
        ''' automatically analyses a aluguel request '''
        if not self.decorated.input_area.has_key(pedido_key): return False
        #move the request from the input_area to the processing_area
        self.decorated.transfer(pedido_key,'input','processing')
        #picks the aluguel for processing
        pedido = self.decorated.processing_area[pedido_key]
        #automatically approves or not
        if not pedido.filme.restricted:
           pedido.approved = True
        else:
           pedido.approved = False
        #transfers the aluguel to the output_area
        self.decorated.transfer(pedido_key,'processing','output')

    @operation(category='business')
    def create_aluguel(self, pedido):
        ''' creates a aluguel '''
        aluguel = Aluguel(pedido)
        #puts the new aluguel on the atendente's output_area, using atendente's register as key
        self.decorated.output_area[aluguel.pedido.atendente.register] = aluguel


