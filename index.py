from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterservicoUI import ManterServicoUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.listarhorarioUI import ListarHorarioUI
from templates.manterperfilUI import ManterPerfilUI
from templates.ManterProfissionais import ManterProfissionalUI
from templates.loginUI import LoginUI
from templates.alterardadosUI import AlterardadosUI
from templates.profissionalagendaUI import ProfissionalAgendaUI
from views import View

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Cadastro de Perfis", "Cadastro de Profissional", "Abrir Agenda do Dia", "Alterar meus dados"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Perfis": ManterPerfilUI.main()
        if op == "Cadastro de Profissional": ManterProfissionalUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
        if op == "Alterar meus dados": AlterardadosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Visualizar a minha agenda", "Alterar meus dados"])
        if op == "Visualizar a minha agenda": ProfissionalAgendaUI.main()
        if op == "Alterar meus dados": AlterardadosUI.main()
        
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Horários Disponíveis", "Alterar meus dados"])
        if op == "Horários Disponíveis": ListarHorarioUI.main()
        if op == "Alterar meus dados": AlterardadosUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()
    
    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            prof = False
            for x in View.profissional_listar():
                if st.session_state["cliente_nome"] == x.nome:
                    prof = True
            # mensagen de bem-vindo
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # menu do usuário
            if admin: IndexUI.menu_admin()
            elif prof: IndexUI.menu_profissional()
            else: IndexUI.menu_cliente()
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        # verifica a existe o usuário admin
        View.cliente_admin()
        # monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()
