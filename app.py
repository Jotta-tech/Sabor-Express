import os

restaurantes = ["Pizza", "Sushi"]


def exibir_nome_do_programa():
    print("""
Sabor Express
""")


def exibir_opcoes():
    print("1. Cadastrar retaurante")
    print("2. Listar retaurante")
    print("3. Ativar retaurante")
    print("4. Sair")


def finalizar_app():
    exibir_subtitulo("Finalizando app")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastrar novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n ")
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    for restaurante in restaurantes:
        print(f".{restaurante}")

    voltar_ao_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolha = int(input("Escolha uma opção: ")) 

        if opcao_escolha == 1: 
            cadastrar_novo_restaurante()

        elif opcao_escolha == 2:
            listar_restaurantes()

        elif opcao_escolha == 3:
            print("Ativar restaurante")

        elif opcao_escolha == 3:
                finalizar_app()
        else:
            opcao_invalida() 
    except:
        opcao_invalida()


def main():
    os.system("cls")
    print(exibir_nome_do_programa)    
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()


