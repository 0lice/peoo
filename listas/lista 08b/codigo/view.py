from main import Cliente, Clientes

class View:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        if nome == '': raise ValueError('o nome deve ser preenchido.')
        if email == '': raise ValueError('o email deve ser preenchido.')
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, 'noname', 'noemail', '')
        Clientes.excluir(c)

