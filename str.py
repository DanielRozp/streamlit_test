
import streamlit as st

def main():
  #giving a title
  st.title('Mirror Store Prediction Web APP')

  # getting the input data from the user
  store = st.text_input('Name of Store')

  # code for prediction
  diagnosis = ''

  # creating a button for predictions
  if st.button('Test Result'):
    diagnosis = 'For '+store+' the mirror sotres are: Alcobendas, Toledo, Huercal with 90% of similarity'

  st.success(diagnosis)

if __name__ == '__main__':
  main()
  
  
