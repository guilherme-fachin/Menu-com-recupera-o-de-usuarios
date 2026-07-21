import os
import json
from exceptions.usuario_exceptions import *
import datetime

class UsuarioSistema:                                                                        #      
    def __init__(self):                                                                      #
        self.arquivo = 'projeto_pt5/dados/usuarios.json'  # Caminho para o arquivo JSON      # essas parte sao para chamr o arquivo e o sistema funcionar, elas sao responsaveis por ve(caminho) se o arquivo existe e se nao existe cria
        self.criar_arquivo()  # Garante que o arquivo exista                                 #
        self.usuarios = self.ler_usuarios()  # Carrega usuários do arquivo                   #
        ###
        self.arquivo_deletados = 'projeto_pt5/dados/usuarios_deletados.json'       #esses dois fazem a 
        self.criar_arquivo_deletados()                                              #mesma coisa que em cima(so q e responsavel por salvar em uma pasta separada os usuarios deletados)
        ###

    def criar_arquivo(self):
        # Cria a pasta 'dados' se não existir
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)       
        # Cria o arquivo se não existir
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                json.dump([], f)  # Inicializa o arquivo como uma lista vazia

    def ler_usuarios(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:  # Tratamento para arquivo não encontrado
            raise ArquivoNaoEncontradoException()  # Lança exceção personalizada
        except json.JSONDecodeError:  # Tratamento para erro de decodificação JSON
            raise ErroDeDecodificacaoException()  # Lança exceção personalizada
    
    def create(self):
        novo_usuario = input("Digite o nome do novo usuário: ")
        self.usuarios.append(novo_usuario)
        self.salvar_usuarios()  # Salva a lista atualizada no arquivo
        print(f"Usuário {novo_usuario} cadastrado com sucesso!")

    def read(self):
        print("Usuários cadastrados:")
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario}")

    def update(self):
        self.read()  # Exibe a lista de usuários
        try:
            indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
            if 0 <= indice < len(self.usuarios):
                novo_nome = input(f"Digite o novo nome para {self.usuarios[indice]}: ")
                self.usuarios[indice] = novo_nome
                self.salvar_usuarios()  # Salva as alterações
                print(f"Usuário atualizado para {novo_nome} com sucesso!")
            else:
                raise UsuarioInvalidoException()
        except ValueError:  # Tratamento para entrada inválida
            raise EntradaInvalidaException()  # Lança exceção personalizada

    def delete(self):
        self.read()  # Exibe a lista de usuários
        try:
            indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
            if 0 <= indice < len(self.usuarios):
                removido = self.usuarios.pop(indice)
                self.salvar_usuarios()  # Salva as alterações
                self.salvar_usuario_deletado(removido) #salva o usuario                
                print(f"Usuário {removido} excluído com sucesso!")
            else:
                raise UsuarioInvalidoException()
        except ValueError:  # Tratamento para entrada inválida
            raise EntradaInvalidaException()  # Lança exceção personalizada
            
    def salvar_usuarios(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.usuarios, f, ensure_ascii=False )  # Salva a lista de usuários no arquivo

    def criar_arquivo_deletados(self):
        # cria a pasta 'dados' se nao existir
        os.makedirs(os.path.dirname(self.arquivo_deletados), exist_ok=True)
        #cria o arquivo de deletados se nao existir
        if not os.path.exists(self.arquivo_deletados):#atenção tinha erro no "os.path.exists" em ves do exists estava dirname e se for o driname ekle n funciuona pq ele acha q o arquivo vai estar sempre ja criado poius esta sempre verdadeiro, e se o arwuivo n existir ele n consegue criar nem abrir, se for o exists ele consegue destinguir e criar caso n existir
            with open(self.arquivo_deletados, 'w', encoding='utf-8') as f:
                json.dump([], f) #inicializa o arquivo como uma lista vazia


#meu cod:

    def salvar_usuario_deletado(self, usuario):
        data_exclusao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        usuario_deletado = {
            "nome": usuario,
            "data_exclusao": data_exclusao
        }
        #carrega usuarios deletados de arquivo
        with open(self.arquivo_deletados, 'r', encoding='utf-8') as f:
            usuarios_deletados = json.load(f)
        
        #adiciona o novo usuario deletado e salva de volta no arquivo
        usuarios_deletados.append(usuario_deletado)
        with open(self.arquivo_deletados, 'w', encoding='utf-8') as f:
            json.dump(usuarios_deletados, f, ensure_ascii=False)
    
    def recuperar_usuarios_deletados(self):
        try:
            #carrega usuarios deletados do arquivo
            with open(self.arquivo_deletados, 'r', encoding='utf-8') as f:
                usuarios_deletados = json.load(f)
                
            if not usuarios_deletados:
                print("nenhum usuarios para recuperar.")
                return
            
            print("usuarios deletados disponiveis para recuperação:")
            
            for i, usuario in enumerate(usuarios_deletados, start=1):
                print(f"{i}. Nome: {usuario['nome']}, data de exclusao: {usuario['data_exclusao']}")
            indice = int(input("digite o numero do usuario que deseja recuperar: ")) - 1
            
            if 0 <= indice < len(usuarios_deletados):
                usuario_recuperado = usuarios_deletados.pop(indice)
                self.usuarios.append(usuario_recuperado["nome"])
                self.salvar_usuarios() #salva os usuarios ativos atualizados
                #atualiza o arquivo de usuarios deletados:
                with open(self.arquivo_deletados, 'w', encoding='utf-8') as f:
                    json.dump(usuarios_deletados, f, ensure_ascii=False)
                print(f"usuarios{usuario_recuperado['nome']} recuperado com sucesso!")
            else:
                raise UsuarioInvalidoException()
        except ValueError:
            raise EntradaInvalidaException()
        