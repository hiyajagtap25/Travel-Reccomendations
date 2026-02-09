import streamlit as st # type: ignore
import functions as fn

# Page Configuration
st.set_page_config(
    page_title="Travel Recommendations | Discover Your Next Adventure",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Elegant Travel Theme
st.markdown("""
<style>
    /* Import Premium Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #0f1419 100%);
        color: #e8e8e8;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title Styling */
    h1 {
        font-family: 'Playfair Display', serif !important;
        font-size: 4.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #d4af7e 0%, #e8d5b0 50%, #d4af7e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.02em;
        animation: fadeInDown 0.8s ease-out;
        text-transform: uppercase;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #b8956a;
        font-weight: 300;
        margin-bottom: 3rem;
        letter-spacing: 0.1em;
        animation: fadeIn 1s ease-out 0.3s both;
        text-transform: uppercase;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #151b27 0%, #0f1419 100%);
        border-right: 2px solid rgba(212, 175, 126, 0.15);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Sidebar Title */
    [data-testid="stSidebar"] h1 {
        font-size: 1.8rem !important;
        color: #d4af7e;
        text-align: left;
        margin-bottom: 2rem;
    }
    
    /* Selectbox Styling */
    .stSelectbox label {
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #e8e8e8 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    
    .stSelectbox > div > div {
        background: rgba(212, 175, 126, 0.08);
        border: 2px solid rgba(212, 175, 126, 0.25);
        border-radius: 12px;
        color: #e8e8e8;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #d4af7e;
        background: rgba(212, 175, 126, 0.12);
        box-shadow: 0 0 20px rgba(212, 175, 126, 0.15);
        transform: translateY(-2px);
    }
    
    /* Header Styling */
    h2 {
        font-family: 'Playfair Display', serif !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #e8e8e8 !important;
        margin-top: 2rem !important;
        margin-bottom: 1.5rem !important;
        text-align: center;
        text-transform: capitalize;
        position: relative;
        animation: slideInLeft 0.6s ease-out;
    }
    
    h2::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, transparent, #d4af7e, transparent);
        border-radius: 2px;
    }
    
    /* Section Title */
    h3 {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #b8956a !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Content Container */
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* Places Card Container */
    .places-container {
        background: linear-gradient(135deg, rgba(212, 175, 126, 0.05) 0%, rgba(21, 27, 39, 0.6) 100%);
        border: 2px solid rgba(212, 175, 126, 0.15);
        border-radius: 20px;
        padding: 2.5rem;
        margin-top: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(212, 175, 126, 0.08);
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Places List */
    .place-item {
        background: rgba(212, 175, 126, 0.06);
        border-left: 4px solid #b8956a;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 500;
        color: #e8e8e8;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .place-item::before {
        content: '✦';
        margin-right: 1rem;
        font-size: 1.3rem;
        color: #d4af7e;
    }
    
    .place-item::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(212, 175, 126, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .place-item:hover {
        background: rgba(212, 175, 126, 0.1);
        border-left-width: 6px;
        border-left-color: #d4af7e;
        transform: translateX(10px);
        box-shadow: 0 4px 20px rgba(212, 175, 126, 0.15);
    }
    
    .place-item:hover::after {
        left: 100%;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Loading Animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
    }
    
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 4px solid rgba(212, 175, 126, 0.1);
        border-top: 4px solid #d4af7e;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        h1 {
            font-size: 2.5rem !important;
        }
        
        h2 {
            font-size: 2rem !important;
        }
        
        .places-container {
            padding: 1.5rem;
        }
        
        .place-item {
            padding: 1rem;
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1>Travel Recommendations</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover Your Next Adventure</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🌍 Select Destination")
    country = st.selectbox(
        "Choose A Country",
        ["India", "USA", "China", "Brazil", "Canada", "Italy", "Mexico"],
        help="Select a country to explore famous destinations"
    )
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; margin-top: 2rem; color: rgba(255, 255, 255, 0.5); font-size: 0.9rem;'>
        <p>✨ Powered by AI</p>
        <p style='font-size: 0.8rem; margin-top: 0.5rem;'>Explore the world's most beautiful destinations</p>
    </div>
    """, unsafe_allow_html=True)

# Main Content
if country:
    with st.spinner(''):
        response = fn.generate_state_destinations(country)
        
        # State/Region Header
        st.markdown(f"<h2> {response['state_name']}</h2>", unsafe_allow_html=True)
        
        # Build discovery card HTML
        places_list = response['places'].split(",")
        places_html = "".join([f"<div class='place-item'>{p.strip().title()}</div>" for p in places_list if p.strip()])
        
        discovery_card_html = f"""
        <div class='places-container'>
            <div style='text-align: center; margin-bottom: 2rem;'>
                <p style='color: rgba(255,255,255,0.7); font-size: 1.1rem; font-style: italic; line-height: 1.6; max-width: 800px; margin: 0 auto;'>
                    "{response.get('description', '')}"
                </p>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 1.5rem;'>
                <div style='height: 1px; flex-grow: 1; background: linear-gradient(90deg, transparent, rgba(178, 145, 103));'></div>
                <h3 style='margin: 0 1.5rem; white-space: nowrap;'>🌟 Famous Places To Visit</h3>
                <div style='height: 1px; flex-grow: 1; background: linear-gradient(90deg, rgba(178, 145, 103), transparent);'></div>
            </div>
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;'>
                {places_html}
            </div>
        </div>
        """
        
        st.markdown(discovery_card_html, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align: center; padding: 4rem 2rem; color: rgba(255, 255, 255, 0.6);'>
        <h3 style='color: #ff6090;'>👈 Select a country from the sidebar to begin your journey</h3>
        <p style='margin-top: 1rem; font-size: 1.1rem;'>Discover amazing destinations around the world</p>
    </div>
    """, unsafe_allow_html=True)

