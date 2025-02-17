from models.banda import Banda
from models.representante import Representante
from models.usuario import Usuario
from models.persistencia import Persistencia

banda_teste = Banda(1, 2, "Banda X", "bandeirantes", "rock", "nalice123@gmail.com", "alice@123", "(84) 99965-5932")
representante_teste = Representante(1, "Carlos", "carlinhos267@hotmail.com", "socorro.123", "(21) 98876-0991")
usuario_teste = Usuario(1, "João", "joao@email.com", "juarez47*")

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
