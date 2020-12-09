nome = input("Digite o nome: ")
idade = int(input("digite a idade"))
doenca_infecto = input("suspeita de doença infecto contagiosa?").upper()
# IF simples
prioridade = "NÂO"
if idade > 65:
    prioridade = "SIM"
print("o paciente " + nome + " possui atendimento prioritario? " + prioridade)

# if composto

if idade > 65:
    print("o paciente " + nome + "Possui atendimento prioriorirario")
elif doenca_infecto == "SIM":
    print("o paciente " + nome + " deve ser direcionado para a sala de espera reserva")
else:
    print("o paciente " + nome + " não possui atendimento prioritario")

print("--------------------------------------------")

if idade >= 65 and doenca_infecto == "SIM":
    print("paciente direcionado para a sala amarela - com prioridade")
elif idade < 65 and doenca_infecto == "SIM":
    print("paciente direcionado para a sala amarela - prioridade")
elif idade >= 65 and doenca_infecto == "NAO":
    print("paciente direcionado para a sala branca - com prioridade")
elif idade < 65 and doenca_infecto == "NAO":
    print("paciente direcionado para a sala branca - sem prioridade")
else:
    print("Resposta a suspeita de doença infecto sem SIM ou NAO")
