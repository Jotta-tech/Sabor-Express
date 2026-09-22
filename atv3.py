#EXERCICIO 01
listas_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_nomes = ["João", "Maria", "Isaque", "Cleide"]
lista_de_anos = [2007, 2026]

#EXERCICIO 02
lista_de_livros = ["Biblia", "Diario de um banana", "Senhor dos anéis", "Código limpo", "Harry Potter"]
for livro in lista_de_livros:
    print(f"{livro}\n")     

#EXERCICIO 03
soma_impares = 0
for i in range (1, 11, 2):
    soma_impares += i
    print(soma_impares)

#EXERCICIO 04
for i in range (10, 0, -1):
    print(i)

#EXERCICIO 05
num = int(input("Digite um numero: "))
for i in range (1, 11, 1):
    print(num * i)
    
#EXERCICIO 06
soma = 0
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    for numero in listas_de_numeros:
        soma += numero
    print("Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EXERCICIO 07
lista_de_media = [7, 7, 7, 7]
soma = 0
try: 
    for valor in lista_de_media:
        soma += valor
    media = soma / len(lista_de_media)
    print(f"Média  dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possivel calcular a média. ")
except Exception as e:
    print(f"Ocorreu um erro: {e}") 
    