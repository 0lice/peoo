from models.cidade import Cidade, Cidades
from models.usuario import Usuario, Usuarios
from models.representante import Representante, Representantes
from models.banda import Banda, Bandas
from models.apresentacao import Apresentacao, Apresentacoes
from models.cidade import Cidade, Cidades
from datetime import datetime

_bandas = Bandas("bandas.json")
_usuarios = Usuarios("usuarios.json")
_representantes = Representantes("representantes.json")
_apresentacoes = Apresentacoes("apresentacoes.json")
_cidades = Cidades("cidades.json")

class View:
    @staticmethod
    def usuario_inserir(nome: str, email: str, senha: str):
        usuario = Usuario(0, nome, email, senha)
        _usuarios.inserir(usuario)

    @staticmethod
    def usuario_listar():
        return _usuarios.listar()

    @staticmethod
    def usuario_listar_id(id_usuario: int):
        return _usuarios.listar_id(id_usuario)

    @staticmethod
    def usuario_atualizar(id_usuario: int, novos_dados: dict):
        _usuarios.atualizar(id_usuario, novos_dados)

    @staticmethod
    def usuario_excluir(id_usuario: int):
        _usuarios.excluir(id_usuario)

    @staticmethod
    def representante_inserir(nome: str, email: str, senha: str, telefone: str):
        representante = Representante(0, nome, email, senha, telefone)
        _representantes.inserir(representante)

    @staticmethod
    def representante_listar():
        return _representantes.listar()

    @staticmethod
    def representante_listar_id(id_rep: int):
        return _representantes.listar_id(id_rep)

    @staticmethod
    def representante_atualizar(id_rep: int, novos_dados: dict):
        _representantes.atualizar(id_rep, novos_dados)

    @staticmethod
    def representante_excluir(id_rep: int):
        _representantes.excluir(id_rep)

    @staticmethod
    def banda_inserir(id_representante: int, nome: str, gravadora: str, genero: str, email: str, senha: str, tel: str):
        banda = Banda(0, id_representante, nome, gravadora, genero, email, senha, tel)
        _bandas.inserir(banda)

    @staticmethod
    def banda_listar():
        return _bandas.listar()

    @staticmethod
    def banda_listar_id(id_banda: int):
        return _bandas.listar_id(id_banda)

    @staticmethod
    def banda_atualizar(id_banda: int, novos_dados: dict):
        _bandas.atualizar(id_banda, novos_dados)

    @staticmethod
    def banda_excluir(id_banda: int):
        _bandas.excluir(id_banda)

    @staticmethod
    def representante_inserir(nome: str, email: str, senha: str, telefone: str):
        representante = Representante(0, nome, email, senha, telefone)
        _representantes.inserir(representante)

    @staticmethod
    def representante_listar():
        return _representantes.listar()

    @staticmethod
    def representante_listar_id(id_rep: int):
        return _representantes.listar_id(id_rep)

    @staticmethod
    def representante_atualizar(id_rep: int, novos_dados: dict):
        _representantes.atualizar(id_rep, novos_dados)

    @staticmethod
    def representante_excluir(id_rep: int):
        _representantes.excluir(id_rep)

    @staticmethod
    def apresentacao_inserir(id_banda: int, data: datetime, local: str, confirmado: bool = False):
        apresentacao = Apresentacao(0, id_banda, data, local, confirmado)
        _apresentacoes.inserir(apresentacao)

    @staticmethod
    def apresentacao_listar():
        return _apresentacoes.listar()

    @staticmethod
    def apresentacao_listar_id(id_apresentacao: int):
        return _apresentacoes.listar_id(id_apresentacao)

    @staticmethod
    def apresentacao_atualizar(id_apresentacao: int, novos_dados: dict):
        _apresentacoes.atualizar(id_apresentacao, novos_dados)

    @staticmethod
    def apresentacao_excluir(id_apresentacao: int):
        _apresentacoes.excluir(id_apresentacao)

    @staticmethod
    def cidade_inserir(nome: str, local_show: str, estado: str):
        cidade = Cidade(0, nome, local_show, estado)
        _cidades.inserir(cidade)

    @staticmethod
    def cidade_listar():
        return _cidades.listar()

    @staticmethod
    def cidade_listar_id(id_cidade: int):
        return _cidades.listar_id(id_cidade)

    @staticmethod
    def cidade_atualizar(id_cidade: int, nome: str, local_show: str, estado: str):
        novos_dados = {"nome": nome, "local_show": local_show, "estado": estado}
        _cidades.atualizar(id_cidade, novos_dados)

    @staticmethod
    def cidade_excluir(id_cidade: int):
        _cidades.excluir(id_cidade)

