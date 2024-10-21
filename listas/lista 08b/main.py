import re
import json

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.__id = 0
        self.__nome = ''
        self.__email = ''
        self.__fone = ''

        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def __str__(self):
       return f'Informações do cliente:\n* id: {self.__id}\n* nome: {self.__nome}\n* email: {self.__email}\n* telefone: {self.__fone}'

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def set_id(self, new_id):
        try:
            if not isinstance(new_id, int) or new_id <= 0:
                raise ValueError('O ID deve seguir as seguintes condições:\n- ser um número;\n- ser positivo.')
            
            self.__id = new_id

        except ValueError as ve:
            print(f'Erro: {ve}')

    def set_nome(self, new_name):
        try:
            if not isinstance(new_name, str) or len(new_name) < 2:
                raise ValueError('O nome deve seguir as seguintes condições:\n- ser um texto/string;\n- não ter menos que 2 caracteres.')
            
            self.__nome = new_name
        
        except ValueError as ve:
            print(f'Erro: {ve}')

    def set_email(self, new_email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        try:
            if not re.match(padrao, new_email):
                raise ValueError('O email deve seguir as seguintes condições:\n- ser um texto/string;\n- estar no formato correto para email. Exemplo: abc123@dominio.com')
            
            self.__email = new_email

        except ValueError as ve:
            print(f'Erro: {ve}')

    def set_fone(self, new_fone):
        try:
            if not isinstance(new_fone, str) or len(new_fone) != 11:
                raise ValueError('O número de telefone deve seguir as seguintes condições:\n- ser um texto/string;\n- ter exatamente 11 dígitos, com DDD. Exemplo: 84912345678')
            
            self.__fone = new_fone

        except ValueError as ve:
            print(f'Erro: {ve}')


class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos: # para cada cliente na lista 'objetos' da classe:
            if x.id > id: id = x.id # se o id do cliente for maior que a variável id: id será = id do cliente
        id =+ 1
        obj.id = id
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        for x in cls.objetos:
            if x.id == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod # Isso indica que o método é um método de classe, ou seja, ele pode acessar atributos da classe (como cls.objetos) em vez de instâncias específicas da classe.
    def salvar(cls):
        with open('clientes.json', mode='w') as arquivo: #  Abre o arquivo clientes.json no modo de escrita ("w"). Se o arquivo já existir, ele será sobrescrito.
            json.dump(cls.objetos, arquivo, default = vars) # Serializa cls.objetos e grava essa representação no arquivo JSON. O parâmetro default=vars indica que, se um objeto não puder ser serializado diretamente, a função vars() será chamada para obter um dicionário com seus atributos.

    def abrir(cls):
        cls.objetos = []
        try:
          with open("../clientes.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                  cls.objetos.append(c)
        except FileNotFoundError:
          pass  


