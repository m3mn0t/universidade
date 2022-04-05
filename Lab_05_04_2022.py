file1 = open("/media/m3mn0t/Data1.5TB/Dev/Qt projects/test/untitled/chave a encriptar.txt", "r+")
texto: str

texto = file1.read()
print("Chave a encriptar -->         ", texto, "\n")
print("total de caracteres -->         ", len(texto), "Temos de somar mais 1 e dividir por 5, sabe se quantas listas")
texto1 = list(texto)
#print(texto1)


lista1 = (texto1[:5])
print(lista1)
lista2 = (texto1[5:10])
print(lista2)
lista3 = (texto1[10:15])
print(lista3)
lista4 = (texto1[15:20])
print(lista4)
lista5 = (texto1[20:25])
print(lista5)

lista6 = (texto1[25:30])
if lista6[3] == "\n":
    lista6[3]= " "
while len(lista6) != 5:
    lista6.append(" ")

print(lista6)

final1 = str(lista1[0] + lista2[0] + lista3[0] + lista4[0] + lista5[0] + lista6[0])
final2 = str(lista1[1] + lista2[1] + lista3[1] + lista4[1] + lista5[1] + lista6[1])
final3 = str(lista1[2] + lista2[2] + lista3[2] + lista4[2] + lista5[2] + lista6[2])
final4 = str(lista1[3] + lista2[3] + lista3[3] + lista4[3] + lista5[3] + lista6[3])
final5 = str(lista1[4] + lista2[4] + lista3[4] + lista4[4] + lista5[4] + lista6[4])

print (final1, final2, final3, final4, final5)








file1.close()
