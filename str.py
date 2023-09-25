
import streamlit as st

def main():
  #giving a title
  st.title('Mirror Store Prediction Web APP')

  # getting the input data from the user
  store = st.text_input('Name of Store')

  # code for prediction
  diagnosis = ''

  # creating a button for predictions
  stores = ['Badalona', 'Toledo', 'Alcalá de henares']
  st.selectbox('Store name, stores')

if __name__ == '__main__':
  main()
  
  
