from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p
  
class Visitor(AbstractVisitor):
    def visitProgramConcrete(self, programConcrete):
      programConcrete.block.accept(self)

    def visitBlockConcrete(self, blockConcrete):
      blockConcrete.command.accept(self)
      blockConcrete.command_ret.accept(self)

  #incompleto esse
    def visitCommandCallFunction(self, commandCallFunction):
      commandCallFunction.exp_prefix.accept(self)
      commandCallFunction.args.accept(self)
      commandCallFunction.name.accept(self)

    def visitCommandStructWhile(self, commandStructWhile):
      print (blank(), 'while ', end='', sep='')
      commandStructWhile.exp.accept(self)
      print ('do', end='', sep='')
      commandStructWhile.block.accept(self)
      print ('end')

    def visitCommandStructRepeat(self, commandStructRepeat):
      print (blank(), 'repeat ', end='', sep='')
      commandStructRepeat.block.accept(self)
      print ('until ', end='' )
      commandStructRepeat.exp.accept(self)

    def visitCommandStructForIn(self, commandStructForIn):
      print (blank(), 'for ', end='', sep='')  
      commandStructForIn.list_names.accept(self)
      print ('in ', end='', sep='') 
      commandStructForIn.list_exps.accept(self)
      print ('do ', end='', sep='') 
      commandStructForIn.block.accept(self)
      print ('end')

    def visitCommandStructFor(self, commandStructFor):
      print(blank(), 'for ', end='', sep='')
      commandStructFor.name.accept(self)
      print(' = ', end='', sep='')
      commandStructFor.exp.accept(self)
      print(' == ', end='', sep='')
      commandStructFor.exp.accept(self)
      print(' do ', end='', sep='')
      commandStructFor.block.accept(self)
      print(' end ', end='', sep='')

    def visitCommandDefFunction(self, commandDefFunction):
      commandDefFunction.function.accept(self)
      commandDefFunction.local_function.accept(self)

    def visitCommandFunction(self, commandFunction):
      commandFunction.function.accept(self)
      commandFunction.name_function.accept(self)
      commandFunction.body_function.accept(self)

    def visitCommandNameFunction(self, commandName):
      commandName.name.accept(self)

    def visitCommandListvars(self, commandListvars):
      commandListvars.var.accept(self)
      commandListvars.list_vars.accept(self)

    def visitCommandVar(self, commandVar):
      commandVar.name.accept(self)
      commandVar.prefix_exp.accept(self)
      commandVar.exp.accept(self)

    def visitCommandListNames(self, commandListNames):
      commandListNames.name.accept(self)
      commandListNames.list_names.accept(self)

    def visitCommandListExps(self, commandListExps):
      commandListExps.exp.accept(self)
      commandListExps.list_exps.accept(self)
#parei aqui
    def visitCommandExpDefFunction(self, commandExpDefFunction):
      commandExpDefFunction.def_function.accept(self)

    def visitCommandExp(self, commandExp):
      commandExp.exp.accept(self)
      commandExp.exp2.accept(self)

    def visitCommandExpPrefix(self, commandExpPrefix):
      commandExpPrefix.var.accept(self)
      commandExpPrefix.exp.accept(self)

    def visitCommandCallFunction(self, commandCallFunction):
      commandCallFunction.exp_prefix.accept(self)
      commandCallFunction.args.accept(self)

    def visitCommandArgs(self, commandArgs):
      commandArgs.list_exps.accept(self)

  
    
       
