from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgramConcrete(self, program): pass

    @abstractmethod
    def visitBlockConcrete(self, block): pass

    @abstractmethod
    def visitCommandConcrete(self, command): pass

    @abstractmethod
    def visitCommandCallFunction(self, commandCallFunction): pass

    @abstractmethod
    def visitCommandStructWhile(self, commandStructWhile): pass

   