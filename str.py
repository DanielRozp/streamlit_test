
import streamlit as st

def main():
  #giving a title
  st.title('Mirror Store Prediction Web APP')

  # getting the input data from the user
  store = st.text_input('Name of Store')

  # code for prediction
  diagnosis = ''
  if st.button('Test Result'):
    diagnosis = 'For '+store+' the mirror sotres are: Alcobendas, Toledo, Huercal with 90% of similarity'
  # creating a button for predictions
  stores = ['Badalona', 'Toledo', 'Alcalá de henares']
  query = st.selectbox('Store name', stores, help='Type the name of the store you want to compare and retrieve its mirror store.')
  
  st.write('You selected:', query)
  

if __name__ == '__main__':
  main()
  
  
