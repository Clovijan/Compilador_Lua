from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

''' declaração de trecho'''
class Program(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class ProgramConcrete(Program):
  def __init__(self, block, function):
    self.block = block
    self.function = function
  def accept(self, visitor):
    return visitor.visitProgramConcrete(self)
  
'''declaração de bloco'''
class Block(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class BlockConcrete(Block):
  def __init__(self, command):
    self.command = command
  def accept(self, visitor):
    return visitor.visitBlockConcrete(self)

'''declaração de comando'''
class Command(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CommandCallFunction(Command):
  def __init__(self, exp_prefix, args, name):
    self.exp_prefix = exp_prefix
    self.args = args
    self.name = name
  def accept(self, visitor):
     return visitor.visitCommandCallFunction(self)

class CommandStructWhile(Command):
  def __init__(self, exp, block):
    self.exp = exp
    self.block = block
  def accept(self, visitor):
    return visitor.visitCommandStructWhile(self)

class CommandStructRepeat(Command):
  def __init__(self, block, exp):
    self.block = block
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitCommandStructRepeat(self)

class CommandStructForIn(Command):
  def __init__(self, list_names, list_exps, block):
    self.list_names = list_names
    self.list_exps = list_exps
    self.block = block
  def accept(self, visitor):
    return visitor.visitCommandStructForIn(self)

class CommandStructFor(Command):
  def __init__(self, name, exp, exp2, block):
    self.name = name
    self.exp = exp
    self.exp2 = exp
    self.block = block
  def accept(self, visitor):
    return visitor.visitCommandStructFor(self)

class CommandDefFunction(Command):
  def __init__(self, function):
    self.function = function
  def accept(self, visitor):
    return visitor.visitCommandDefFunction(self)

'''declaração de comandoret'''
class CommandRet(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CommandRetConcrete(CommandRet):
  def __init__(self, list_exps):
    self.list_exps = list_exps
  def accept(self, visitor):
    return visitor.visitCommandRet2(self)

'''declaração de nomefunção'''
class NameFunction(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de nomefunção'''
class NameFunctionConcrete(NameFunction):
  def __init__(self, name):
    self.name = name
  def accept(self, visitor):
    return visitor.visitCommandNameFunction(self)
    
'''declaração de listvars'''
class ListVars(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListvarsConcrete(ListVars):
  def __init__(self, var, list_vars):
    self.var = var
    self.list_vars = list_vars
  def accept(self, visitor):
    return visitor.visitCommandListvars(self)

'''declaração de var'''
class Var(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de var'''
class VarConcrete(Var):
  def __init__(self, name, prefix_exp, exp):
    self.name = name
    self.prefix_exp = prefix_exp
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitCommandVar(self)

'''declaração de listadenomes'''
class ListNames(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListNamesConcrete(ListNames):
  def __init__(self, name, list_names):
    self.name = name
    self.list_names = list_names
  def accept(self, visitor):
    return visitor.visitListNames(self)

'''declaração de listaexp'''
class ListExps(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class ListExpsConcrete(ListExps):
  def __init__(self, exp, list_exps):
    self.exp = exp
    self.list_exp = list_exps
  def accept(self, visitor):
    return visitor.visitListExps(self)

'''declaração de exp'''
class Exp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpConcrete(Exp):
  def __init__(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitCommandExp(self)

class ExpDefFunctionConcrete(Exp):
  def __init__(self, def_function):
    self.def_function = def_function
  def accept(self, visitor):
    return visitor.visitCommandDefFunction(self)

'''declaração de expprefixo'''
class ExpPrefix(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpPrefix2(Exp):
  def __init__(self,call_function):
    self.call_function = call_function 
  def accept(self, visitor):
    return visitor.visitCommandPrefix2(self)

class ExpPrefix1(Exp):
  def __init__(self,var):
    self.var = var
  def accept(self, visitor):
    return visitor.visitCommandPrefix1(self)

'''declaração de chamdadafuncao'''
class CallFunction(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CallFunctionConcrete(CallFunction):
  def __init__(self, exp_prefix, args, name):
    self.exp_prefix = exp_prefix
    self.args = args
    self.name = name
  def accept(self, visitor):
    return visitor.visitCallFunction(self)

'''declaração de args'''
class Args(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de args'''
class ArgsConcrete(Args):
  def __init__(self, list_exps):
    self.list_exps = list_exps
  def accept(self, visitor):
    pass

'''declaração de corpofuncao'''
class BodyFunction(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class BodyFunctionConcrete(BodyFunction):
  def __init__(self, list_pars, block):
    self.list_pars = list_pars
    self.block = block
  def accept(self, visitor):
    pass

'''declaração de listapars'''
class ListPars(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listadecampos'''
class listfields(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de campo'''
class Field(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de separadordecampos'''
class SeparatorFields(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de variável local'''
class LocalVar(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de opbin'''
class OpBin(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de opunário'''
class OpUnary(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de função'''
class Function(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de função'''
class FunctionConcrete(Function):
  def __init__(self, name_function, body_function):
    self.name_function= name_function
    self.body_function = body_function
  def accept(self, visitor):
    return visitor.visitCommandFunctionConcrete(self)
  
'''declaração de if'''
class If(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class IfConcrete(If):
  def __init__(self, exp, block, else1, else_if):
    self.exp = exp
    self.block = block
    self.else1 = else1
    self.else_if = else_if
  def accept(self, visitor):
    pass

class ElseIf(If):
  def __init__(self, exp, block):
    self.exp = exp
    self.block = block
  def accept(self, visitor):
    pass

class Else(If):
  def __init__(self, block):
    self.block = block
  def accept(self, visitor):
    pass

'''declaração de while'''
class StructWhile(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StructWhileConcret(StructWhile):
  def __init__(self, exp, block):
    self.exp = exp
    self.block = block
  def accept(self, visitor):
    pass

'''declaração de for'''
class StructFor(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StructForConcret(StructFor):
  def __init__(self, exp, block):
    self.exp = exp
    self.block = block
  def accept(self, visitor):
    pass

class StructForIn(StructFor):
  def __init__(self, list_names, list_exps):
    self.list_names = list_names
    self.list_exps = list_exps
  def accept(self, visitor):
    pass

'''declaração de repeat'''
class StructRepeat(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StructRepeatConcrete(StructRepeat):
  def __init__(self, block, exp):
    self.block = block
    self.exp = exp
  def accept(self, visitor):
    pass

'''declaracao de error'''
class Error(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

