import streamlit as st # Importa a biblioteca do streamlit para criar elementos visuais.

st.title ("🧮 CALCULADORA SIMPLES")

num1 = st.number_input ("Digite o 1° valor:", step=1) #st.number vai criar caixas pro usuário digitar os valoeres. O "step=1" define o parâmetro.
num2 = st.number_input ("Digite o 2° valor:", step=1)

operação = st.selectbox("Escolha a operação: ", ("+","-","%","*")) # st.selectbox cria uma caixa com os ícones definidos para não existir erro na hora da escrita.

if st.button("Calcular"): # Cria um botão "calcular" que permite o código só rodar apos o usuário clicar nele.
  match operação:
   
    case "+":
      res = num1 + num2 
     
    case "-":
      res = num1 - num2

    case "*":
      res = num1 * num2

    case "%":
      res = num1 / num2
      
      if num2 != 0: # Se o segundo número for diferente de 0, a divisão prossegue, caso contrário, surge na tela uma mensagem de erro.
        res = num1 / num2
      else:
        res = "Erro divisão por zero!"


  st.success(f"A resposta da operação é: {res}") # Exibe o resultado da operação.
