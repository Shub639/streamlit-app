import streamlit as st


def get_logo_svg(size=120):
    """Returns an SVG logo for DECIDE."""
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">'
        '<defs>'
        '<linearGradient id="bg_grad" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%" style="stop-color:#3E2723;stop-opacity:1" />'
        '<stop offset="100%" style="stop-color:#6D4C41;stop-opacity:1" />'
        '</linearGradient>'
        '<linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">'
        '<stop offset="0%" style="stop-color:#C4A882;stop-opacity:1" />'
        '<stop offset="100%" style="stop-color:#E8D5B7;stop-opacity:1" />'
        '</linearGradient>'
        '</defs>'
        '<circle cx="100" cy="100" r="95" fill="url(#bg_grad)" />'
        '<circle cx="100" cy="100" r="88" fill="none" stroke="url(#accent)" stroke-width="2" />'
        '<path d="M100 35 L145 60 L145 115 Q145 155 100 175 Q55 155 55 115 L55 60 Z" fill="none" stroke="#C4A882" stroke-width="3" />'
        '<path d="M78 105 L93 120 L125 80" fill="none" stroke="#C4A882" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />'
        '<circle cx="100" cy="42" r="4" fill="#E8D5B7" />'
        '<circle cx="148" cy="70" r="4" fill="#E8D5B7" />'
        '<circle cx="140" cy="140" r="4" fill="#E8D5B7" />'
        '<circle cx="60" cy="140" r="4" fill="#E8D5B7" />'
        '<circle cx="52" cy="70" r="4" fill="#E8D5B7" />'
        '</svg>'
    )


def inject_global_css():
    """Inject all global styles, background, animations."""
    st.markdown("""
    <style>
        /* ===== ANIMATED GRADIENT BACKGROUND ===== */
        .stApp {
            background: linear-gradient(135deg, #FAF6F0 0%, #F0E6D6 25%, #F5EDE3 50%, #EDE0D0 75%, #FAF6F0 100%);
            background-size: 400% 400%;
            animation: bgShift 20s ease infinite;
        }
        @keyframes bgShift {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* ===== HIDE STREAMLIT DEFAULTS ===== */
        [data-testid="stSidebarCollapsedControl"] { display: none; }
        [data-testid="stSidebar"] { display: none; }
        header { visibility: hidden; }
        .block-container { padding-top: 10px !important; }

        /* ===== GLASSMORPHISM CARDS ===== */
        .glass-card {
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 8px 32px rgba(62, 39, 35, 0.08);
            padding: 32px 36px;
            margin-bottom: 24px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .glass-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 48px rgba(62, 39, 35, 0.12);
        }

        /* ===== ANIMATIONS ===== */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInLeft {
            from { opacity: 0; transform: translateX(-40px); }
            to { opacity: 1; transform: translateX(0); }
        }
        @keyframes fadeInRight {
            from { opacity: 0; transform: translateX(40px); }
            to { opacity: 1; transform: translateX(0); }
        }
        @keyframes scaleIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }
        @keyframes float {
            0%   { transform: translateY(0px); }
            50%  { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }
        @keyframes shimmer {
            0%   { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        @keyframes pulseGlow {
            0%   { box-shadow: 0 0 5px rgba(196,168,130,0.2); }
            50%  { box-shadow: 0 0 25px rgba(196,168,130,0.4); }
            100% { box-shadow: 0 0 5px rgba(196,168,130,0.2); }
        }

        /* ===== TYPOGRAPHY ===== */
        .heading-xl {
            font-family: 'Times New Roman', serif;
            font-size: 42px;
            font-weight: bold;
            color: #3E2723;
            text-align: center;
            animation: fadeInUp 0.8s ease-out;
        }
        .heading-lg {
            font-family: 'Times New Roman', serif;
            font-size: 36px;
            font-weight: bold;
            color: #3E2723;
            text-align: center;
            animation: fadeInUp 0.8s ease-out;
        }
        .heading-md {
            font-family: 'Times New Roman', serif;
            font-size: 22px;
            font-weight: bold;
            color: #3E2723;
            text-decoration: underline;
            text-align: center;
            margin-bottom: 14px;
        }
        .subtitle {
            font-family: 'Times New Roman', serif;
            font-size: 16px;
            color: #6D4C41;
            text-align: center;
            font-style: italic;
            margin-bottom: 20px;
        }
        .body-text {
            font-family: 'Times New Roman', serif;
            font-size: 15px;
            color: #444;
            line-height: 1.85;
            text-align: center;
        }

        /* ===== DECORATIVE DIVIDER ===== */
        .gold-divider {
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, #C4A882, #6D4C41);
            margin: 0 auto 35px auto;
            border-radius: 2px;
            animation: scaleIn 0.8s ease-out;
        }

        /* ===== PILLAR CHIPS ===== */
        .pillar-row {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .pillar-chip {
            background: linear-gradient(135deg, #F5EDE3, #E8D5B7);
            border: 1px solid #D4C4B0;
            border-radius: 30px;
            padding: 8px 20px;
            font-family: 'Times New Roman', serif;
            font-size: 13px;
            color: #3E2723;
            font-weight: bold;
            transition: transform 0.2s ease;
        }
        .pillar-chip:hover {
            transform: scale(1.05);
        }

        /* ===== SCORE BADGE ===== */
        .score-badge {
            display: inline-block;
            padding: 8px 24px;
            border-radius: 30px;
            font-family: 'Times New Roman', serif;
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }

        /* ===== STAT CARD ===== */
        .stat-card {
            background: rgba(255,255,255,0.7);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            border: 1px solid rgba(196,168,130,0.3);
            box-shadow: 0 4px 20px rgba(62,39,35,0.06);
            animation: pulseGlow 4s ease-in-out infinite;
        }
        .stat-number {
            font-family: 'Times New Roman', serif;
            font-size: 36px;
            font-weight: bold;
            color: #3E2723;
        }
        .stat-label {
            font-family: 'Times New Roman', serif;
            font-size: 13px;
            color: #888;
            margin-top: 4px;
        }

        /* ===== QUOTE MARKS ===== */
        .quote-mark {
            font-size: 48px;
            color: #C4A882;
            text-align: center;
            line-height: 1;
            margin-bottom: -10px;
        }

        /* ===== FLOATING ICON ===== */
        .float-icon {
            font-size: 44px;
            text-align: center;
            margin-bottom: 12px;
            animation: float 3s ease-in-out infinite;
        }

        /* ===== NAV BAR OVERRIDE ===== */
        .nav-link:hover {
            background-color: rgba(166,139,107,0.3) !important;
            transition: background 0.3s ease;
        }
    </style>
    """, unsafe_allow_html=True)