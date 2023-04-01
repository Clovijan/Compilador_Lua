from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

# declaração de programa
class Program(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass