from node import Node
from eispatterns.domain.supportive.rule import rule


class Person(Node):
    def __init__(self):
        Node.__init__(self)
        self.name = None
        self.contact_information = None

