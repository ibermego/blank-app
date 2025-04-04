import streamlit as st
from PIL import Image

def mostrar_recomendador():
    st.title("📋 Recomienda tu Rutina")

    st.subheader("Elige tus objetivos y te ayudaremos a entrenar mejor 💪")

    objetivo = st.selectbox("¿Cuál es tu objetivo principal?", ["Selecciona...", "Ganar masa muscular", "Perder grasa", "Mantener forma"])
    nivel = st.radio("¿Cuál es tu nivel?", ["Principiante", "Intermedio", "Avanzado"])

    if objetivo != "Selecciona...":
        st.markdown("---")
        st.subheader("🏋️ Rutina recomendada:")

        # match-case disponible en Python 3.10+
        match (objetivo, nivel):
            case ("Ganar masa muscular", "Principiante"):
                nombre, desc = "Press de banca", "Ejercicio clave para pecho y fuerza general."
            case ("Ganar masa muscular", "Intermedio"):
                nombre, desc = "Dominadas lastradas", "Intensifica el entrenamiento de espalda y brazos."
            case ("Perder grasa", "Principiante"):
                nombre, desc = "Burpees", "Ejercicio completo que acelera tu metabolismo."
            case ("Perder grasa", "Avanzado"):
                nombre, desc = "Sprints en cinta", "Cardio de alta intensidad para quemar grasa."
            case ("Mantener forma", "Intermedio"):
                nombre, desc = "Planchas laterales", "Fortalece el core y mejora el equilibrio."
            case _:
                nombre, desc = "Sentadillas", "Nunca fallan, cuestan, pero son efectivas."

        # Mostrar en columnas (con imagen)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("Indicaciones")  # Columna vacía
            try:
                image = Image.open("imagengimnasio.jpg")  # Intenta abrir la imagen
                st.image(image, caption="¡Mi imagen genial!", use_container_width=True)  # Usamos use_container_width
            except Exception as e:
                st.error(f"Error al cargar la imagen: {e}")  # Muestra un mensaje de error si no se puede cargar la imagen
        with col2:
            st.write(f"### {nombre}")
            st.write(desc)

        # Encuesta
        st.markdown("---")
        st.subheader("📣 ¿Te ha servido esta recomendación?")
        utilidad = st.radio("Tu opinión nos importa:", ["Sí, me ha ayudado", "Más o menos", "No mucho"], key="feedback")

        if utilidad:
            if utilidad == "Sí, me ha ayudado":
                st.success("¡Genial! Nos alegra ayudarte 💪")
            elif utilidad == "Más o menos":
                st.info("Gracias por tu feedback. Seguiremos mejorando 🛠️")
            else:
                st.error("Lástima 😞 ¡Seguiremos dándolo todo para hacerlo mejor!")

    else:
        st.warning("👀 Por favor, selecciona un objetivo para comenzar.")

if __name__ == "__main__":
    mostrar_recomendador()
