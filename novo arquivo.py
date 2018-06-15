# t = int(input("Qual vai ser o tamanho dessa lista: "))
#
# lista = ['']*t
# sp=0
# i=0
# peso=0
# p=0
# lista[p] = int(input("Digite valor: "))
# p=1
# while p<len(lista):
#     lista[p] = int(input("Digite valor: "))
#     peso+=1
#     sp=sp+(lista[p]*p)
#     p+=1
# print(sp/peso)

t = int(input("Qual vai ser o tamanho dessa lista: "))

lista = ['']*t
p=0
r=0
sp=0
si=0
while p<len(lista):
    lista[p] = int(input("Digite valor: "))
    p=p+1
p=0
for valor in lista:
    print("Valor amarzenado na local {} é {}".format(p,valor))
    p=p+1
