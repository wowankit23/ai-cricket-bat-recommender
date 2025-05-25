import streamlit as st

# --- Page config ---
st.set_page_config(page_title="🏏 AI Cricket Bat Recommender", layout="centered")

# --- Custom Color Theme ---
st.markdown("""
    <style>
        /* App background */
        .main {
            background-color: #f0f7ff;
        }

        /* Font customization */
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            color: #333;
        }

        /* Titles and headers */
        h1, h2, h3 {
            color: #1f4e79;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 16px;
        }

        div.stButton > button:hover {
            background-color: #135a96;
            transition: 0.3s ease;
        }

        /* Success message */
        .stAlert-success {
            background-color: #d0f0c0;
            border-left: 5px solid #34a853;
        }

        /* Info message */
        .stAlert-info {
            background-color: #e0f3ff;
            border-left: 5px solid #1f77b4;
        }

        /* Sidebar customization */
        section[data-testid="stSidebar"] {
            background-color: #dceefb;
            border-right: 2px solid #c4e1f5;
        }

        /* Image container spacing */
        .element-container img {
            border-radius: 10px;
            margin-top: 10px;
        }

        /* Table styling */
        .stTable tbody tr:nth-child(even) {
            background-color: #eaf4fd;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar (optional) ---
st.sidebar.image("https://yourdomain.com/logo.png", use_container_width=True)
st.sidebar.title("🏏 Cricket Gear AI")
st.sidebar.markdown("Get your **perfect bat** based on your play style and height.")

# --- Data ---
bat_images = {
    "Defensive": "https://www.laverwood.com/wp-content/uploads/2020/09/Sweet-spot.png",
    "Aggressive": "https://www.laverwood.com/wp-content/uploads/2020/09/Sweet-spot.png",
    "All-Rounder": "https://www.laverwood.com/wp-content/uploads/2020/09/Sweet-spot.png"
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
bat_sizes = [
    {"Size": "0", "Length (in)": "24-27", "Player Height (cm)": "Below 122", "Player Height (ft)": "Below 4′0″", "Age": "3-4 years"},
    {"Size": "1", "Length (in)": "27-28", "Player Height (cm)": "122-129", "Player Height (ft)": "4′0″ - 4′2″", "Age": "4-5 years"},
    {"Size": "2", "Length (in)": "29-30", "Player Height (cm)": "130-136", "Player Height (ft)": "4′3″ - 4′5″", "Age": "6-7 years"},
    {"Size": "3", "Length (in)": "30-31", "Player Height (cm)": "137-144", "Player Height (ft)": "4′6″ - 4′8″", "Age": "8-9 years"},
    {"Size": "4", "Length (in)": "31-32", "Player Height (cm)": "145-151", "Player Height (ft)": "4′9″ - 4′11″", "Age": "9-10 years"},
    {"Size": "5", "Length (in)": "32-33", "Player Height (cm)": "152-159", "Player Height (ft)": "5′0″ - 5′2″", "Age": "10-11 years"},
    {"Size": "6", "Length (in)": "33-34", "Player Height (cm)": "160-164", "Player Height (ft)": "5′3″ - 5′4″", "Age": "11-12 years"},
    {"Size": "Harrow", "Length (in)": "32-33", "Player Height (cm)": "165-169", "Player Height (ft)": "5′5″ - 5′6″", "Age": "12-14 years"},
    {"Size": "Short Handle", "Length (in)": "32-33.5", "Player Height (cm)": "170-182", "Player Height (ft)": "5′7″ - 5′11″", "Age": "15+ years"},
    {"Size": "Long Handle", "Length (in)": "33.5-34.5", "Player Height (cm)": "183+", "Player Height (ft)": "6′0″+", "Age": "15+ years"},
]

# --- Suggestion Logic ---
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

# --- Main Title ---
st.markdown("# 🧠 AI Cricket Bat Recommender")
st.markdown("### Find your perfect bat based on your profile and height.")

# --- Player Profile Form ---
with st.form("profile_form"):
    st.subheader("📋 Player Profile")

    col1, col2 = st.columns(2)
    with col1:
        age_group = st.selectbox("🎂 Age Group", ["Junior", "Adult"])
        build = st.selectbox("💪 Player Build", ["Light", "Medium", "Strong"])
        match_format = st.selectbox("🏏 Match Format", ["Test", "ODI", "T20"])
    with col2:
        experience = st.selectbox("📈 Experience Level", ["Beginner", "Intermediate", "Professional"])
        preferred_shots = st.selectbox("🎯 Preferred Shots", ["Front foot", "Back foot", "Both"])
        batting_position = st.selectbox("🧍‍♂️ Batting Position", ["Opener", "Middle order", "Lower order"])

    st.markdown("### 📐 Player Height")

    if age_group == "Junior":
        st.caption("👦 Typical junior height range: 3′0″ to 5′6″")
        col3, col4 = st.columns(2)
        height_ft = col3.number_input("Feet", min_value=3, max_value=5, value=4, step=1)
        height_in = col4.number_input("Inches", min_value=0, max_value=11, value=6, step=1)
    else:
        st.caption("🧑 Typical adult height range: 4′10″ to 7′0″")
        col3, col4 = st.columns(2)
        height_ft = col3.number_input("Feet", min_value=4, max_value=7, value=5, step=1)
        height_in = col4.number_input("Inches", min_value=0, max_value=11, value=8, step=1)

    height_cm = round((height_ft * 30.48) + (height_in * 2.54), 1)
    submit = st.form_submit_button("🎯 Suggest My Bat")

# --- Results ---
if submit:
    style = suggest_batting_style(age_group, experience, build, preferred_shots, match_format, batting_position)
    bat_size = suggest_bat_size(height_cm)

    st.markdown("---")
    st.subheader("🔍 Recommendation")
    st.success(f"**🏏 Batting Style:** {style}")
    st.success(f"**📏 Recommended Bat Size:** {bat_size}")
    st.info(f"👤 Player Height: `{height_ft}′{height_in}″`  (`{height_cm} cm`)")

    col_img, col_info = st.columns([1, 2])
    with col_img:
        st.image(bat_images.get(style, ""), caption=f"{style} Bat Preview", use_container_width=True)
    with col_info:
        st.markdown(f"📝 **Description:** {bat_descriptions.get(style)}")
        st.markdown(f"[🛒 Order Recommended Bat]({bat_links.get(style, '#')})", unsafe_allow_html=True)

    with st.expander("📊 View Full Bat Size Chart"):
        st.table(bat_sizes)
