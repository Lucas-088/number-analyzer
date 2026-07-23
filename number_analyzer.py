lista=[]

while True:
 n1=int(input ("Digite um numero :"))
 if n1== 0 :
   break
 lista.append(n1)

print("Números digitados :", lista)
print("Quantidade de números digitados :",len(lista))
print("Média :", sum(lista) / len(lista)) 


