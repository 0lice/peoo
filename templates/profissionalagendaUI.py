import streamlit as st
import pandas as pd
from views import View
import time


class ProfissionalAgendaUI:
    def main():
        st.header("Sua agenda")
        ProfissionalAgendaUI.agenda()


    def agenda():
        prof = st.session_state["cliente_nome"]
        horarios = View.profissional_agenda(prof)
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:  
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.id_cliente)
                servico = View.servico_listar_id(obj.id_servico)
                profissional = View.profissional_listar_id(obj.id_profissional)
                if cliente != None: cliente = cliente.nome
                if servico != None: servico = servico.descricao
                if profissional != None: profissional = profissional.nome
                
                dic.append({"id" : obj.id, "data" : obj.data, "confirmado" : obj.confirmado, "cliente" : cliente, "serviço" : servico, "profissional" : profissional })
            df = pd.DataFrame(dic)
            st.dataframe(df)
        