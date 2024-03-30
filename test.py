import streamlit as st

st.write('Aplikasi Penjumlahan Bilangan Numerik,divider=rainbow')

angka_pertama = st.number_input('massukkan angka pertama')
st.write('the first number is',angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('the number is',angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"angka pertama {angka_pertama} x angka kedua {angka_kedua} = {operasi_matematika}")
st.write('ini ya jawabannya :sunglasses:')