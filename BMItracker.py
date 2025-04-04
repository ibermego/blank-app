import streamlit as st
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def mostrar_bmi():
    st.title("📊 BMI Tracker")

    # Inicializar session_state si no existe
    if "bmi_records" not in st.session_state:
        st.session_state.bmi_records = []

    # Inputs para altura y peso
    height = st.number_input("Introduce tu altura (cm)", min_value=50, max_value=250, value=170)
    weight = st.number_input("Introduce tu peso (kg)", min_value=20, max_value=300, value=70)

    # Calcular y guardar BMI al pulsar el botón
    if st.button("Calcular BMI"):
        bmi = weight / ((height / 100) ** 2)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        st.session_state.bmi_records.append({
            "Fecha": fecha,
            "Altura": height,
            "Peso": weight,
            "BMI": round(bmi, 2)
        })
        st.success(f"Tu BMI es: {bmi:.2f} — ¡A seguir mejorando!")

    # Mostrar historial si hay datos
    if st.session_state.bmi_records:
        st.subheader("📜 Historial de BMI:")
        for record in st.session_state.bmi_records:
            st.write(f"- 📌 {record}")

        # Mostrar gráfico de evolución
        fechas = [record["Fecha"] for record in st.session_state.bmi_records]
        bmis = [record["BMI"] for record in st.session_state.bmi_records]

        fig, ax = plt.subplots()
        ax.plot(fechas, bmis, marker='o', color='b', linestyle='-', label="BMI")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("BMI")
        ax.set_title("Evolución del BMI")
        ax.grid(True)
        ax.legend()
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Convertimos a DataFrame
        df = pd.DataFrame(st.session_state.bmi_records)

        # Botón para guardar como archivo local
        if st.button("💾 Guardar historial como CSV"):
            df.to_csv("bmi_log.csv", index=False)
            st.success("Historial guardado como 'bmi_log.csv'")

        
    else:
        st.info("Todavía no has registrado ningún BMI.")

# Ejecutar función
if __name__ == "__main__":
    mostrar_bmi()
