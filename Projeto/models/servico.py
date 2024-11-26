import json

# Modelo
class Servico:
    def __init__(self, id, descricao, valor, duracao):
        try:
            if not descricao:
                raise ValueError('A descrição não pode estar vazia.')
            
            if not valor > 0:
                raise ValueError('O valor tem que ser um número maior que 0.')
            
            if not duracao > 0:
                raise ValueError('A duração deve ser um número maior do que 0.')
            
            self.__id = id
            self.__descricao = descricao
            self.__valor = valor
            self.__duracao = duracao
        
        except ValueError as e:
            print(f'Erro: {e}')

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f} - {self.__duracao} min"

    def to_dict(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "valor": self.__valor,
            "duracao": self.__duracao
        }

    def get_id(self):
        return self.__id

    def set_id(self, id):
        try:
          if not isinstance(id, int):
              raise ValueError('o id deve ser um número.')
          elif id <= 0:
              raise ValueError('o id deve ser um número positivo maior que 0.')
          self.__id = id

        except ValueError as ve:
          print(f'Erro: {ve}')

    def get_desc(self):
        return self.__descricao

    def set_desc(self, desc):
        try:
          if not desc:
              raise ValueError('a descrição não pode estar vazia.')
          elif not isinstance(desc, str):
              raise ValueError('a descrição deve ser um texto.')
          self.__descricao = desc

        except ValueError as ve:
            print(f'Erro: {ve}')

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        try:
          if not isinstance(valor, int):
              raise ValueError('o valor deve ser um número.')
          elif valor <= 0:
              raise ValueError('o valor deve ser maior que 0.')
          self.__valor = valor

        except ValueError as ve:
            print(f'Erro: {ve}')

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
      try:
        if not isinstance(duracao, int):
            raise ValueError('o tempo de duração deve ser um número.')
        elif duracao <= 0:
            raise ValueError('A duração deve ser maior que 0.')
        self.__duracao = duracao

      except ValueError as ve:
          print(f'Erro: {ve}')

# Persistência
class Servicos:
    objetos = []  # atributo estático

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = max((c.get_id() for c in cls.objetos), default=0)  # Usando método get_id()
        obj.set_id(m + 1)  # Define o próximo ID
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.objetos:
            if c.get_id() == id:  # Usando método get_id()
                return c
        return None

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c is not None:
            c.set_desc(obj.get_desc())
            c.set_valor(obj.get_valor())
            c.set_duracao(obj.get_duracao())
            cls.salvar()

    @classmethod
    def excluir(cls, id):
        c = cls.listar_id(id)
        if c is not None:
            cls.objetos.remove(c)
            cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump([c.to_dict() for c in cls.objetos], arquivo)  # Serializa objetos

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
