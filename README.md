#  MoodFit – Emotion Detection & Music Recommendation

**MoodFit** est une application IA qui détecte ton émotion à partir d’un texte et te recommande une chanson adaptée   
Basé sur **DistilBERT** avec une **Focal Loss** pour gérer le déséquilibre des classes, et une interface simple en **Streamlit**.

---

##  Fonctionnalités
-  Détection d’émotions (joie, peur, tristesse, amour, colère, surprise)
-  Entraînement avec Focal Loss
-  Visualisation de la matrice de confusion
-  Sauvegarde et chargement du modèle
-  Interface Streamlit interactive

---

##  Installation

```bash
git clone https://github.com/oumaymaBelaid/MoodFit.git
cd MoodFit
pip install -r requirements.txt
