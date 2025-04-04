import streamlit as st

def mostrar_distancia():
    st.title("🚶‍♂️ Distancia Recorrida y Calorías Quemadas")

    # Pedir al usuario la cantidad de pasos dados
    pasos = st.number_input("Introduce los pasos dados:", min_value=0, value=1000, step=100)
    
    # Calcular la distancia recorrida, asumiendo que 2 pasos = 1 metro
    distancia = pasos / 2  # 2 pasos = 1 metro
    
    # Cálculo de las calorías quemadas (suponemos 40 calorías por cada 1000 pasos)
    calorias_quemadas = (pasos / 1000) * 40
    
    # Mostrar el resultado
    st.write(f"Has recorrido {distancia:.2f} metros.")
    st.write(f"Has quemado aproximadamente {calorias_quemadas:.2f} calorías.")

if __name__ == "__main__":
    mostrar_distancia()
