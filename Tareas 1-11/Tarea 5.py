dinero_inicial = 2000
precio_helado = 100
edad = 89
hambre = edad
incremento_helado = 1.20
contador_helados = 0


if 85 <= hambre <= 100:
    print ("Eres demasiado mayor para comer helado")


while (dinero_inicial > 0 and hambre < 85):
    hambre += edad
    precio_helado *= incremento_helado
    dinero_inicial -= precio_helado * incremento_helado
    contador_helados += 1


if dinero_inicial < 0:
    print ("No tienes dinero suficiente para saciar tu hambre de titan")
else:
    print ("Tras ", contador_helados, " helados ya no tienes hambre, pero solo te quedan ",
        round(dinero_inicial), "€")