import streamlit as st

st.title('EXERCÍCIO DE COMUNICAÇÃO DO TUBARÃO MAKÃO')

texto = st.text_area(label='Digite aqui a mensagem a ser convertida:', value="", on_change=st.rerun)

while True:
    try:
        texto += input().upper() + ' \n'
    except:
        break

texto = texto.replace(' É ', ' EH ')
texto = texto.replace(' E ', ' ET ')
texto = texto.replace('Á ', 'AH ')
texto = texto.replace('À', 'A')
texto = texto.replace('Á', 'A')
texto = texto.replace('Â', 'A')
texto = texto.replace('É', 'E')
texto = texto.replace('Ê', 'E')
texto = texto.replace('Ó', 'O')
texto = texto.replace('Í', 'I')
texto = texto.replace('Ú', 'U')
texto = texto.replace('Ã', 'A')
texto = texto.replace('Õ', 'O')
texto = texto.replace('Ç', 'C')
texto = texto.replace(',', ' VG')
texto = texto.replace('.',' PT')
texto = texto.replace(';', ' PTVG')
texto = texto.replace(':',' BIPT')
texto = texto.replace('-', 'HF')
texto = texto.replace('"', ' ASP ')
texto = texto.replace('“', 'ASP ')
texto = texto.replace('”', ' ASP')
texto = texto.replace('%', 'PCT')
texto = texto.replace('(', ' PRT ')
texto = texto.replace(')', ' PRT ')
texto = texto.replace('  ', ' ')


st.write('Resultado: ')
st.write(texto)