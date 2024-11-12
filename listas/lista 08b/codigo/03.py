import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime
class ListarHorarioUI:
    def main():
        st.header("Horários Disponíveis")
        ListarHorarioUI.listar()

    def listar():
        # Lista os horários disponíveis
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                horario_data = obj.to_json()
                if horario_data['id_cliente'] in [None, 0] or horario_data['id_servico'] in [None, 0]:
                    del horario_data['id_cliente']  
                    del horario_data['id_servico'] 
                    dic.append(horario_data)  
            df = pd.DataFrame(dic)
            st.dataframe(df)

            horarios_filtrados = [h for h in horarios if h.id_cliente not in [None, 0] and h.id_servico not in [None, 0]]

            if len(horarios_filtrados) == 0:
                st.write("Nenhum horário disponível")
            else:
                op = st.selectbox(
                    "Escolha um horário",
                    horarios_filtrados,
                    format_func=lambda h: f"{h.data.strftime('%d/%m/%Y %H:%M')}"
                )
            servicos = View.servico_listar()
            data = op.data.strftime("%d/%m/%Y %H:%M")
            confirmado = False
            id_servico = None if op.id_servico in [0, None] else op.id_servico
            servico = st.selectbox("Informe o serviço", servicos, next((i for i, s in enumerate(servicos) if s.id == id_servico), None))
            cliente = st.session_state["cliente_id"]
            if st.button("Marcar"):
                id_cliente = None
                id_servico = None
                if cliente != None: id_cliente = st.session_state["cliente_id"]
                if servico != None: id_servico = servico.id
                View.horario_atualizar(op.id, datetime.strptime(data, "%d/%m/%Y %H:%M"),  confirmado, id_cliente, id_servico)
                st.success("Horário marcado com sucesso")
                time.sleep(2)
                st.rerun()
