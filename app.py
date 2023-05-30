import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Path del modelo preentrenado
MODEL_PATH = 'models/pickle_model.pkl'

# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1,-1)
    preds = model.predict(x)
    return preds

def main():
    
    local_css("styles.css")
    
    model = ''

    # Se carga el modelo
    if model == '':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Lista de países con sus identificadores numéricos asignados previamente
    paises = {
        'Alemania': 1,
        'Austria': 2,
        'Bélgica': 3,
        'Brasil': 4,
        'Bulgaria': 5,
        'Dinamarca': 6,
        'Eslovaquia': 7,
        'Eslovenia': 8,
        'Países Bajos': 9,
        'Francia': 10,
        'Reino Unido': 11,
        'Suecia': 12,
        'Rumanía': 13,
        'Finlandia': 14,
        'Italia': 15,
        'Irlanda': 16,
        'Suiza': 17,
        'Polonia': 18,
        'Rep. Checa': 19,
        'Hungría': 20,
        'Portugal': 21,
        'Estonia': 22,
        'Macedonia': 23,
        'Grecia': 24,
        'Noruega': 25,
        'USA/Canada': 26,
        'Islandia': 27,
        'Lituania': 28,
        'Japón': 29,
        'Serbia': 30
    }
    
    # Título
    html_temp = """
    <h1>Demanda de alquileres sitycleta por países</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Lista de días del 1 al 31
    dias = list(range(1, 32))

    # Lecctura de datos
    P = st.selectbox("Día:", dias)
    K = st.text_input("prec:")
    Temp = st.text_input("presMax:")
    Hum = st.text_input("presMin:")
    pH = st.text_input("tmax:")
    rain = st.text_input("tmed:")
    rai = st.text_input("tmin:")
    ra = st.text_input("velmedia:")
    r = st.text_input("place:")
    
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        predictions = []
        for pais in paises:
            x_in = [
                paises[pais],
                np.float_(P),
                np.float_(K),
                np.float_(Temp),
                np.float_(Hum),
                np.float_(rai),
                np.float_(ra),
                np.float_(r),
                np.float_(pH),
                np.float_(rain)
            ]
            predictS = model_prediction(x_in, model)
            predictions.append((pais, predictS[0]))

        st.success('Resultados de predicción:')
        for pais, prediction in predictions:
            st.write(pais,':', prediction)
            st.write('---')


if __name__ == '__main__':
    main()