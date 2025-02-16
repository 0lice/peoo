import streamlit as st
import time
from views import View
from datetime import datetime

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Agenda do Dia")
        AbrirAgendaUI.abrir_agenda()

    @staticmethod
    def abrir_agenda():
        data = st.text_input("Informe a data (dd/mm/aaaa)", datetime.now().strftime("%d/%m/%Y"), key="agenda_data")
        hora_inicio = st.text_input("Informe o horário inicial (HH:MM)", key="agenda_inicio")
        hora_fim = st.text_input("Informe o horário final (HH:MM)", key="agenda_fim")
        intervalo = st.text_input("Informe o intervalo (minutos)", key="agenda_intervalo")
        if st.button("Abrir Agenda"):
            if data and hora_inicio and hora_fim and intervalo:
                try:
                    View.horario_abrir_agenda(data, hora_inicio, hora_fim, int(intervalo))
                    st.success("Agenda aberta com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {str(e)}")
            else:
                st.error("Preencha todos os campos!")
                