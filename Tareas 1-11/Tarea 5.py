dinero_inicial = 2000
precio_helado = 100
edad = 18
hambre = edad
incremento_helado = 1.20
contador_helados = 0
dinero_final = 0

while (dinero_inicial > 0 and hambre < 85):
    hambre = hambre + edad
    print (hambre)
    precio_helado = precio_helado * incremento_helado
    dinero_inicial = dinero_inicial - (precio_helado * incremento_helado)
    contador_helados += 1

while (dinero_inicial > 0 and 85 <= hambre <= 100):
    hambre = hambre + edad
    print (hambre)
    precio_helado = precio_helado * incremento_helado
    dinero_inicial = dinero_inicial - (precio_helado * incremento_helado)
    contador_helados += 1

dinero_final = 2000 - dinero_inicial

if dinero_final < 0:
    print ("No tienes dinero suficiente para saciar tu hambre de titan")
else:
    print ("Tras ", contador_helados, " helados ya no tienes hambre, pero te has gastado ",
        round(dinero_final), "€ en helados tonto")

print (hambre)