# API_Gcloud_Streamlit
Generaremos un modelo SVM y lo pondremos en producción usando Streamlit y Google Cloud. El modelo SVM permitirá recomendar un tipo de cultivo dependiendo de características del suelo y ambientales.

##  1. Entrenamiento del modelo
Entrenamos el modelo SVM usando el siguiente cuaderno de colab
    
   [CropPrediction.ipynb](https://github.com/DavidReveloLuna/API_Gcloud_Streamlit/blob/master/CropPrediction.ipynb)

##  2. Producción en servidor local - preparación del entorno

Creamos un entorno con python 3.7, e instalamos las dependencias necesarias.

    $   conda create -n api_sagulpa
    $   conda activate api_sagulpa
    $   conda install python=3.7
    $   pip install -r requirements.txt
    $   streamlit run app.py
    
  ![Screenshot](https://github.com/DavidReveloLuna/API_Gcloud_Streamlit/blob/master/assets/Screenshot.png)
