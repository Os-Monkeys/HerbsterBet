import random
#formar um caça-níquel
def rodarRoleta():
    numero = random.randint(1, 10)
    return numero

money = 500.00
simboloUm = rodarRoleta()
simboloDois = rodarRoleta()
simboloTres = rodarRoleta()











#Jackpot
if simboloUm == simboloDois and simboloUm == simboloTres:
    money += 0.50