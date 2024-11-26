# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    try:
      if not id:
        raise ValueError('O id não pode estar vazio.')
      
      if not nome:
        raise ValueError('O nome não pode estar vazio.')

      if not email:
        raise ValueError('O email não pode estar vazio.') 
      
      if not fone:
        raise ValueError('O telefone não pode estar vazio.')
      
      if not senha:
        raise ValueError('A senha não pode estar vazia.')
      
      self.__id = id
      self.__nome = nome
      self.__email = email
      self.__fone = fone
      self.__senha = senha

    except ValueError as e:
      print(f'Erro: {e}')  
  
  def __str__(self):
    return f"{self.__nome} - {self.__email} - {self.__fone}"

  def get_id(self):
    return self.__id
  
  def get_nome(self):
    return self.__nome
  
  def get_email(self):
    return self.__email
  
  def get_fone(self):
    return self.__fone
  
  def get_senha(self):
    return self.__senha

  def set_id(self, id):
   try:
     if not id:
       raise ValueError('o id não pode estar vazio.')
     self.__id = id
   except ValueError as e:
    print(f'Erro: {e}')

  def set_id(self, nome):
   try:
     if not nome:
       raise ValueError('o nome não pode estar vazio.')
     self.__nome = nome
   except ValueError as e:
    print(f'Erro: {e}')

  def set_email(self, email):
   try:
     if not email:
       raise ValueError('o email não pode estar vazio.')
     self.__email = email
   except ValueError as e:
    print(f'Erro: {e}')

  def set_fone(self, fone):
   try:
     if not fone:
       raise ValueError('o telefone não pode estar vazio.')
     self.__fone = fone
   except ValueError as e:
    print(f'Erro: {e}')

  def set_senha(self, senha):
   try:
     if not senha:
       raise ValueError('a senha não pode estar vazia.')
     self.__senha = senha
   except ValueError as e:
    print(f'Erro: {e}')

# Persistência
class Clientes:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
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
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.email = obj.email
      c.fone = obj.fone
      c.senha = obj.senha
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda cliente: cliente.nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

