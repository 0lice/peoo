import streamlit as st
import pandas as pd
from views import View
import time


class AlterardadosUI:
    def main():
        st.header("Alterar meus dados")
        AlterardadosUI.alterar()

    def alterar():
        cliente = st.session_state["cliente_nome"]
        obj_cliente = None
        indicador = ""
        for x in View.cliente_listar():
            if x.nome == cliente:
                obj_cliente = x
                indicador = "cliente"
                break
        for x in View.profissional_listar():
            if x.nome == cliente:
                obj_cliente = x
                indicador = "profissional"
                break

        if cliente != "admin":
            nome = st.text_input("Informe o novo nome do cliente", obj_cliente.nome)
            email = st.text_input("Informe o novo e-mail", obj_cliente.email)
            if indicador == "cliente":
                fone = st.text_input("Informe o novo fone", obj_cliente.fone)
                perfil = st.selectbox("Informe o novo perfil do cliente", View.perfil_listar(), index = None)
            if indicador == "profissional":
                especialidade = st.text_input("Informe o nova especialidade", obj_cliente.especialidade)
                conselho = st.text_input("Informe o novo conselho", obj_cliente.conselho)       
        senha = st.text_input("Informe a nova senha", obj_cliente.senha, type="password")

        if st.button("Atualizar"):
            if cliente == "admin":
                View.cliente_atualizar(obj_cliente.id, obj_cliente.nome, obj_cliente.email, obj_cliente.fone, senha, obj_cliente.id_perfil)                
            elif indicador == "profissional":
                View.profissional_atualizar(obj_cliente.id, nome, especialidade, conselho, email, senha)
            else:
                View.cliente_atualizar(obj_cliente.id, nome, email, fone, senha, perfil)
            st.success("Seus dados foram atualizados com sucesso")
            time.sleep(2)
            st.rerun()