import streamlit as st
from PIL import Image
import pytesseract
import io

# ── Configuration de la page ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Manuscrit → Texte",
    page_icon="📜",
    layout="centered"
)

# ── CSS personnalisé ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
}

.main {
    background: #faf8f4;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
}

.titre-app {
    text-align: center;
    padding: 2rem 0 0.5rem 0;
}

.titre-app h1 {
    font-size: 2.8rem;
    color: #2c1810;
    margin-bottom: 0.2rem;
}

.titre-app p {
    color: #7a6652;
    font-size: 1.1rem;
    font-weight: 300;
}

.separateur {
    border: none;
    border-top: 2px solid #e8ddd0;
    margin: 1.5rem 0;
}

.resultat-box {
    background: #ffffff;
    border: 1px solid #e0d5c8;
    border-left: 4px solid #8b5e3c;
    border-radius: 4px;
    padding: 1.5rem;
    margin-top: 1rem;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 1rem;
    line-height: 1.7;
    color: #2c1810;
    white-space: pre-wrap;
}

.stButton > button {
    background-color: #8b5e3c;
    color: white;
    border: none;
    padding: 0.6rem 2rem;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 1rem;
    border-radius: 3px;
    cursor: pointer;
    width: 100%;
    transition: background 0.2s;
}

.stButton > button:hover {
    background-color: #6d4a2f;
}

.info-box {
    background: #f0ebe4;
    border-radius: 4px;
    padding: 0.8rem 1rem;
    color: #5a4a3a;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ── En-tête ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="titre-app">
    <h1>📜 Manuscrit → Texte</h1>
    <p>Transformez vos manuscrits en texte numérique en quelques secondes</p>
</div>
<hr class="separateur">
""", unsafe_allow_html=True)

# ── Upload de l'image ──────────────────────────────────────────────────────────
st.markdown("### 📁 Charger votre manuscrit")

st.markdown("""
<div class="info-box">
    💡 <strong>Conseils pour de meilleurs résultats :</strong> image bien éclairée, nette, fond blanc de préférence.
</div>
""", unsafe_allow_html=True)

fichier = st.file_uploader(
    "Glissez une image ici ou cliquez pour parcourir",
    type=["png", "jpg", "jpeg", "tiff", "bmp", "webp"],
    label_visibility="collapsed"
)

if fichier:
    image = Image.open(fichier)

    # Affichage de l'image uploadée
    st.markdown("### 🖼️ Aperçu du manuscrit")
    st.image(image, use_container_width=True)

    st.markdown("<hr class='separateur'>", unsafe_allow_html=True)

    # ── Bouton d'extraction ────────────────────────────────────────────────────
    if st.button("✨ Extraire le texte"):
        with st.spinner("Lecture du manuscrit en cours..."):
            try:
                # Configuration Tesseract pour le français
                config_tesseract = "--oem 3 --psm 6"
                texte = pytesseract.image_to_string(
                    image,
                    lang="fra",
                    config=config_tesseract
                )

                texte = texte.strip()

                if texte:
                    st.markdown("### 📝 Texte extrait")
                    st.markdown(
                        f'<div class="resultat-box">{texte}</div>',
                        unsafe_allow_html=True
                    )

                    # Bouton de téléchargement
                    st.download_button(
                        label="⬇️ Télécharger le texte (.txt)",
                        data=texte.encode("utf-8"),
                        file_name="manuscrit_extrait.txt",
                        mime="text/plain"
                    )

                    # Statistiques rapides
                    nb_mots = len(texte.split())
                    nb_chars = len(texte)
                    col1, col2 = st.columns(2)
                    col1.metric("Mots détectés", nb_mots)
                    col2.metric("Caractères", nb_chars)

                else:
                    st.warning("⚠️ Aucun texte détecté. Essayez avec une image plus nette ou mieux éclairée.")

            except Exception as e:
                st.error(f"❌ Erreur lors de l'extraction : {e}")
                st.info("Vérifiez que Tesseract est bien installé avec le pack de langue française.")

else:
    st.markdown("""
    <div style="text-align:center; padding: 3rem; color: #a89880;">
        <div style="font-size: 4rem;">📄</div>
        <p>Aucune image chargée pour l'instant</p>
    </div>
    """, unsafe_allow_html=True)

# ── Pied de page ──────────────────────────────────────────────────────────────
st.markdown("<hr class='separateur'>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align:center; color:#a89880; font-size:0.85rem;">
    Propulsé par Tesseract OCR • Langue : Français
</p>
""", unsafe_allow_html=True)
