import streamlit as st
import pandas as pd
from views import View
import time

class ManterCidadeUI:
    def main():
        st.header("Cadastro de Cidades")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCidadeUI.listar()
        with tab2: ManterCidadeUI.inserir()
        with tab3: ManterCidadeUI.atualizar()
        with tab4: ManterCidadeUI.excluir()

    def listar():
        cidades = View.cidade_listar()
        if len(cidades) == 0:
            st.write("Nenhuma cidade cadastrada")
        else:
            df = pd.DataFrame(cidades)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome da cidade")
        local_show = st.text_input("Informe o local de show")
        estado = st.text_input("Informe o estado (ex: SP)")
        if st.button("Inserir"):
            if nome == "" or local_show == "" or estado == "":
                st.error("Todos os campos devem ser preenchidos!")
                time.sleep(2)
                st.rerun()
            else:
                View.cidade_inserir(nome, local_show, estado)
                st.success("Cidade inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        cidades = View.cidade_listar()
        if len(cidades) == 0:
            st.write("Nenhuma cidade cadastrada")
        else:
            # Seleciona a cidade para atualizar a partir do id
            opcoes = {f"{c['id']} - {c['nome']}": c for c in cidades}
            opcao = st.selectbox("Selecione a cidade para atualizar", list(opcoes.keys()))
            cidade = opcoes[opcao]
            nome = st.text_input("Informe o novo nome", cidade["nome"])
            local_show = st.text_input("Informe o novo local de show", cidade["local_show"])
            estado = st.text_input("Informe o novo estado", cidade["estado"])
            if st.button("Atualizar"):
                View.cidade_atualizar(cidade["id"], nome, local_show, estado)
                st.success("Cidade atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        cidades = View.cidade_listar()
        if len(cidades) == 0:
            st.write("Nenhuma cidade cadastrada")
        else:
            opcoes = {f"{c['id']} - {c['nome']}": c for c in cidades}
            opcao = st.selectbox("Selecione a cidade para excluir", list(opcoes.keys()))
            cidade = opcoes[opcao]
            if st.button("Excluir"):
                View.cidade_excluir(cidade["id"])
                st.success("Cidade excluída com sucesso")
                time.sleep(2)
                st.rerun()