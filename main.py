import torch
from transformers import DistilBertForSequenceClassification
from utils.preprocess import tokenize_texts
from utils.spotify_api import get_playlist_for_emotion
import streamlit as st

# Charger le modèle pré-entraîné pour le prototype
model_name = 'distilbert-base-uncased-finetuned-sst-2-english'  # modèle sentiment général (remplacer plus tard par émotions)
model = DistilBertForSequenceClassification.from_pretrained(model_name)
model.eval()

# Fonction pour prédire l'émotion
def predict_emotion(text):
    tokens = tokenize_texts([text])
    with torch.no_grad():
        outputs = model(**tokens)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    # Pour prototype, on map sentiment → émotion simplifiée
    mapping = {0: "sadness", 1: "joy"}
    return mapping.get(predicted_class, "joy")

# Interface Streamlit
st.title("🎵 MoodFit — Playlist selon ton humeur")
user_text = st.text_area("Écris ton texte ici :")
if st.button("MoodFit !"):
    emotion = predict_emotion(user_text)
    st.write(f"**Émotion détectée :** {emotion}")
    playlist = get_playlist_for_emotion(emotion)
    st.write(f"**Playlist recommandée :** [Ouvrir sur Spotify]({playlist})")
