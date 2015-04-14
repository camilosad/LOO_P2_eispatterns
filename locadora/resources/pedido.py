from datetime import datetime
from should_dsl import should, ShouldNotSatisfied
from eispatterns.domain.supportive.association_error import AssociationError
from eispatterns.domain.resource.work_item import WorkItem
from eispatterns.domain.supportive.rule_manager import RuleManager


class Pedido(WorkItem):
    ''' A Pedido has a filme, a date and time, a associated atendente and a cliente '''
    def __init__(self, filme, atendente, cliente):
        WorkItem.__init__(self)
        self.approved = False
        self.datetime = datetime.now()
        if not RuleManager.get_instance().check_rule('should_be_instance_of_filme', filme):
           raise AssociationError('Filme instance expected, instead %s passed' % type(filme))
        self.filme = filme
        if not RuleManager.get_instance().check_rule('should_be_instance_of_atendente', atendente):
            raise AssociationError('Atendente instance expected, instead %s passed' % type(atendente))
        self.atendente = atendente
        if not RuleManager.get_instance().check_rule('should_be_instance_of_cliente', cliente):
            raise AssociationError('Cliente instance expected, instead %s passed' % type(cliente))
        self.cliente = cliente
