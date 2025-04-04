import streamlit as st
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def mostrar_progress():
    st.title("📅 Progress Tracker")
    
    # Pedimos al usuario los días que fue al gimnasio
    dias_asistidos = st.multiselect(
        "Selecciona los días que fuiste al gimnasio:", 
        options=[f"{i+1}/{datetime.datetime.now().month}" for i in range(31)]
    )

    # Guardamos los días en el session_state si no existe
    if "dias_asistidos_registrados" not in st.session_state:
        st.session_state.dias_asistidos_registrados = []

    # Si se presiona el botón para guardar los días
    if st.button("Guardar días en CSV"):
        # Si el usuario seleccionó días nuevos, los agregamos a los días registrados
        if dias_asistidos and dias_asistidos != st.session_state.dias_asistidos_registrados:
            st.session_state.dias_asistidos_registrados = dias_asistidos
            # Guardamos la lista de días en un archivo CSV
            df = pd.DataFrame(st.session_state.dias_asistidos_registrados, columns=["Días Asistidos"])
            df.to_csv("progress_tracker.csv", index=False)
            st.success("Días guardados en 'progress_tracker.csv' 📝")

    # Convertimos los datos para graficar
    dias_numericos = [int(dia.split('/')[0]) for dia in dias_asistidos]
    
    # Graficamos los días asistidos con puntos
    fig, ax = plt.subplots()
    ax.scatter(dias_numericos, [1]*len(dias_numericos), color="blue", label="Días Asistidos")
    ax.set_yticks([])  # Quitamos los ticks del eje Y
    ax.set_xticks(range(1, 32))  # Mostramos todos los días del mes en X
    ax.set_xlabel("Día del Mes")
    ax.set_title("Días Asistidos al Gimnasio")
    ax.legend()
    
    st.pyplot(fig)

if __name__ == "__main__":
    mostrar_progress()
