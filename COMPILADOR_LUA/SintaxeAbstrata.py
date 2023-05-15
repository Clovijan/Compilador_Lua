from abc import abstractmethod
from abc import ABCMeta

''' declaração de program'''
class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ProgramConcrete(Program):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        return Visitor.visitProgramConcrete(self)

class ProgramConcrete2(Program):
    def __init__(self, function):
        self.function = function
    def accept(self, visitor):
        return Visitor.visitProgramConcrete2(self)


'''declaração de bloco'''
class Block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BlockConcrete(Block):
    def __init__(self, command):
        self.command = command
    def accept(self, visitor):
        return Visitor.visitBlockConcrete(self)


class BlockConcrete2(Block):
    def __init__(self, command, block):
        self.command = command
        self.block = block
    def accept(self, visitor):
        return Visitor.visitBlockConcrete2(self)


'''declaração de comando'''
class Command(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class CommandAtrib(Command):
    def __init__(self, list_var, list_exps):
        self.list_var = list_var
        self.list_exps = list_exps
    def accept(self, visitor):
        return Visitor.visitCommandAtrib(self)


class CommandCallFunction(Command):
    def __init__(self, call_function):
        self.call_function = call_function
    def accept(self, visitor):
        return Visitor.visitCommandCallFunction(self)


class CommandRotulo(Command):
    def __init__(self, rotulo):
        self.rotulo = rotulo
    def accept(self, visitor):
        return Visitor.visitCommandRotulo(self)


# Verificar se esse BREAK precisa ser chamado
class CommandBreak(Command):
    def __init__(self, BREAK):
        self.BREAK = BREAK
    def accept(self, visitor):
        return Visitor.visitCommandBreak(self)


class CommandDoBrlockEnd(Command):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandDoBlockEnd(self)


# aguardando validação dos membros do grupo
# class CommandStructWhile(Command):
#     def __init__(self, struct_while):
#         self.struct_while = struct_while

#     def accept(self, visitor):
#         return Visitor.visitCommandStructWhile(self)


class CommandStructWhile(Command):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandStructWhile(self)


# aguardando validação do grupo
# class CommandStructRepeat(Command):
#     def __init__(self, struct_repeat):
#         self.struct_repeat = struct_repeat

#     def accept(self, visitor):
#         return Visitor.visitCommandStructRepeat(self)


class CommandStructRepeat(Command):
    def __init__(self, block, exp):
        self.block = block
        self.exp = exp
    def accept(self, visitor):
        return Visitor.visitCommandStructRepeat(self)


class CommandIf(Command):
    def __init__(self, IF):
        self.IF = IF
    def accept(self, visitor):
        return Visitor.visitCommandIf(self)


class CommandStructForIn(Command):
    def __init__(self, list_names, list_exps, block):
        self.list_names = list_names
        self.list_exps = list_exps
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandStructForIn(self)


# aguardando validação dos membros do grupo
# class CommandStructFor(Command):
#     def __init__(self, struct_for):
#         self.struct_for = struct_for

#     def accept(self, visitor):
#         return Visitor.visitCommandStructFor(self)


class CommandStructFor(Command):
    def __init__(self, name, exp, exp2, block):
        self.name = name
        self.exp = exp
        self.exp2 = exp
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandStructFor(self)


class CommandDefFunction(Command):
    def __init__(self, function):
        self.function = function
    def accept(self, visitor):
        return Visitor.visitCommandDefFunction(self)


class CommandLocalListVarsAtribListExps(Command):
    def __init__(self, list_vars, list_exps, command_ret):
        self.list_vars = list_vars
        self.list_exps = list_exps
        self.command_ret = command_ret
    def accept(self, visitor):
        return Visitor.visitCommandLocalListVarsAtribListExps(self)


'''declaração de comandoret'''
class CommandRet(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class CommandRetConcrete(CommandRet):
    def __init__(self, list_exps):
        self.list_exps = list_exps
    def accept(self, visitor):
        return Visitor.visitCommandRet2(self)


'''declaração de rótulo'''
class Rotulo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

    def ExpRotulo(Rotulo):
        def __init__(self, dualcolon1, name, dualcolon2):
            self.dualcolon1 = dualcolon1
            self.name = name
            self.dualcolon2 = dualcolon2
        def accept(self, visitor):
            return Visitor.visitExpRotulo(self)


'''declaração de nomefunção'''
class NameFunction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

    def ExpNameFunction1(NameFunction):
        def __init__(self, name):
            self.name = name
        def accept(self, visitor):
            return Visitor.visitExpNameFunction1(self)

    def ExpNameFunction2(NameFunction):
        def __init__(self, name):
            self.name = name
        def accept(self, visitor):
            return Visitor.visitExpNameFunction2(self)


# '''declaração de nomefunção'''

# class NameFunctionConcrete(NameFunction):
#     def __init__(self, name):
#         self.name = name

#     def accept(self, visitor):
#         return Visitor.visitCommandNameFunction(self)
'''declaração de listvars'''
class ListVars(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ListvarsConcrete1(ListVars):
    def __init__(self, var, list_vars):
        self.var = var
    def accept(self, visitor):
        return Visitor.visitCommandListvars1(self)


class ListvarsConcrete2(ListVars):
    def __init__(self, var, list_vars):
        self.var = var
        self.list_vars = list_vars
    def accept(self, visitor):
        return Visitor.visitCommandListvars2(self)


'''declaração de var'''
class Var(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class VarConcrete1(Var):
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        return Visitor.visitCommandVar1(self)


class VarConcrete2(Var):
    def __init__(self, prefix_exp, exp):
        self.prefix_exp = prefix_exp
        self.exp = exp
    def accept(self, visitor):
        return Visitor.visitCommandVar2(self)


'''declaração de listadenomes'''
class ListNames(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ListNamesConcrete1(ListNames):
    def __init__(self, list_names, name):
        self.list_names = list_names
        self.name = name
    def accept(self, visitor):
        return Visitor.visitListNamesConcrete1(self)


class ListNamesConcrete2(ListNames):
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        return Visitor.visitListNamesConcrete2(self)


'''declaração de listaexp'''
class ListExps(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ListExpsConcrete1(ListExps):
    def __init__(self, exp, list_exps):
        self.exp = exp
        self.list_exp = list_exps
    def accept(self, visitor):
        return Visitor.visitListExpsConcrete1(self)


class ListExpsConcrete2(ListExps):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return Visitor.visitListExpsConcrete2(self)


'''declaração de exp'''
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpNil(Exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return Visitor.visitCommandExp(self)


class ExpPrefixExp(Exp):
    def __init__(self, prefix_exp):
        self.prefix_exp = prefix_exp

    def accept(self, visitor):
        return Visitor.visitCommandExpPrefixExp(self)


class ExpTag(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return Visitor.visitCommandTag(self)


class ExpMinus(Exp):
    def __init__(self, exp, exp2):
        self.exp = exp
        self.exp2 = exp2
    def accept(self, visitor):
        return Visitor.visitCommandMinus(self)


class ExpNot(Exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return Visitor.visitCommandNot(self)


class ExpPlus(Exp):
    def __init__(self, exp, exp2):
        self.exp = exp
        self.exp2 = exp2

    def accept(self, visitor):
        return Visitor.visitCommandPlus(self)


class ExpDivide(Exp):
    def __init__(self, exp, exp2):
        self.exp = exp
        self.exp2 = exp2

    def accept(self, visitor):
        return Visitor.visitCommandDivide(self)


class ExpExpo(Exp):
    def __init__(self, exp, exp2):
        self.exp = exp
        self.exp2 = exp2

    def accept(self, visitor):
        return Visitor.visitCommandExpo(self)


class ExpDefFunctionConcrete(Exp):
    def __init__(self, def_function):
        self.def_function = def_function
    def accept(self, visitor):
        return Visitor.visitCommandDefFunction(self)

class ExpBool(Exp):
    def __init__(self, boolean):
        self.boolean = boolean
    def accept(self, visitor):
        return Visitor.visitBooleanExp(self)


# aqui a passagem de parâmetro está incorreta, ExpPrefix2(ExpPrefix)
'''declaração de expprefixo'''
class ExpPrefix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class PrefixExpVar(ExpPrefix):
    def __init__(self, var):
        self.var = var

    def accept(self, visitor):
        return Visitor.visitPrefixExpVar(self)


class PrefixExpCallFunction(ExpPrefix):
    def __init__(self, call_function):
        self.call_function = call_function

    def accept(self, visitor):
        return Visitor.visitPrefixExpCallFunction(self)


'''declaração de chamdadafuncao'''
class CallFunction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class CallFunctionConcrete(CallFunction):
    def __init__(self, exp_prefix, args):
        self.exp_prefix = exp_prefix
        self.args = args

    def accept(self, visitor):
        return Visitor.visitCallFunctionConcrete(self)


'''declaração de args'''
class Args(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpArgs1(Args):
    def __init__(self, list_exps):
        self.list_exps = list_exps

    def accep(self, visitor):
        return Visitor.visitExpArgs1(self)


'''declaração de args'''
class ArgsConcrete(Args):
    def __init__(self, list_exps):
        self.list_exps = list_exps
    def accept(self, visitor):
        return Visitor.visitExpArgs(self)

class ArgsConcrete2(Args):
    def accept(self, visitor):
       return Visitor.visitExpArgs2(self)

''''declaração de corpofuncao'''
class BodyFunction(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class BodyFunctionConcrete(BodyFunction):
    def __init__(self, list_pars, block):
        self.list_pars = list_pars
        self.block = block
    def accept(self, visitor):
        return Visitor.visitBodyFunction(self)


'''declaração de listapars'''
class ListPars(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ListPars(ListPars):
    def __init__(self, list_names):
        self.list_names = list_names
    def accept(self, visitor):
        return Visitor.visitCommandListPars(self)

class ListPars2(ListPars):
    def __init__(self, list_names, varargs):
        self.list_names = list_names
        self.varargs = varargs
    def accept(self, visitor):
        return Visitor.visitCommandListPars2(self)

class ListPars3(ListPars):
    def __init__(self, varargs):
        self.varargs = varargs
    def accept(self, visitor):
        return Visitor.visitCommandListPars3(self)

'''declaração de listadecampos'''
class Listfields(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Listfields(Listfields):
    def __init__(self, field):
        self.field = field
    def accept(self, visitor):
        return Visitor.visitCommandListFields(self)

class Listfields2(Listfields):
    def __init__(self, field, separator_fields,list_fields):
        self.field = field
        self.separator_fields = separator_fields
        self.list_fields = list_fields
    def accept(self, visitor):
        return Visitor.visitCommandListFields2(self)

class Listfields3(Listfields):
    def __init__(self, field_empty):
        self.field_empty = field_empty
    def accept(self, visitor):
        return Visitor.visitCommandListFields3(self)

class Listfields4(Listfields):
    def __init__(self, field_empty, separator_fields, list_fields):
        self.field_empty = field_empty
        self.separator_fields = separator_fields
        self.list_fields = list_fields
    def accept(self, visitor):
        return Visitor.visitCommandListFields4(self)

'''declaração de campo'''
class FieldEmpty(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FieldEmptyConcrete(FieldEmpty):
    def __init__(self, field_empty):
        self.field_empty = field_empty
    def accept(self, visitor):
        return Visitor.visitCommandListFieldEmpty(self)

'''declaração de separadordecampos'''


class SeparatorFields(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SeparatorFieldsConcrete(SeparatorFields):
    def accept(self, visitor):
        return Visitor.visitCommandSeparatorFields(self)

class SeparatorFieldsConcrete2(SeparatorFields):
    def accept(self, visitor):
        return Visitor.visitCommandSeparatorFields2(self)

'''declaração de variável local'''
class LocalVar(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
      
class LocalVarConcrete(LocalVar):
    def __init__(self, list_names, list_exps):
        self.list_names = name_function
        self.list_exps = list_exps
    def accept(self, visitor):
        return visitor.visitCommandLocalVar(self)

class LocalVarConcrete2(LocalVar):
    def __init__(self, list_names):
        self.list_names = list_names
    def accept(self, visitor):
        return visitor.visitCommandLocalVar2(self)

class LocalVarConcrete3(LocalVar):
    def __init__(self, list_names):
        self.list_names = list_names
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitCommandLocalVar3(self)

'''declaração de função'''
class Function(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

'''declaração de função'''
class FunctionConcrete(Function):
    def __init__(self, name_function, body_function):
        self.name_function = name_function
        self.body_function = body_function
    def accept(self, visitor):
        return visitor.visitCommandFunction(self)


'''declaração de if'''
class If(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IfConcrete(If):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandIf(self)

class IfConcrete2(If):
    def __init__(self, exp, block, else1):
        self.exp = exp
        self.block = block
        self.else1 = else1
    def accept(self, visitor):
        return Visitor.visitCommandIf2(self)

class IfConcrete3(If):
    def __init__(self, exp, block, else1, else_if):
        self.exp = exp
        self.block = block
        self.else1 = else1
        self.else_if = else_if
    def accept(self, visitor):
        return Visitor.visitCommandIf3(self)

class ElseIf(If):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandElseIf(self)

class ElseIf2(If):
    def __init__(self, exp, block, else_if):
        self.exp = exp
        self.block = block
        self.else_if = else_if
    def accept(self, visitor):
        return Visitor.visitCommandElseIf2(self)

class Else(If):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        return Visitor.visitCommandElse(self)


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
        return Visitor.visitCommandStructWhile(self)


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
        return Visitor.visitCommandStructFor(self)


class StructForIn(StructFor):
    def __init__(self, list_names, list_exps):
        self.list_names = list_names
        self.list_exps = list_exps

    def accept(self, visitor):
        return Visitor.visitCommandStructForIn(self)


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
        return Visitor.visitCommandStructRepeat(self)


'''declaracao de error'''


class Error(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
