# coding: iso-8859-1 -*-
import platform

print("Distribui��o do Sistema Operacional: {}".format(platform.platform()))
print("Nome do Sistema Operacional: {}".format(platform.system()))
print("Vers�o do Sistema Operacional: {}".format(platform.release()))
print("Arquitetura: {}".format(platform.architecture()))
print("Nome do Computador: {}".format(platform.node()))
print("Tipo de M�quina: {}".format(platform.machine()))
print("Processador: {}".format(platform.processor()))
print("Vers�o do Python: {}".format(platform.python_version()))