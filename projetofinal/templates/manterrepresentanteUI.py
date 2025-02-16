import streamlit as st
import pandas as pd
import time
from views import View

class ManterRepresentanteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Representantes")
        ManterRepresentanteUI.listar()
        ManterRepresentanteUI.inserir()
        ManterRepresentanteUI.atualizar()
        ManterRepresentanteUI.excluir()

    @staticmethod
    def listar():
        reps = View.representante_listar()
        if reps:
            st.subheader("Listar Representantes")
            st.dataframe(pd.DataFrame(reps))
        else:
            st.write("Nenhum representante cadastrado.")

    @staticmethod
    def inserir():
        st.subheader("Inserir Representante")
        nome = st.text_input("Nome", key="rep_nome")
        email = st.text_input("E-mail", key="rep_email")
        senha = st.text_input("Senha", type="password", key="rep_senha")
        telefone = st.text_input("Telefone (ex: (11) 91234-5678)", key="rep_tel")
        if st.button("Inserir Representante"):
            if nome and email and senha and telefone:
                View.representante_inserir(nome, email, senha, telefone)
                st.success("Representante inserido!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Preencha todos os campos!")

    @staticmethod
    def atualizar():
        st.subheader("Atualizar Representante")
        reps = View.representante_listar()
        if reps:
            opcoes = {f"{r['id']} - {r['nome']}": r for r in reps}
            opcao = st.selectbox("Selecione o Representante", list(opcoes.keys()), key="atualiza_rep")
            rep = opcoes[opcao]
            novo_nome = st.text_input("Novo Nome", rep["nome"], key="rep_novo_nome")
            novo_email = st.text_input("Novo E-mail", rep["email"], key="rep_novo_email")
            nova_senha = st.text_input("Nova Senha", rep["senha"], type="password", key="rep_nova_senha")
            novo_tel = st.text_input("Novo Telefone", rep["telefone"], key="rep_novo_tel")
            if st.button("Atualizar Representante"):
                novos_dados = {
                    "nome": novo_nome,
                    "email": novo_email,
                    "senha": nova_senha,
                    "telefone": novo_tel
                }
                View.representante_atualizar(rep["id"], novos_dados)
                st.success("Representante atualizado!")
                time.sleep(2)
                st.rerun()
        else:
            st.write("Nenhum representante cadastrado.")

    @staticmethod
    def excluir():
        st.subheader("Excluir Representante")
        reps = View.representante_listar()
        if reps:
            opcoes = {f"{r['id']} - {r['nome']}": r for r in reps}
            opcao = st.selectbox("Selecione o Representante para exclusão", list(opcoes.keys()), key="exclui_rep")
            rep = opcoes[opcao]
            if st.button("Excluir Representante"):
                View.representante_excluir(rep["id"])
                st.success("Representante excluído!")
                st.rerun()
        else:
            st.write("Nenhum representante cadastrado.")
            