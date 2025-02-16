import re
import json
from models.persistencia import Persistencia

class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
    
    @property
    def id_user(self):
        return self.__id
    
    @id_user.setter
    def user_id(self, novo_id):
        if isinstance(novo_id, int):
            self.__id = novo_id
        else:
            raise ValueError('Id inválido. O id deve ser um número inteiro.')
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise ValueError('Nome inválido. O nome deve ser um texto.')
        elif not (3 <= len(novo_nome) <= 100):
            raise ValueError('O nome da banda deve ter, no mínimo, 3 caracteres e, no máximo, 100 caracteres.')
        else:
            self.__nome = novo_nome

    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, novo_email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(padrao, novo_email): 
            self.__email = novo_email
        else:
            raise ValueError('E-mail inválido. Verifique o formato: exemplo@dominio.com')
    
    @property
    def senha(self):
        return self.__senha
        
    @senha.setter
    def senha(self, nova_senha):
        if nova_senha.replace(' ', '').isalpha():
            raise ValueError("A senha deve conter um número ou caractere especial.")
        self.__senha = nova_senha

    def to_dict(self):
        return {"id": self.__id, "nome": self.__nome, "email": self.__email, "senha": self.__senha}

    def __str__(self):
        return f"Usuário {self.id}: {self.nome} ({self.email})"
    
class Usuarios(Persistencia):
    def inserir(self, usuario: Usuario):
        usuarios = self.abrir()
        usuarios.append(usuario.to_dict())
        self.salvar(usuarios)

    def listar(self):
        return self.abrir()

    def listar_id(self, id_usuario: int):
        usuarios = self.abrir()
        for u in usuarios:
            if u['id'] == id_usuario:
                return u
        return None

    def atualizar(self, id_usuario: int, novos_dados: dict):
        usuarios = self.abrir()
        for u in usuarios:
            if u['id'] == id_usuario:
                u.update(novos_dados)
        self.salvar(usuarios)

    def excluir(self, id_usuario: int):
        usuarios = self.abrir()
        usuarios = [u for u in usuarios if u['id'] != id_usuario]
        self.salvar(usuarios)
