import streamlit as st
import pandas as pd

def mostrar_workout():
    st.title("🏋️ Workout Logger Avanzado")

    if 'ejercicios_registrados' not in st.session_state:
        st.session_state.ejercicios_registrados = []

    st.subheader("Añadir nuevo ejercicio")
    with st.form("form_ejercicio"):
        ejercicio = st.text_input("Nombre del Ejercicio", key="nombre_ejercicio")
        reps = st.number_input("Repeticiones", min_value=1, value=10, key="reps")
        weight = st.number_input("Peso (kg)", min_value=0, value=70, key="peso")
        sets = st.number_input("Series", min_value=1, value=3, key="series")

        submitted = st.form_submit_button("Añadir ejercicio")

        if submitted and ejercicio:
            ejercicio_info = {
                "Ejercicio": ejercicio,
                "Repeticiones": reps,
                "Peso (kg)": weight,
                "Series": sets
            }
            st.session_state.ejercicios_registrados.append(ejercicio_info)
            st.success(f"Ejercicio '{ejercicio}' añadido con éxito 💪")

    if st.session_state.ejercicios_registrados:
        st.subheader("Resumen de ejercicios")
        for i, ejercicio in enumerate(st.session_state.ejercicios_registrados, 1):
            st.write(f"### Ejercicio {i}")
            st.write(f"**Nombre:** {ejercicio['Ejercicio']}")
            st.write(f"**Repeticiones:** {ejercicio['Repeticiones']}")
            st.write(f"**Peso:** {ejercicio['Peso (kg)']} kg")
            st.write(f"**Series:** {ejercicio['Series']}")
            st.markdown("---")

        # Botón para guardar en CSV (dentro del if para evitar error)
        if st.button("💾 Guardar en CSV"):
            df = pd.DataFrame(st.session_state.ejercicios_registrados)
            df.to_csv("workout_log.csv", index=False)
            st.success("Ejercicios guardados en 'workout_log.csv' 📝")
    else:
        st.info("No se han registrado ejercicios aún.")

if __name__ == "__main__":
    mostrar_workout()
