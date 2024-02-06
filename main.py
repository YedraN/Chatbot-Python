### Chatbot en Python ###

#Módulos
import random
from Módulos import saludos as sal
from Módulos import buscar as bus
from Módulos import respuestas as res

#Variables
ejecutando = True
chat = 'Chat:'
respuesta = ''

#Bucle principal
while ejecutando:
    print(chat, random.choice(sal.saludos))
    respuesta = input('Tú: ')
    if 'buscar' in respuesta:
        print(chat, bus.chat_buscar)
        bus.buscar()
        print('')
        print(chat, '¿Estás contento con los resultados?')
        respuesta = input('Tú: ')
        if respuesta == 'Si' or 'si':
            print(chat, 'Perfecto!!')
        else:
            print(chat, 'Disculpame, si quieres que genere nuevos vuelve a pedirme que busque')
    else:
        continue
    input()