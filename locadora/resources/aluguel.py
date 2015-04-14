from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.supportive.rule import rule
from eispatterns.domain.resource.work_item import WorkItem
from locadora.resources.pedido import Pedido
from eispatterns.domain.supportive.rule_manager import RuleManager


class Aluguel(WorkItem):
    ''' A Aluguel is generated from a Aluguel Request '''
    def __init__(self, pedido):
        WorkItem.__init__(self)
        if not RuleManager.get_instance().check_rule('should_be_instance_of_pedido', pedido):
           raise AssociationError('Aluguel Request instance expected, instead %s passed' % type(pedido))
        self.pedido = pedido
        self.datetime = datetime.now()
        self.pedido.movie.register_movie_aluguel()

