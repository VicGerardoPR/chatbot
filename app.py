import streamlit as st
import openai
import os

# Configura la clave de la API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Función para obtener la respuesta del chatbot
def get_chatbot_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # Puedes cambiar el motor según tu suscripción
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return response.choices[0].text.strip()

# Configurar la página de Streamlit
st.title('Chatbot con OpenAI')
st.write("Interactúa con el chatbot ingresando tu mensaje a continuación.")

# Inicializar el estado de la sesión para almacenar el historial del chat
if 'history' not in st.session_state:
    st.session_state.history = []

# Formulario de entrada del usuario
with st.form(key='chat_form'):
    user_input = st.text_input("Tú: ")
    submit_button = st.form_submit_button(label='Enviar')

# Procesar la entrada del usuario
if submit_button and user_input:
    # Obtener la respuesta del chatbot
    response = get_chatbot_response(user_input)

    # Actualizar el historial del chat
    st.session_state.history.append({"user": user_input, "bot": response})

# Mostrar el historial del chat
if st.session_state.history:
    for chat in st.session_state.history:
        st.write(f"Tú: {chat['user']}")
        st.write(f"Bot: {chat['bot']}")
        st.write("---")
