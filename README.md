# 📜 Manuscrit → Texte

Application Streamlit pour transformer des images de manuscrits en texte numérique via OCR (Tesseract).

---

## 🚀 Déploiement sur Streamlit Community Cloud

### Étape 1 — Préparer GitHub
1. Crée un compte sur [github.com](https://github.com)
2. Crée un nouveau repository (ex: `manuscrit-ocr`)
3. Uploade les 3 fichiers :
   - `app.py`
   - `requirements.txt`
   - `packages.txt`

### Étape 2 — Déployer
1. Va sur [share.streamlit.io](https://share.streamlit.io)
2. Connecte ton compte GitHub
3. Sélectionne ton repository
4. Fichier principal : `app.py`
5. Clique **Deploy** ✅

Ton app sera disponible sur une URL du type :
`https://ton-app.streamlit.app`

---

## 💻 Lancer en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

> ⚠️ En local, Tesseract doit être installé sur ton système :
> - **Windows** : [UB Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
> - **Mac** : `brew install tesseract tesseract-lang`
> - **Linux** : `sudo apt install tesseract-ocr tesseract-ocr-fra`

---

## 📦 Structure du projet

```
manuscrit-ocr/
├── app.py            ← Application principale
├── requirements.txt  ← Bibliothèques Python
└── packages.txt      ← Paquets système (Tesseract)
```
