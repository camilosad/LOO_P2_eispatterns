from should_dsl import should,should_not, ShouldNotSatisfied
from rule import rule
from core_rules import CoreRules


class RuleManager(object):
    #Singleton machinery
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RuleManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()
    #/Singleton machinery

    #should be through configuration
    rule_base = CoreRules()
    def __init__(self):
        self.rules = RuleManager.rule_base

    def check_decoration_rules(self, decorator_class, decoration_candidate):
        '''Checks all decoration rules of a given decorator upon a given decoration candidate'''
        approved_rules = []
        refused_rules = []
        if not decorator_class.decoration_rules:
           raise ValueError('%s type has no decoration rules' % decorator_class.__name__)
        for rule in decorator_class.decoration_rules:
            try:
                approved = getattr(self.rules, rule)(decoration_candidate)
            except AttributeError:
                raise AttributeError('Rule Manager has no %s rule' % rule)
            rule_object_docstring = getattr(self.rules, rule).__doc__
            if approved:
                approved_rules.append(rule_object_docstring)
            else:
                refused_rules.append(rule_object_docstring)
        if not refused_rules:
            return True, approved_rules, None
        else:
            return False, approved_rules, refused_rules

    def check_rule(self, rule, association_candidate):
        '''Check a single rule for a given association candidate'''
        try:
            approved = getattr(self.rules, rule)(association_candidate)
        except AttributeError:
            raise AttributeError('Rule Manager has no %s rule' % rule)
        return approved

    #(1)rules in fact should be loaded from a configuration file
    #(2)need to develop a rule builder - through decorator
    @rule('association')
    def should_be_instance_of_person(self, associated):
        '''Associated object should be instance of Person'''
        from eispatterns.domain.node.person import Person
        try: associated |should| be_instance_of(Person)
        except ShouldNotSatisfied: return False
        else: return True

    @rule('association')
    def should_be_instance_of_machine(self, associated):
        '''Associated object should be instance of Machine'''
        from eispatterns.domain.node.machine import Machine
        try: associated |should| be_instance_of(Machine)
        except ShouldNotSatisfied: return False
        else: return True

    #
    #Really ugly stuff:
    #the rules below should me managed by AcademicSystemRuleManager
    #when dynamic loading is ready they will leave this class
    #
	@rule('association')
	def should_be_instance_of_aluno(self, associated):
		'''Associated object should be instance of Aluno Decorator'''
		from academico.decorators.aluno_decorator import AlunoDecorator
		try: associated |should| be_instance_of(AlunoDecorator)
		except ShouldNotSatisfied: return False
		else: return True

	@rule('association')
	def should_be_instance_of_curso(self, associated):
		'''Associated object should be instance of Curso Decorator'''
		from academico.decorators.curso_decorator import CursoDecorator
		try: associated |should| be_instance_of(CursoDecorator)
		except ShouldNotSatisfied: return False
		else: return True

	@rule('association')
	def should_be_instance_of_curso(self, associated):
		'''Associated object should be instance of Curso Decorator'''
		from academico.decorators.curso_decorator import CursoDecorator
		try: associated |should| be_instance_of(CursoDecorator)
		except ShouldNotSatisfied: return False
		else: return True

	@rule('association')
	def should_have_curso_decorator(self, associated):
		'''Associated object should be previously decorated by Curso'''
		from academico.decorators.curso_decorator import CursoDecorator
		import domain.supportive.contract_matchers
		try: associated |should| be_decorated_by(CursoDecorator)
		except ShouldNotSatisfied: return False
		else: return True

	@rule('association')
	def should_not_be_decorated_by_curso_superior_decorator(self,associated):
		''' Associated object should not be previously decorated by Curso Superior '''
		from academico.decorators.superior_decorator import SuperiorDecorator 
		import eispatterns.domain.supportive.contract_matchers
		try: associated |should_not| be_decorated_by(SuperiorDecorator)
		except ShouldNotSatisfied: return False
		else: return True

	@rule('association')
	def should_not_be_decorated_by_curso_tecnico_decorator(self,associated):
		''' Associated object should not be previously decorated by Curso Tecnico '''
		from academico.decorators.tecnico_decorator import TecnicoDecorator 
		import eispatterns.domain.supportive.contract_matchers
		try: associated |should_not| be_decorated_by(TecnicoDecorator)
		except ShouldNotSatisfied: return False
		else: return True	



