# coding: iso-8859-1 -*-
import platform

print("Distribuição do Sistema Operacional: {}".format(platform.platform()))
print("Nome do Sistema Operacional: {}".format(platform.system()))
print("Versão do Sistema Operacional: {}".format(platform.release()))
print("Arquitetura: {}".format(platform.architecture()))
print("Nome do Computador: {}".format(platform.node()))
print("Tipo de Máquina: {}".format(platform.machine()))
print("Processador: {}".format(platform.processor()))
print("Versão do Python: {}".format(platform.python_version()))