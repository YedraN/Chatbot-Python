#Módulo de búsqueda en google

from googlesearch import search

chat_buscar = '¿Qué quieres buscar?'

def buscar():
    q = input('Tú: ')
    results = search(q)
    num = 4
    lang = 'es'
    stop = num
    results = search(q, lang = lang, num = num, stop = stop)
    for r in results:
	    print(r)