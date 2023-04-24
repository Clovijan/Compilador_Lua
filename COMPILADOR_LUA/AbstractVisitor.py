from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgramConcrete(self, program): pass

    @abstractmethod
    def visitBlockConcrete(self, block): pass

    @abstractmethod
    def visitCommandConcrete(self, command): pass

   