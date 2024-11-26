from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        try:    
            for c in View.cliente_listar():
                if c.email == email:
                    raise ValueError(f'o email {email} já está em uso.')
            c = Cliente(0, nome, email, fone, senha)
            Clientes.inserir(c)

        except ValueError as e:
            print(f'Erro: {e}')

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        try:
            for c in View.cliente_listar:
                if c.email == email:
                    raise ValueError(f'o email {email} já está em uso.')
            c = Cliente(id, nome, email, fone, senha)
            Clientes.atualizar(c)

        except ValueError as e:
            print(f'Erro: {e}')

    def cliente_excluir(id):
        for h in View.horario_listar():
            if h.id_cliente == id:
                raise ValueError(f"O cliente com id {id} possui horários agendados e não pode ser excluído.")
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)    

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        if id_cliente is not None and View.cliente_listar_id(id_cliente) is None:
            raise ValueError(f"Cliente com ID {id_cliente} não encontrado.")
        if id_servico is not None and View.servico_listar_id(id_servico) is None:
            raise ValueError(f"Serviço com ID {id_servico} não encontrado.")
        c = Horario(0, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        if id_cliente is not None and View.cliente_listar_id(id_cliente) is None:
            raise ValueError(f"Cliente com ID {id_cliente} não encontrado.")
        if id_servico is not None and View.servico_listar_id(id_servico) is None:
            raise ValueError(f"Serviço com ID {id_servico} não encontrado.")
        c = Horario(id, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.atualizar(c)

    def horario_excluir(id):
        for h in View.horario_listar():
            if h.id == id and h.id_cliente is not None:
                raise ValueError(f"O horário com ID {id} está agendado para um cliente e não pode ser excluído.")
        c = Horario(id, None)
        Horarios.excluir(c)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        #data = "05/11/2024"
        #inicio = "08:00"
        #fim = "12:00"
        #intervalo = 60
        try:
            di = datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
            df = datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M")
            if di >= df:
                raise ValueError("A hora de início deve ser anterior à hora de fim.")
            if intervalo <= 0:
                raise ValueError("O intervalo deve ser maior que 0 minutos.")
        except ValueError as e:
            raise ValueError(f"Erro ao abrir a agenda: {e}")

        # Gerar horários
        d = timedelta(minutes=intervalo)
        x = di
        while x <= df:
            View.horario_inserir(x, False, None, None)
            x += d

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        for h in View.horario_listar():
            if h.id_servico == id:
                raise ValueError(f"O serviço com ID {id} está associado a um horário na agenda e não pode ser excluído.")
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)   
