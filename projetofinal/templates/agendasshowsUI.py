import streamlit as st
import pandas as pd
from datetime import datetime
from views import View

class AgendaShowsUI:
    @staticmethod
    def main():
        st.header("Agenda de Shows")
        AgendaShowsUI.agenda()

    @staticmethod
    def agenda():
        apresentacoes = View.apresentacao_listar()
        if not apresentacoes:
            st.write("Nenhum show agendado.")
            return
        filtro = st.checkbox("Mostrar apenas shows futuros?")
        if filtro:
            agora = datetime.now()
            filtradas = []
            for a in apresentacoes:
                try:
                    dt = datetime.strptime(a["data"], "%d/%m/%Y %H:%M")
                    if dt >= agora:
                        filtradas.append(a)
                except:
                    pass
            apresentacoes = filtradas
        if apresentacoes:
            st.dataframe(pd.DataFrame(apresentacoes))
        else:
            st.write("Nenhum show encontrado com o filtro selecionado.")
