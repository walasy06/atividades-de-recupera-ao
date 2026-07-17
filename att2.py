1) melhorar media 

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"\nMédia final: {media:.2f}")

if media >= 7.0:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")

2) melhorar imc

peso = float(input("Digite seu peso em kg : "))
altura = float(input("Digite sua altura em metros : "))
imc = peso / (altura ** 2)

f imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Peso normal )"
elif imc < 30.0:
    classificacao = "Sobrepeso"
elif imc < 35.0:
    classificacao = "Obesidade Grau 1"
elif imc < 40.0:
    classificacao = "Obesidade Grau 2"
else:
    classificacao = "Obesidade Grau 3 "

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Avaliação: {classificacao}")
