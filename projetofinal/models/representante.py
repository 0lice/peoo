from usuario import Usuario
from persistencia import Persistencia
import re

class Representante(Usuario):
    def __init__(self, id: int, nome: str, email: str, senha: str, telefone: str):
        super().__init__(id, nome, email, senha)
        self.telefone = telefone

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        padrao = r'^\(\d{2}\)\s?9\d{4}-\d{4}$|^\(\d{2}\)\s?\d{4}-\d{4}$'
        if re.match(padrao, novo_telefone):
            self.__telefone = novo_telefone
        else:
            raise ValueError("Telefone inválido.")
    
    def to_dict(self):
        data = super().to_dict()
        data["telefone"] = self.__telefone
        return data

    def __str__(self):
        return f"Representante {self.id}: {self.nome} ({self.email}, {self.telefone})"
    
class Representantes(Persistencia):
    def inserir(self, representante: Representante):
        representantes = self.abrir()
        representantes.append(representante.to_dict())
        self.salvar(representantes)

    def listar(self):
        return self.abrir()

    def listar_id(self, id_representante: int):
        representantes = self.abrir()
        for r in representantes:
            if r['id'] == id_representante:
                return r
        return None

    def atualizar(self, id_representante: int, novos_dados: dict):
        representantes = self.abrir()
        for r in representantes:
            if r['id'] == id_representante:
                r.update(novos_dados)
        self.salvar(representantes)

    def excluir(self, id_representante: int):
        representantes = self.abrir()
        representantes = [r for r in representantes if r['id'] != id_representante]
        self.salvar(representantes)

representante = Representante(1, "João", "joao@email.com", "senha123", "(11) 91234-5678")
