import streamlit as st
import pandas as pd
from views import View
import time

class ManterBandaUI:
    def main():
        st.header("Cadastro de Bandas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterBandaUI.listar()
        with tab2: ManterBandaUI.inserir()
        with tab3: ManterBandaUI.atualizar()
        with tab4: ManterBandaUI.excluir()

    def listar():
        bandas = View.banda_listar()
        if not bandas:
            st.write("Nenhuma banda cadastrada")
        else:
            df = pd.DataFrame(bandas)
            st.dataframe(df)

    def inserir():
        # Para inserir uma banda, precisamos escolher o representante previamente cadastrado
        rep_list = View.representante_listar()
        if not rep_list:
            st.error("Nenhum representante cadastrado. Cadastre um representante primeiro.")
            return
        rep_opcoes = {f"{r['id']} - {r['nome']}": r for r in rep_list}
        rep_sel = st.selectbox("Selecione o representante", list(rep_opcoes.keys()))
        representante = rep_opcoes[rep_sel]

        nome = st.text_input("Informe o nome da banda")
        gravadora = st.text_input("Informe a gravadora")
        genero = st.text_input("Informe o gênero musical")
        email = st.text_input("Informe o e-mail da banda")
        senha = st.text_input("Informe a senha da banda", type="password")
        tel = st.text_input("Informe o telefone da banda (ex: (11) 98765-4321)")
        if st.button("Inserir"):
            if nome == "" or gravadora == "" or genero == "" or email == "" or senha == "" or tel == "":
                st.error("Todos os campos devem ser preenchidos!")
                time.sleep(2)
                st.rerun()
            else:
                View.banda_inserir(representante['id'], nome, gravadora, genero, email, senha, tel)
                st.success("Banda inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        bandas = View.banda_listar()
        if not bandas:
            st.write("Nenhuma banda cadastrada")
        else:
            opcoes = {f"{b['id']} - {b['nome']}": b for b in bandas}
            opcao = st.selectbox("Selecione a banda para atualizar", list(opcoes.keys()))
            banda = opcoes[opcao]
            # Atualização dos dados
            nome = st.text_input("Informe o novo nome", banda["nome"])
            gravadora = st.text_input("Informe a nova gravadora", banda["gravadora"])
            genero = st.text_input("Informe o novo gênero", banda["genero"])
            email = st.text_input("Informe o novo e-mail", banda["email"])
            senha = st.text_input("Informe a nova senha", banda["senha"], type="password")
            tel = st.text_input("Informe o novo telefone", banda["tel"])
            if st.button("Atualizar"):
                novos_dados = {"nome": nome, "gravadora": gravadora, "genero": genero, "email": email, "senha": senha, "tel": tel}
                View.banda_atualizar(banda["id"], novos_dados)
                st.success("Banda atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        bandas = View.banda_listar()
        if not bandas:
            st.write("Nenhuma banda cadastrada")
        else:
            opcoes = {f"{b['id']} - {b['nome']}": b for b in bandas}
            opcao = st.selectbox("Selecione a banda para exclusão", list(opcoes.keys()))
            banda = opcoes[opcao]
            if st.button("Excluir"):
                View.banda_excluir(banda["id"])
                st.success("Banda excluída com sucesso")
                time.sleep(2)
                st.rerun()