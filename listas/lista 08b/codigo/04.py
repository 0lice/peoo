import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime
class Confirmacao:
    def main():
        st.header("Horários a Serem Confirmados")
        Confirmacao.listar()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                horario_data = obj.to_json()
                if (horario_data['id_cliente'] not in [None, 0] or horario_data['id_servico'] not in [None, 0]) and horario_data['confirmado'] != True:
                    cliente = View.cliente_listar_id(obj.id_cliente)
                    servico = View.servico_listar_id(obj.id_servico)
                    if cliente != None: cliente = cliente.nome
                    if servico != None: servico = servico.descricao
                    dic.append({"id" : obj.id, "data" : obj.data, "confirmado" : obj.confirmado, "cliente" : cliente, "serviço" : servico})

            df = pd.DataFrame(dic)
            st.dataframe(df)

            horarios_filtrados = [h for h in horarios if h.id_cliente not in [None, 0] and h.id_servico not in [None, 0] and h.confirmado != True]
            if len(horarios_filtrados) == 0:
                st.write("Nenhum horário com dados preenchidos")
            else:
                op = st.selectbox(
                    "Escolha um horário",
                    horarios_filtrados,
                    format_func=lambda h: f"{h.data.strftime('%d/%m/%Y %H:%M')}"
                )
            servicos = View.servico_listar()
            clientes = View.cliente_listar()
            data = op.data.strftime("%d/%m/%Y %H:%M")
            confirmado = st.checkbox("Nova confirmação", op.confirmado)
            id_cliente = None if op.id_cliente in [0, None] else op.id_cliente
            id_servico = None if op.id_servico in [0, None] else op.id_servico
            cliente_selecionado = next((c for c in clientes if c.id == id_cliente), None)
            cliente = st.selectbox("Cliente", clientes, index=clientes.index(cliente_selecionado), disabled=True)
            servico_selecionado = next((c for c in servicos if c.id == id_servico), None)
            servico = st.selectbox("Serviço", servicos, index=servicos.index(servico_selecionado), disabled=True)
            if st.button("Atualizar"):
                id_cliente = None
                id_servico = None
                if cliente != None: id_cliente = cliente.id
                if servico != None: id_servico = servico.id
                View.horario_atualizar(op.id, datetime.strptime(data, "%d/%m/%Y %H:%M"),  confirmado, id_cliente, id_servico)
                st.success("Horário atualizado com sucesso")
                time.sleep(2)
                st.rerun()
