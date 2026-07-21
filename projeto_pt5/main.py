from models.usuarioSistema import UsuarioSistema
from exceptions.usuario_exceptions import *

def menu():
    sistema = UsuarioSistema()

    opcao = 0
    while opcao != 6:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Usuário")
        print("2 - Ler Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - recuperar usuario deletado")
        print("6 - Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        try:
            if opcao == 1:
                sistema.create()
            elif opcao == 2:
                sistema.read()
            elif opcao == 3:
                sistema.update()
            elif opcao == 4:
                sistema.delete()
            elif opcao == 5:
                sistema.recuperar_usuarios_deletados()
            elif opcao == 6:
                print("Encerrando o sistema.")
            else:
                print("Opção inválida. Tente novamente.")
        except (ArquivoNaoEncontradoException, UsuarioInvalidoException,
                ErroDeDecodificacaoException, EntradaInvalidaException) as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu()

