import json
from models.crud import CRUD

# Modelo
class Perfil:
  def __init__(self, id, nome, descricao, beneficios):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.beneficios = beneficios
  def __str__(self):
    return f"{self.nome} - {self.descricao} - {self.beneficios}"

# Persistência
class Perfis (CRUD):
  objetos = []    # atributo estático

  @classmethod
  def salvar(cls):
    with open("perfis.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("perfis.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Perfil(obj["id"], obj["nome"], obj["descricao"], obj["beneficios"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass