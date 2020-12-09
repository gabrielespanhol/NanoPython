# coding: iso-8859-1 -*-
import getpass
from datetime import datetime

print("Usuário {}".format(getpass.getuser()))
print("Data Completa {}".format(datetime.now()))
print("Dia {}".format(datetime.now().day))
print("Mês {}".format(datetime.now().month))
print("Ano {}".format(datetime.now().year))
print("Hora {}".format(datetime.now().hour))
print("Minuto {}".format(datetime.now().minute))
print("Segundo {}".format(datetime.now().second))