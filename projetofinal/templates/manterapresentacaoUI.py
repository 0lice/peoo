import streamlit as st
import pandas as pd
from views import View
from datetime import datetime
import time

class ManterApresentacaoUI:
    def main():
        st.header("Cadastro de Apresentações")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterApresentacaoUI.listar()
        with tab2: ManterApresentacaoUI.inserir()
        with tab3: ManterApresentacaoUI.atualizar()
        with tab4: ManterApresentacaoUI.excluir()

    def listar():
        apresentacoes = View.apresentacao_listar()
        if not apresentacoes:
            st.write("Nenhuma apresentação cadastrada")
        else:
            df = pd.DataFrame(apresentacoes)
            st.dataframe(df)

    def inserir():
        # Para inserir, seleciona uma banda previamente cadastrada
        bandas = View.banda_listar()
        if not bandas:
            st.error("Nenhuma banda cadastrada. Cadastre uma banda primeiro.")
            return
        opcoes = {f"{b['id']} - {b['nome']}": b for b in bandas}
        opcao = st.selectbox("Selecione a banda", list(opcoes.keys()))
        banda = opcoes[opcao]
        
        data_str = st.text_input("Informe a data e horário (dd/mm/aaaa HH:MM)", datetime.now().strftime("%d/%m/%Y %H:%M"))
        local = st.text_input("Informe o local da apresentação")
        confirmado = st.checkbox("Apresentação confirmada")
        if st.button("Inserir"):
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                if local == "":
                    st.error("O local deve ser informado!")
                    return
                View.apresentacao_inserir(banda['id'], data, local, confirmado)
                st.success("Apresentação inserida com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {str(e)}")

    def atualizar():
        apresentacoes = View.apresentacao_listar()
        if not apresentacoes:
            st.write("Nenhuma apresentação cadastrada")
        else:
            opcoes = {f"{a['id']} - Banda {a['id_banda']} em {a['data']}": a for a in apresentacoes}
            opcao = st.selectbox("Selecione a apresentação para atualizar", list(opcoes.keys()))
            apresentacao = opcoes[opcao]
            data_str = st.text_input("Informe a nova data e horário (dd/mm/aaaa HH:MM)", apresentacao["data"])
            local = st.text_input("Informe o novo local", apresentacao["local"])
            confirmado = st.checkbox("Apresentação confirmada", value=apresentacao["confirmado"])
            if st.button("Atualizar"):
                try:
                    data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                    novos_dados = {"data": data.strftime("%d/%m/%Y %H:%M"), "local": local, "confirmado": confirmado}
                    View.apresentacao_atualizar(apresentacao["id"], novos_dados)
                    st.success("Apresentação atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {str(e)}")

    def excluir():
        apresentacoes = View.apresentacao_listar()
        if not apresentacoes:
            st.write("Nenhuma apresentação cadastrada")
        else:
            opcoes = {f"{a['id']} - Banda {a['id_banda']} em {a['data']}": a for a in apresentacoes}
            opcao = st.selectbox("Selecione a apresentação para exclusão", list(opcoes.keys()))
            apresentacao = opcoes[opcao]
            if st.button("Excluir"):
                View.apresentacao_excluir(apresentacao["id"])
                st.success("Apresentação excluída com sucesso")
                time.sleep(2)
                st.rerun()