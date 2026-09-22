
#atividade 1
def par_ou_impar():

    num = int(input("Escolha um numero: "))

    if num % 2 == 0:
        print(f"O numero {num} é par")

    else:
        print(f"O numero {num} é impar")    

par_ou_impar()

#atividade 2
def verificacao_de_idade():
    old = int(input("Digite sua idade: "))

    if old >= 0 and old <= 12:
        print("Você é criança")

    elif old >= 13 and old <= 18:
        print("Você é adolescente")

    else:
        print("Você é adulto")

verificacao_de_idade()

#atividade 3 (entendi de uma forma diferente)
def nome_e_senha():
    user = input("Digite seu nome de usuario: ")
    password = input("Enter your password: ")

    if user.isalpha():
        print("Usuario valido")

    else:
        print("Usuario invalido")

nome_e_senha()    

#atividade 3
usuario_correto = "jotta"
senha_correta = "jotta123"

usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login valido")
else:
    print("Login invalido, tente novamente")



#atividade 4
def quadrantes():
    x = float(input("Digite a cordenada x: "))
    y = float(input("Digite a cordenada y: "))

    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante.")

    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante.")

    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante.")

    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante.")

    else:
        print("O ponto está sobre o eixo ou na origem.")
