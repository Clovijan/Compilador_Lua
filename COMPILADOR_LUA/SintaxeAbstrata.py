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
  def __init__(self, call_function):
    self.call_function = call_function
  def accept(self, visitor):
    pass

class CommandRotulo(Command):
  def __init__(self, rotulo):
    self.rotulo = call_function
  def accept(self, visitor):
    pass

class CommandStructWhile(Command):
  def __init__(self, struct_while):
    self.struct_while = struct_while
  def accept(self, visitor):
    pass

'''declaração de comandoret'''
class Command_Ret(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de rótulo'''
class Rotulo(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de nomefunção'''
class Name_Function(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass
    
'''declaração de listvars'''
class List_vars(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de var'''
class Var(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listadenomes'''
class List_Names(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listaexp'''
class List_Exps(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de exp'''
class Exp(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de expprefixo'''
class Exp_Prefix(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de chamdadafuncao'''
class Call_Function(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de args'''
class Args(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de deffuncao'''
class Def_Function(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de corpofuncao'''
class Body_Function(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listapars'''
class List_Pars(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de construtortabela'''
class Construct_Table(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de listadecampos'''
class list_fields(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de campo'''
class Field(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de separadordecampos'''
class Separator_Fields(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de variável local'''
class Local_Var(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de opbin'''
class Op_Bin(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de opunário'''
class Op_Unary(metaclass=ABCMeta)
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
class Struct_While(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de for'''
class Struct_For(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de forin'''
class Struct_For_In(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de repeat'''
class struct_repeat(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaração de funcaolocal'''
class Local_Function(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

'''declaracao de error'''
class Error(metaclass=ABCMeta)
  @abstractmethod
  def accept(self, visitor):
    pass

