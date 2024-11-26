import json
from datetime import datetime
from cliente import Cliente, Clientes
from servico import Servico, Servicos

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0

    def __str__(self):
        return f"{self.__id} - {self.__data}"
    
    def to_json(self):
      dic = {}
      dic["id"] = self.__id
      dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.__confirmado
      dic["id_cliente"] = self.__id_cliente
      dic["id_servico"] = self.__id_servico
      return dic    

    def get_id(self):
      return self.__id
    
    def get_data(self):
      return self.__data
    
    def get_conf(self):
      return self.__confirmado
    
    def get_idcliente(self):
      return self.__id_cliente
    
    def get_idserv(self):
      return self.__id_servico
    
    def set_id(self, id):
      self.__id = id
    
    def set_data(self, data):
      self.__data = data

    def set_conf(self, confirmacao):
      self.__confirmado = confirmacao

    def set_idcliente(self, idcliente): 
      self.___id_cliente = idcliente

    def set_idserv(self, idservico):
      self.__id_servico = idservico


class Horarios:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    if obj.get_idcliente() and not Clientes.listar_id(obj.get_idcliente()):
        raise ValueError("O ID do cliente é inválido.")
    if obj.get_idserv() and not Servicos.listar_id(obj.get_idserv()):
        raise ValueError("O ID do serviço é inválido.")

    m = 0
    for c in cls.objetos:
        if c.get_id() > m: 
            m = c.get_id()
    obj.set_id(m + 1)
    cls.objetos.append(obj)
    cls.salvar()
    
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    if obj.get_idcliente() and not Clientes.listar_id(obj.get_idcliente()):
            raise ValueError("O ID do cliente é inválido.")
    if obj.get_idserv() and not Servicos.listar_id(obj.get_idserv()):
            raise ValueError("O ID do serviço é inválido.")
    

    c = cls.listar_id(obj.id)
    if c != None:
      c.data = obj.data
      c.confirmado = obj.confirmado
      c.id_cliente = obj.id_cliente
      c.id_servico = obj.id_servico
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    c = cls.listar_id(obj.get_id())
    if c:
        if c.get_conf():
            raise ValueError("Não é possível excluir um horário confirmado.")
        cls.objetos.remove(c)
        cls.salvar()
    else:
        raise ValueError("O horário especificado não foi encontrado.")
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.confirmado = obj["confirmado"]
          c.id_cliente = obj["id_cliente"]
          c.id_servico = obj["id_servico"]
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



