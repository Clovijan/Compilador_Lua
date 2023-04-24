from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *


class Visitor(AbstractVisitor):
    def visitProgramConcrete(self, programConcrete):
        programConcrete.block.accept(self)

    def visitBlockConcrete(self, blockConcrete):
        blockConcrete.block.accept(self)

    def visitCommandConcrete(self, commandConcrete):
        commandConcrete.command.accept(self)
        commandConcrete.command_ret.accept(self)

    def visitRotuloConcrete(self, commandConrete):
        commandConcrete.rotulo.accept(self)
