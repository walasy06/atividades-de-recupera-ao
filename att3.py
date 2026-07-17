1) Faça um programa que recebe uma senha e enquanto ela não for igual a "12345", ele imprime "Tente novamente".
Quando a senha estiver correta, o programa encerra imprimindo "Acesso liberado".

senha = input("Digite a senha: ")
while senha != "12345":
    print("Tente novamente")
  
    senha = input("Digite a senha: ")
print("Acesso liberado")

2) Faça um programa que recebe dez números inteiros positivos e diz quantos números pares foram informados.

total_pares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro positivo: "))
    
  if numero > 0 and numero % 2 == 0:
        total_pares += 1

print(f"\nQuantidade de números pares informados: {total_pares}")
