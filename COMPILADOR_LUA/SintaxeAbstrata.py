from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

''' declaração de trecho'''
class Program(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass
    
class ProgramConcrete(Program):
  def __init__(self, block):
    self.block = block
  def accept(self, visitor):
    return visitor.visitProgramConcrete(self)
  
'''declaração de bloco'''
class Block(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

class BlockConcrete(Block):
  def __init__(self, command, command_ret):
    self.command = command
    self.command_ret = command_ret
  def accept(self, visitor):
    return visitor.visitBlockConcrete(self)

'''declaração de comando'''
class Command(metaclass=ABCMeta)
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
  def __init__(self, function, local_function):
    self.function = function
    self.local_function = local_function
  def accept(self, visitor):
    return visitor.visitCommandDefFunction(self)

'''declaração de comandoret'''
class CommandRet(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

class CommandRetConcrete(CommandRet)
  def __init__(self, list_exps)
    self.list_exps = list_exps
  def accept(self, visitor):
    return visitor.visitCommandRetConcrete(self)

'''declaração de nomefunção'''
class NameFunction(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass
    
'''declaração de listvars'''
class Listvars(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de var'''
class Var(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listadenomes'''
class ListNames(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listaexp'''
class ListExps(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de exp'''
class Exp(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de expprefixo'''
class ExpPrefix(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de chamdadafuncao'''
class CallFunction(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de args'''
class Args(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de deffuncao'''
class DefFunction(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de corpofuncao'''
class BodyFunction(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listapars'''
class ListPars(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de construtortabela'''
class ConstructTable(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listadecampos'''
class listfields(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de campo'''
class Field(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de separadordecampos'''
class SeparatorFields(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de variável local'''
class LocalVar(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de opbin'''
class OpBin(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de opunário'''
class OpUnary(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de função'''
class Function(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de if'''
class If(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de while'''
class StructWhile(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de for'''
class StructFor(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de forin'''
class StructForIn(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de repeat'''
class structRepeat(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de funcaolocal'''
class LocalFunction(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaracao de error'''
class Error(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

