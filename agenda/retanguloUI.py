import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header('cálculos com retângulo')
        b = st.text_input('base')
        h = st.text_input('altura')
        if st.button('calcular'):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f'área = {r.calc_area()}')
            st.write(f'diagonal = {r.calc_diagonal()}')
