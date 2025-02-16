import streamlit as st
import time
from views import View

class RegisterUI:
    @staticmethod
    def main():
        st.header("Registrar Novo Usuário/Representante")
        # Exibe o formulário de registro e chama o método insert() ao confirmar.
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        tipo = st.selectbox("Tipo de registro", ["Usuário", "Representante"])
        telefone = ""
        if tipo == "Representante":
            telefone = st.text_input("Telefone (ex: (11) 91234-5678)")
        
        if st.button("Registrar"):
            RegisterUI.insert(nome, email, senha, tipo, telefone)
            st.success("Registro efetuado com sucesso!")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def insert(nome: str, email: str, senha: str, tipo: str, telefone: str):
        # Insere o registro conforme o tipo escolhido
        if tipo == "Usuário":
            View.usuario_inserir(nome, email, senha)
        else:
            View.representante_inserir(nome, email, senha, telefone)
            