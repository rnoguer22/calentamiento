for i in range (51):
    print (i)



import random
hambre = random.randint(1,100)

dinero_inicial = 2000
precio_helado = 100
contador_helados = 0
while hambre < 85:
    hambre += hambre
    precio_helado *= 1.20
    contador_helados += 1
    if 85 < hambre < 100:
        print ("Tras ", contador_helados, " y con ", precio_helado, " menos en el bolsillo, no queda hambre")