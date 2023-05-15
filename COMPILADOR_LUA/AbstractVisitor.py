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

    @abstractmethod  
    def visitProgramConcrete2(self, programConcrete):pass

    @abstractmethod 
    def visitCommandRotulo(self, commandRotulo):pass
      
    @abstractmethod 
    def visitCommandDoEnd(self, commandDoEnd):pass

    @abstractmethod  
    def visitCommandStructRepeat(self, commandStructRepeat):pass

    @abstractmethod  
    def visitCommandIf(self, commandIf):pass

    @abstractmethod  
    def visitCommandIf2(self, commandIf):pass

    @abstractmethod 
    def visitCommandIf3(self, commandIf):pass
      
    @abstractmethod 
    def visitCommandElseIf(self, commandIf):pass

    @abstractmethod 
    def visitCommandElse(self, commandIf):pass

    @abstractmethod 
    def visitCommandElseIf2(self, commandIf):pass

    @abstractmethod  
    def visitCommandStructForIn(self, commandStructForIn):pass

    @abstractmethod  
    def visitCommandStructFor(self, commandStructFor):pass
      
    @abstractmethod  
    def visitCommandRet1(self, commandRet):pass

    @abstractmethod 
    def visitCommandRet2(self, commandRet):pass

    @abstractmethod 
    def visitCommandRet3(self, commandRet):pass
      
    @abstractmethod  
    def visitCommandDefFunction(self, commandDefFunction):pass

    @abstractmethod 
    def visitCommandFunction(self, commandFunction):pass

    @abstractmethod   
    def visitCommandNameFunction(self, commandName):pass
    
    @abstractmethod 
    def visitCommandListvars(self, commandListvars):pass

    @abstractmethod  
    def visitCommandVar(self, commandVar):pass

    @abstractmethod  
    def visitCommandListNames(self, commandListNames):pass

    @abstractmethod  
    def visitCommandListExps(self, commandListExps):pass

    @abstractmethod 
    def visitCommandExpNil(self, commandExp):pass

    @abstractmethod 
    def visitBooleanExp(self, booleanExp): pass

    @abstractmethod 
    def visitCommandExpNumber(self, commandExp):pass

    @abstractmethod  
    def visitCommandExpString(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpTag(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpMinus(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpNot(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpPlus(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpDivide(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpExpo(self, commandExp):pass

    @abstractmethod  
    def visitCommandExpPercentual(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpConcat(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpLt(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpLtEquals(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpGt(self, commandExp):pass

    @abstractmethod 
    def visitCommandExpGtEquals(self, commandExp):pass

    @abstractmethod  
    def visitCommandExpEquals(self, commandExp):pass

    @abstractmethod    
    def visitCommandExpDif(self, commandExp):pass

    @abstractmethod    
    def visitCommandExpAnd(self, commandExp):pass

    @abstractmethod  
    def visitCommandExpOr(self, commandExp):pass

    @abstractmethod    
    def visitCommandPrefix1(self, commandPrefix):pass

    @abstractmethod 
    def visitCommandPrefix2(self, commandPrefix):pass

    @abstractmethod 
    def visitCommandArgs(self, commandArgs):pass

    @abstractmethod 
    def visitCommandArgs2(self, commandArgs):pass

    @abstractmethod  
    def visitCommandBodyFunction(self, commandFunction):pass

    @abstractmethod 
    def visitCommandListPars(self, commandListPars):pass

    @abstractmethod 
    def visitCommandListPars2(self, commandListPars):pass

    @abstractmethod 
    def visitCommandListPars3(self, commandListPars):pass

    @abstractmethod 
    def visitCommandListFields(self, commandListFields):pass
      
    @abstractmethod 
    def visitCommandListFields2(self, commandListFields):pass

    @abstractmethod 
    def visitCommandListFields3(self, commandListFields):pass
      
    @abstractmethod 
    def visitCommandListFields4(self, commandListFields):pass

    @abstractmethod    
    def visitCommandListFieldEmpty(self, commandListField):pass

    @abstractmethod 
    def visitCommandListField(self, commandListField):pass
      
    @abstractmethod 
    def visitCommandListField2(self, commandListField):pass
      
    @abstractmethod 
    def visitCommandSeparatorFields(self, commandListField):pass

    @abstractmethod 
    def visitCommandSeparatorFields2(self, commandListField):pass
      
    @abstractmethod 
    def visitCommandLocalVar(self, commandLocalVar):pass
      
    @abstractmethod  
    def visitCommandLocalVar2(self, commandLocalVar):pass

    @abstractmethod  
    def visitCommandLocalVar3(self, commandLocalVar):pass