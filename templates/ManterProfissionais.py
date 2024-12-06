import streamlit as st
import pandas as pd
from views import View
import time

class ManterProfissionalUI():


    def main():
        st.header("Cadastro de profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:    
            #for obj in profissionais: st.write(obj)
            dic = []
            for obj in profissionais: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum serviço cadastrado")

        cliente = st.selectbox("Informe o profissional", clientes)
        nome = st.text_input("Informe o nome", cliente.nome)
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = cliente.email
        senha = cliente.senha
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, conselho, email, senha)
            View.cliente_excluir(cliente.id)
            st.success("profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissional", profissionais)
            nome = st.text_input("Informe o novo nome do profissional", op.nome)
            especialidade = st.text_input("Informe o nova especialidade", op.especialidade)
            conselho = st.text_input("Informe o novo conselho", op.conselho)
            if st.button("Atualizar"):
                View.profissional_atualizar(op.id, nome, especialidade, conselho)
                st.success("profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissional", profissionais)
            if st.button("Excluir"):
                View.profissional_excluir(op.id)
                st.success("profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()
