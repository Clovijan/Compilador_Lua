from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgramConcrete(self, program): pass

    @abstractmethod
    def visitBlockConcrete(self, block): pass

    @abstractmethod
    def visitCommandCallFunction(self, commandCallFunction): pass

    @abstractmethod
    def visitCommandStructWhile(self, commandStructWhile): pass

    @abstractmethod
    def visitCommandStructRepeat(self, commandStructRepeat): pass

    @abstractmethod
    def visitCommandStructForIn(self, commandStructForIn): pass

    @abstractmethod
    def visitCommandStructFor(self, commandStructFor): pass
      
    @abstractmethod 
    def visitCommandDefFunction(self, commandDefFunction): pass
   