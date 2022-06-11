import streamlit as st

st.header('EMI Calculator')
ch = st.radio('Calculate', ('EMI', 'Outstanding Loan Balance'))

if ch == 'EMI':
	p = st.number_input('Principle amount : ')
	r = st.number_input('Rate of interest : ', 0.0, 50.0, step=0.1)
	n = st.number_input('Number of months : ', step=1.0)
	if st.button('Calculate'):
		emi = p * (r/100) * (((1+(r/100))**n)/(((1+(r/100))**n)-1))
		st.write('EMI = ', round(emi, 2))
elif ch == 'Outstanding Loan Balance':
	p = st.number_input('Principle amount : ')
	r = st.number_input('Rate of interest : ', 0.0, 50.0, step=1.0)
	n = st.number_input('Number of months : ', step=1.0)
	m = st.number_input('After how many months balance is calculated: ')
	if st.button('Calculate'):
		emi = (p * (((1+(r/100))**n)-((1+(r/100))**m)))/(((1+(r/100))**n)-1)
		st.write('EMI = ', round(emi, 2))
