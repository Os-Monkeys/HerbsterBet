import random
from flask import Flask, render_template, request, flash, url_for, session 
#formar um caça-níquel
def rodarRoleta():
    numero = random.randint(1, 10)
    return numero

money = 500.00
simboloUm = rodarRoleta()
simboloDois = rodarRoleta()
simboloTres = rodarRoleta()



print(f'[{simboloUm}][{simboloDois}][{simboloTres}]')
if simboloUm == simboloDois and simboloUm == simboloTres: #Jackpot
    adicional = 50.50
    money += adicional
elif simboloUm == simboloDois or simboloTres == simboloUm or simboloDois == simboloTres: #Dois iguais
    adicional = 5.00
    money += adicional
else: #Todos diferentes
    adicional = 0.00
    money += adicional

print(f"Você recebeu R${adicional:.2f}!!!")