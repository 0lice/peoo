import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha1 = st.text_input("Informe a senha", type="password")
        senha2 = st.text_input("Confirme a senha", type="password")
        if st.button("Inserir"):
            if senha1 == senha2:
                senha = senha1
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()
            elif senha1 != senha2:
                st.error("As senha devem ser iguais")

        