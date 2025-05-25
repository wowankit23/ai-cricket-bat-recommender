import streamlit as st

# Bat image URLs (update with real hosted images or use local static/images if self-hosted)
bat_images = {
    "Defensive": "https://yourdomain.com/images/bat_defensive.jpg",
    "Aggressive": "https://yourdomain.com/images/bat_aggressive.jpg",
    "All-Rounder": "https://yourdomain.com/images/bat_allrounder.jpg"
}

bat_descriptions = {
    "Defensive": "Ideal for front-foot dominant players and Test formats. Lightweight and balanced.",
    "Aggressive": "Perfect for big hitters in T20s and ODIs. Thick edges and powerful sweet spot.",
    "All-Rounder": "Balanced for all conditions. Versatile pickup and sweet spot."
}

bat_links = {
    "Defensive": "https://yourshop.com/product/defensive-bat",
    "Aggressive": "https://yourshop.com/product/aggressive-bat",
    "All-Rounder": "https://yourshop.com/product/allrounder-bat"
}

# Logic
def suggest_batting_style(age_group, experience, build, preferred_shots, match_format, batting_position):
    if experience.lower() == "beginner" or match_format.lower() == "test":
        if preferred_shots.lower() == "front foot" or build.lower() == "light":
            return "Defensive"
    if experience.lower() == "professional" or match_format.lower() in ["t20", "odi"]:
        if preferred_shots.lower() == "back foot" or build.lower() == "strong":
            return "Aggressive"
    if experience.lower() == "intermediate":
        if preferred_shots.lower() == "both" or build.lower() == "medium":
            return "All-Rounder"
    return "All-Rounder"

# Streamlit UI
st.set_page_config(page_title="AI Bat Style Selector", layout="centered")
st.title("AI-Powered Cricket Bat Recommender")

with st.form("profile_form"):
    st.subheader("Player Profile")
    age_group = st.selectbox("Age Group", ["Junior", "Adult"])
    experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Professional"])
    build = st.selectbox("Player Build", ["Light", "Medium", "Strong"])
    preferred_shots = st.selectbox("Preferred Shots", ["Front foot", "Back foot", "Both"])
    match_format = st.selectbox("Match Format", ["Test", "ODI", "T20"])
    batting_position = st.selectbox("Batting Position", ["Opener", "Middle order", "Lower order"])

    submit = st.form_submit_button("Suggest Batting Style")

if submit:
    style = suggest_batting_style(age_group, experience, build, preferred_shots, match_format, batting_position)
    st.success(f"**Suggested Batting Style: {style}**")

    st.image(bat_images.get(style, ""), caption=f"{style} Bat Preview", use_container_width=True)
    st.info(bat_descriptions.get(style, ""))

    st.markdown(f"[Order Recommended Bat]({bat_links.get(style, '#')})", unsafe_allow_html=True)
