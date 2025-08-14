secret_number = 777

secret_number = int(input("Digite o número:\n"))

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

while secret_number != 777:
    print("O número está incorreto! Tente novamente: ", secret_number)