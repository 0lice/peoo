import streamlit as st
import time
from datetime import datetime
from views import View

class AgendaShowUI:
    @staticmethod
    def main():
        st.header("Agendar Show")
        AgendaShowUI.agenda()

    @staticmethod
    def agenda():
        bandas = View.banda_listar()
        if not bandas:
            st.error("Nenhuma banda cadastrada. Cadastre uma banda primeiro.")
            return
        opcoes = {f"{b['id']} - {b['nome']}": b for b in bandas}
        opcao = st.selectbox("Selecione a Banda", list(opcoes.keys()), key="agenda_show_banda")
        banda = opcoes[opcao]
        data_str = st.text_input("Data e horário (dd/mm/aaaa HH:MM)", datetime.now().strftime("%d/%m/%Y %H:%M"), key="agenda_show_data")
        local = st.text_input("Local do Show", key="agenda_show_local")
        confirmado = st.checkbox("Confirmar Show?", key="agenda_show_confirmado")
        if st.button("Agendar Show"):
            try:
                from datetime import datetime
                data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                View.apresentacao_inserir(banda["id"], data, local, confirmado)
                st.success("Show agendado!")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {str(e)}")
                