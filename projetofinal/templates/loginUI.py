import streamlit as st
import time
from views import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        
        if st.button("Entrar"):
            usuario_encontrado = None
            for u in View.usuario_listar():
                if u['email'] == email and u['senha'] == senha:
                    usuario_encontrado = u
                    break
            if not usuario_encontrado:
                for r in View.representante_listar():
                    if r['email'] == email and r['senha'] == senha:
                        usuario_encontrado = r
                        break
            if usuario_encontrado:
                st.session_state["usuario_id"] = usuario_encontrado["id"]
                st.session_state["usuario_nome"] = usuario_encontrado["nome"]
                st.success("Login efetuado com sucesso!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos.")
                