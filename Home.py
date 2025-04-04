import streamlit as st
import pandas as pd
import datetime
import os

CSV_FILENAME = "valoraciones.csv"

# Inicializar el DataFrame en sesión si no existe
if 'valoraciones' not in st.session_state:
    if os.path.exists(CSV_FILENAME):
        st.session_state['valoraciones'] = pd.read_csv(CSV_FILENAME)
    else:
        st.session_state['valoraciones'] = pd.DataFrame(columns=["Fecha", "Valoración"])

def mostrar_valoracion():
    st.title("🏋️‍♂️ Bienvenido a Fitness Tracker")
    st.write("Esta es tu aplicación para registrar tu progreso en el fitness.")
    st.subheader("⭐ ¿Cuál es su nivel de satisfacción con esta aplicación?")

    with st.form("form_valoracion"):
        valor = st.radio(
            "Seleccione una opción:",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: "⭐" * x,
            key="valoracion_radio"
        )
        submit_button = st.form_submit_button("Enviar valoración")

        if submit_button:
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            nueva_fila = {"Fecha": fecha, "Valoración": valor}
            st.session_state['valoraciones'] = pd.concat(
                [st.session_state['valoraciones'], pd.DataFrame([nueva_fila])],
                ignore_index=True
            )
            st.session_state['valoraciones'].to_csv(CSV_FILENAME, index=False)

            st.success("Valoración guardada correctamente 🙌")

            # Feedback visual
            match valor:
                case 1:
                    st.error("😔 Lamentamos no haber cumplido tus expectativas.")
                case 2:
                    st.warning("😕 Gracias por tu sinceridad, intentaremos mejorar.")
                case 3:
                    st.info("😐 ¡Seguimos trabajando para que te guste más!")
                case 4:
                    st.success("😎 ¡Gracias! Casi perfecto.")
                case 5:
                    st.success("🥳 ¡Gracias por tu máxima valoración!")

# Llamada a la función si estás dentro de main
if __name__ == "__main__":
    mostrar_valoracion()
