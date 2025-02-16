from models.cliente import Cliente
from models.persistencia_json import PersistenciaJSON

# Criando um objeto para teste
cliente_teste = Cliente(1, "Alice", "alice@email.com", "11999999999")

# Criando um gerenciador de persistência
persistencia = PersistenciaJSON("clientes.json")

# Salvando o cliente
persistencia.salvar(cliente_teste)

# Carregando os dados
dados_carregados = persistencia.carregar()

print(dados_carregados)
