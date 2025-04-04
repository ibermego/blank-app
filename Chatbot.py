import streamlit as st

def mostrar_chatbot():
    st.title("🪬 Chatbot de Fitness")

    # Chatbot básico
    user_input = st.text_input("Escribe tu pregunta sobre fitness:")
    if st.button("Enviar"):
        st.write("💡 Respuesta del chatbot: ¡Sigue entrenando fuerte! 💪")

    

if __name__ == "__main__":
    mostrar_chatbot()


