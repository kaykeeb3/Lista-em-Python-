# Copiar lista em Python:

lista_a = ["Kayke", "Pedro", "Marcos", "Lara"]
lista_b = lista_a

lista_b.append("Bira")
print(lista_a)
print(lista_b)

texto_a = "Lira"
texto_b = texto_a
texto_b = texto_b.replace("L", "B")
print(texto_a)
print(texto_b)

# 2 formas 
lista_c = lista_a.copy()
lista_c.append("Feijão")
print(lista_a)
print(lista_c)

# Para lista de lista, temos que pensar diferente.
produtos =  [
    ["Ipad", 4000],
    ["Iphone", 7900],
 ]
 
 produtos2 = produtos[:]
 produtos2[0] [1] = 6000
 print(produtos)
 print(produtos2)
 
  # Solução é um deepcopy
import copy
produtos3 = copy.deepcopy(produtos)
produtos3[0] [1] = 6000
print(produtos)
print(produtos3)

