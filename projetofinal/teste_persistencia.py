from models.banda import Banda
from models.representante import Representante
from models.usuario import Usuario
from models.persistencia import Persistencia

banda_teste = Banda(1, "Banda X", "Rock", ["Alice", "Bob", "Charlie"])
representante_teste = Representante(1, "Carlos", banda_teste)
usuario_teste = Usuario(1, "João", "joao@email.com")

persistencia = Persistencia("dados_agenda.json")

dados_existentes = persistencia.abrir()

if not isinstance(dados_existentes, list):
    dados_existentes = []

dados_existentes.append(banda_teste.to_dict())
dados_existentes.append(representante_teste.to_dict())
dados_existentes.append(usuario_teste.to_dict())

persistencia.salvar(dados_existentes)

dados_carregados = persistencia.abrir()

print(dados_carregados)
