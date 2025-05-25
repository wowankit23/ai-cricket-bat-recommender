import streamlit as st

# Bat image URLs
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

# Bat Size Data (updated to include height in feet)
bat_sizes = [
    {"Size": "0", "Length (in)": "24-27", "Player Height (cm)": "Below 122", "Player Height (ft)": "Below 4'", "Age": "3-4 years"},
    {"Size": "1", "Length (in)": "27-28", "Player Height (cm)": "122-129", "Player Height (ft)": "4'0\" - 4'2\"", "Age": "4-5 years"},
    {"Size": "2", "Length (in)": "29-30", "Player Height (cm)": "130-136", "Player Height (ft)": "4'3\" - 4'5\"", "Age": "6-7 years"},
    {"Size": "3", "Length (in)": "30-31", "Player Height (cm)": "137-144", "Player Height (ft)": "4'6\" - 4'8\"", "Age": "8-9 years"},
    {"Size": "4", "Length (in)": "31-32", "Player Height (cm)": "145-151", "Player Height (ft)": "4'9\" - 4'11\"", "Age": "9-10 years"},
    {"Size": "5", "Length (in)": "32-33", "Player Height (cm)": "152-159", "Player Height (ft)": "5'0\" - 5'2\"", "Age": "10-11 years"},
    {"Size": "6", "Length (in)": "33-34", "Player Height (cm)": "160-164", "Player Height (ft)": "5'3\" - 5'4\"", "Age": "11-12 years"},
    {"Size": "Harrow", "Length (in)": "32-33", "Player Height (cm)": "165-169", "Player Height (ft)": "5'5\" - 5'6\"", "Age": "12-14 years"},
    {"Size": "Short Handle", "Length (in)": "32-33.5", "Player Height (cm)": "170-182", "Player Height (ft)": "5'7\" - 5'11\"", "Age": "15+ years"},
    {"Size": "Long Handle", "Length (in)": "33.5-34.5", "Player Height (cm)": "183+", "Player Height (ft)": "6'0\"+", "Age": "15+ years"},
]

# Batting style logic
def suggest_batting_style(age_group, experience, build, preferred_shots, match_format, batting_position):
    experience = experience.lower()
    build = build.lower()
    preferred_shots = preferred_shots.lower()
    match_format = match_format.lower()

    if experience == "beginner" or match_format == "test":
        if preferred_shots == "front foot" or build == "light":
            return "Defensive"
    if experience == "professional" or match_format in ["t20", "odi"]:
        if preferred_shots == "back foot" or build == "strong":
            return "Aggressive"
    if experience == "intermediate":
        return "All-Rounder"
    return "All-Rounder"

# Bat size suggestion based on cm
def suggest_bat_size(height_cm):
    for size in bat_sizes:
        height_range = size["Player Height (cm)"]
        if "Below" in height_range:
            limit = int(height_range.split(" ")[1])
            if height_cm < limit:
                return size["Size"]
        elif "+" in height_range:
            limit = int(height_range.replace("+", ""))
            if height_cm >= limit:
                return size["Size"]
        else:
            low, high = map(int, height_range.split("-"))
            if low <= height_cm <= high:
                return size["Size"]
    return "Unknown"

# Streamlit UI
st.set_page_config(page_title="AI Bat Style & Size Recommender", layout="centered")
st.title("🏏 AI-Powered Cricket Bat Recommender")

with st.form("profile_form"):
    st.subheader("Player Profile")
    age_group = st.selectbox("Age Group", ["Junior", "Adult"])
    experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Professional"])
    build = st.selectbox("Player Build", ["Light", "Medium", "Strong"])
    preferred_shots = st.selectbox("Preferred Shots", ["Front foot", "Back foot", "Both"], help="Choose the type of shots you play most confidently.")
    match_format = st.selectbox("Match Format", ["Test", "ODI", "T20"])
    batting_position = st.selectbox("Batting Position", ["Opener", "Middle order", "Lower order"])
    
    st.markdown("### Player Height")
    height_ft = st.number_input("Feet", min_value=3, max_value=8, step=1)
    height_in = st.number_input("Inches", min_value=0, max_value=11, step=1)
    height_cm = round((height_ft * 30.48) + (height_in * 2.54), 1)

    submit = st.form_submit_button("Suggest Bat & Size")

if submit:
    style = suggest_batting_style(age_group, experience, build, preferred_shots, match_format, batting_position)
    bat_size = suggest_bat_size(height_cm)

    st.success(f"**Suggested Batting Style:** {style}")
    st.success(f"**Recommended Bat Size:** {bat_size}")
    st.info(f"📏 Player Height: {height_ft}′{height_in}″ ({height_cm} cm)")

    image_url = bat_images.get(style)
    if image_url:
        st.image(image_url, caption=f"{style} Bat Preview", use_container_width=True)
    else:
        st.warning("Image not available for this bat style.")

    st.info(bat_descriptions.get(style, "No description available."))
    st.markdown(f"[🛒 Order Recommended Bat]({bat_links.get(style, '#')})", unsafe_allow_html=True)

    with st.expander("📏 See Full Bat Size Chart"):
        st.table(bat_sizes)
