class UsuarioException(Exception):
    """Classe base para exceções relacionadas ao usuário."""
    pass

class ArquivoNaoEncontradoException(UsuarioException):
    """Exceção para quando o arquivo de usuários não é encontrado."""
    def __init__(self):
        super().__init__("O arquivo de usuários não foi encontrado. Verifique se o caminho está correto.")

class UsuarioInvalidoException(UsuarioException):
    """Exceção para quando o índice do usuário é inválido."""
    def __init__(self):
        super().__init__("Índice de usuário inválido. Escolha um número válido.")

class ErroDeDecodificacaoException(UsuarioException):
    """Exceção para erro ao decodificar o JSON do arquivo de usuários."""
    def __init__(self):
        super().__init__("Erro ao decodificar o arquivo JSON. Verifique se o arquivo está corrompido.")

class EntradaInvalidaException(UsuarioException):
    """Exceção para quando a entrada do usuário é inválida (não é um número)."""
    def __init__(self):
        super().__init__("Entrada inválida. Por favor, digite um número.")


