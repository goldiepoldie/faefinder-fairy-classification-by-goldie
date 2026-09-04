import streamlit as st
import pandas as pd
import joblib
import base64

# Load background image
with open("fairy_background.jpg", "rb") as file:
    background_image = base64.b64encode(file.read()).decode()

# 🌸 FaeFinder Custom Styling
st.markdown(f"""
<style>

    /* 🌿 Main Background */
    .stApp {{
        background-image:
            linear-gradient(
                rgba(248, 239, 232, 0.82),
                rgba(232, 238, 229, 0.82)
            ),
            url("data:image/jpeg;base64,{background_image}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 💗 Main Title */
    h1 {{
        color: #5b514b;
        font-family: Georgia, serif;
        font-size: 48px !important;
        letter-spacing: 2px;
    }}

    /* 🌸 Section Headings */
    h2 {{
        color: #5b514b !important;
        font-family: Georgia, serif;
        font-size: 28px !important;
        letter-spacing: 1px;
        margin-top: 25px;
        margin-bottom: 15px;
    }}

    /* ✨ Normal Text */
    p {{
        color: #665d57;
        font-family: Georgia, serif;
    }}

    /* 🎀 Input Labels */
    label {{
        color: #665d57 !important;
        font-family: Georgia, serif;
    }}

    /* 🌸 Dropdowns */
    div[data-baseweb="select"] > div {{
        background-color: #f5eee8;
        border: 1px solid #d6c7bd;
        border-radius: 10px;
    }}

       /* 🌿 Fairy-style Sliders */

    /* Slider track */
    div[data-testid="stSlider"] [data-baseweb="slider"] {{
        padding-top: 5px;
        padding-bottom: 5px;
    }}

    /* Full slider track */
    div[data-testid="stSlider"] [data-baseweb="slider"] > div {{
        background: #d8d5c8 !important;
    }}

    /* Selected portion of slider */
    div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {{
        background: #8f9f82 !important;
    }}

    /* Slider knob */
    div[data-testid="stSlider"] [role="slider"] {{
        background-color: #8f9f82 !important;
        border: 3px solid #f5eee8 !important;
        box-shadow: 0 2px 7px rgba(90, 75, 65, 0.25);
    }}

    /* Slider number */
    div[data-testid="stSlider"] [data-testid="stThumbValue"] {{
        color: #665d57 !important;
        font-family: Georgia, serif !important;
    }}
    
    /* ✨ Button */
    .stButton > button {{
        background-color: #8f9f82;
        color: #fffaf5;
        border: 1px solid #8f9f82;
        border-radius: 25px;
        padding: 10px 28px;
        font-family: Georgia, serif;
        font-size: 16px;
        transition: all 0.3s ease;
    }}

    .stButton > button:hover {{
        background-color: #78896c;
        border-color: #78896c;
        color: #fffaf5;
    }}

    .stButton > button:focus {{
        background-color: #8f9f82;
        border-color: #8f9f82;
        color: #fffaf5;
        box-shadow: 0 0 0 2px rgba(143, 159, 130, 0.25);
    }}

    /* 🧚 Fairy Result Card */
    .fairy-result {{
        background: rgba(255, 248, 242, 0.94);
        border: 1px solid rgba(180, 160, 145, 0.6);
        border-radius: 22px;
        padding: 30px;
        margin-top: 25px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(90, 75, 65, 0.15);
    }}

    .fairy-result-title {{
        color: #514943;
        font-family: Georgia, serif;
        font-size: 30px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }}

    .fairy-result-text {{
        color: #776b63;
        font-family: Georgia, serif;
        font-size: 17px;
        font-style: italic;
    }}

</style>
""", unsafe_allow_html=True)


# Load model and label encoders
model = joblib.load("fairy_type_prediction.pkl")
label_encoders = joblib.load("fairy_label_encoders.pkl")


# 💗 Title
st.title("💗 FaeFinder")
st.write("✨ Discover which type of fairy you are! ✨")


# 🌿 Personality Inputs
st.markdown("## 🌿 Your Magical Traits")

creativity = st.slider("🎨 Creativity", 1, 10, 5)
adventure = st.slider("🌿 Adventure", 1, 10, 5)
social_energy = st.slider("💃 Social Energy", 1, 10, 5)
nature_love = st.slider("🌱 Love for Nature", 1, 10, 5)
dreaminess = st.slider("🌙 Dreaminess", 1, 10, 5)
confidence = st.slider("✨ Confidence", 1, 10, 5)
emotionality = st.slider("💞 Emotionality", 1, 10, 5)
curiosity = st.slider("🔮 Curiosity", 1, 10, 5)


# 🌸 Favorite Preferences
st.markdown("## 🌸 Your Enchanted Preferences")

favorite_environment = st.selectbox(
    "🏡 What's your favorite environment?",
    label_encoders["Favorite_Environment"].classes_
)

favorite_season = st.selectbox(
    "🌸 What's your favorite season?",
    label_encoders["Favorite_Season"].classes_
)

favorite_time = st.selectbox(
    "🌙 What's your favorite time of day?",
    label_encoders["Favorite_Time"].classes_
)

favorite_color = st.selectbox(
    "🎀 What's your favorite color?",
    label_encoders["Favorite_Color"].classes_
)


# Encode categorical inputs
favorite_environment_encoded = label_encoders["Favorite_Environment"].transform(
    [favorite_environment]
)[0]

favorite_season_encoded = label_encoders["Favorite_Season"].transform(
    [favorite_season]
)[0]

favorite_time_encoded = label_encoders["Favorite_Time"].transform(
    [favorite_time]
)[0]

favorite_color_encoded = label_encoders["Favorite_Color"].transform(
    [favorite_color]
)[0]


# Create DataFrame
df = pd.DataFrame({
    "Creativity": [creativity],
    "Adventure": [adventure],
    "Social_Energy": [social_energy],
    "Nature_Love": [nature_love],
    "Dreaminess": [dreaminess],
    "Confidence": [confidence],
    "Emotionality": [emotionality],
    "Curiosity": [curiosity],
    "Favorite_Environment": [favorite_environment_encoded],
    "Favorite_Season": [favorite_season_encoded],
    "Favorite_Time": [favorite_time_encoded],
    "Favorite_Color": [favorite_color_encoded]
})


# 🧚 Prediction
if st.button("✨ Discover My Fairy Type ✨"):

    prediction = model.predict(df)[0]

    fairy_type = label_encoders["Fairy_Type"].inverse_transform(
        [prediction]
    )[0]

    fairy_emojis = {
        "Water Fairy": "💧",
        "Forest Fairy": "🌲",
        "Flower Fairy": "🌸",
        "Moon Fairy": "🌙",
        "Starlight Fairy": "⭐",
        "Fire Fairy": "🔥"
    }

    fairy_descriptions = {
        "Water Fairy": "💧 You are calm, adaptable, and deeply connected to your emotions. Like water, you can flow through any situation with grace.",

        "Forest Fairy": "🌲 You are adventurous, grounded, and happiest when surrounded by nature. You have a strong connection with the world around you.",

        "Flower Fairy": "🌸 You are creative, gentle, and drawn to beauty. You bring color, warmth, and happiness wherever you go.",

        "Moon Fairy": "🌙 You are dreamy, intuitive, and mysterious. You find magic in quiet moments and feel most at home under the night sky.",

        "Starlight Fairy": "⭐ You are curious, imaginative, and full of wonder. You are always dreaming about new possibilities and adventures.",

        "Fire Fairy": "🔥 You are confident, passionate, and energetic. You have a bright personality and aren't afraid to let yourself shine!"
    }

    # 🧚 Fairy Result Card
    st.markdown(
        f"""
        <div class="fairy-result">
            <div class="fairy-result-title">
                {fairy_emojis[fairy_type]} You are a {fairy_type}! {fairy_emojis[fairy_type]}
            </div>

            <div class="fairy-result-text">
                ✨ Your magical personality has been revealed ✨
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 🌸 Fairy Personality
    st.markdown(
        f"""
        ### ✨ Your Fairy Personality

        {fairy_descriptions[fairy_type]}

        ✨ Welcome to the magical world of **{fairy_type}**! ✨
        """
    )
