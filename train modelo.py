# Crear un modelo de clasificación de texto y guardarlo en un archivo en formato .pkl
# se puede mejroar este modelo tomando los texts y labels de archivos externos
# se puede mejorar este modelo tomando los textos y labels de una base de datos
# se puede mejorar este modelo tomando los textos y labels de una API
# se puede mejorar este modelo tomando los textos y labels de un servicio web
# se puede mejorar este modelo tomando los textos y labels de un servicio en la nube
#
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Datos de ejemplo
texts = ["This is a document about machine learning.",
         "This document is about deep learning.",
         "This is a document about AI.",
         "This document is about data science."]
labels = ["machine learning", "deep learning", "AI", "data science"]

# Crear un pipeline de vectorización y clasificación
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Entrenar el modelo
model.fit(texts, labels)

# Guardar el modelo
model_path = r'C:\Users\marco\Desktop\text_classifier_model.pkl'  #ojo con la ruta del archivo que contiene el modelo
joblib.dump(model, model_path)
print(f"Modelo guardado en {model_path}")