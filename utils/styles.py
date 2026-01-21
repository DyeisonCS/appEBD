"""
Estilos CSS responsivos globais para o Sistema EBD
"""
from utils.constants import COLORS

MOBILE_CSS = f"""
<style>
/* ========== BASE STYLES ========== */
.main {{
    background-color: {COLORS['background']};
}}

/* ========== TYPOGRAPHY ========== */
h1, h2, h3, h4, h5, h6 {{
    word-wrap: break-word;
}}

/* ========== BUTTONS ========== */
.stButton > button {{
    min-height: 44px;
    font-size: 0.95rem;
    border-radius: 0.5rem;
    transition: all 0.2s;
}}

/* ========== INPUTS ========== */
.stTextInput > div > div > input,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input {{
    min-height: 44px;
    font-size: 16px !important; /* Previne zoom no iOS */
}}

/* ========== CHECKBOXES ========== */
.stCheckbox {{
    min-height: 44px;
    display: flex;
    align-items: center;
}}
.stCheckbox label {{
    font-size: 0.95rem;
}}

/* ========== DATAFRAMES ========== */
.stDataFrame {{
    overflow-x: auto;
}}

/* ========== METRICS ========== */
[data-testid="stMetricValue"] {{
    font-size: 1.5rem !important;
}}
[data-testid="stMetricLabel"] {{
    font-size: 0.85rem !important;
}}

/* ========== CARDS / CONTAINERS ========== */
.metric-card {{
    background: white;
    padding: 1rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    text-align: center;
    margin-bottom: 0.5rem;
}}
.metric-card .value {{
    font-size: 1.8rem;
    font-weight: bold;
    color: {COLORS['primary']};
}}
.metric-card .label {{
    font-size: 0.85rem;
    color: {COLORS['text']};
}}

/* ========== MOBILE STYLES ========== */
@media (max-width: 768px) {{
    /* Reduce padding */
    .main .block-container {{
        padding: 1rem 0.5rem !important;
    }}

    /* Smaller headings */
    h1 {{
        font-size: 1.5rem !important;
    }}
    h2 {{
        font-size: 1.3rem !important;
    }}
    h3 {{
        font-size: 1.1rem !important;
    }}

    /* Metrics compactos */
    [data-testid="stMetricValue"] {{
        font-size: 1.2rem !important;
    }}
    [data-testid="stMetricLabel"] {{
        font-size: 0.75rem !important;
    }}
    [data-testid="stMetricDelta"] {{
        font-size: 0.7rem !important;
    }}

    /* Columns stack on mobile */
    [data-testid="column"] {{
        width: 100% !important;
        flex: 1 1 100% !important;
    }}

    /* Tabelas scrollaveis */
    .stDataFrame > div {{
        overflow-x: auto !important;
    }}

    /* Graficos responsivos */
    .js-plotly-plot {{
        width: 100% !important;
    }}

    /* Botoes maiores em mobile */
    .stButton > button {{
        padding: 0.75rem 1rem;
        font-size: 1rem;
    }}

//    /* Sidebar */
//    [data-testid="stSidebar"] {{
//        min-width: 100% !important;
//    }}

    /* Esconde elementos decorativos */
    .decoration-hide-mobile {{
        display: none !important;
    }}

    /* Card metrics mobile */
    .metric-card {{
        padding: 0.75rem;
    }}
    .metric-card .value {{
        font-size: 1.4rem;
    }}
    .metric-card .label {{
        font-size: 0.75rem;
    }}
}}

/* ========== TABLET STYLES ========== */
@media (min-width: 769px) and (max-width: 1024px) {{
    .main .block-container {{
        padding: 1.5rem 1rem !important;
    }}

    [data-testid="stMetricValue"] {{
        font-size: 1.3rem !important;
    }}
}}

/* ========== UTILITY CLASSES ========== */
.text-center {{
    text-align: center;
}}
.text-primary {{
    color: {COLORS['primary']};
}}
.text-success {{
    color: {COLORS['success']};
}}
.text-warning {{
    color: {COLORS['warning']};
}}
.text-danger {{
    color: {COLORS['danger']};
}}
.mt-1 {{
    margin-top: 0.5rem;
}}
.mt-2 {{
    margin-top: 1rem;
}}
.mb-1 {{
    margin-bottom: 0.5rem;
}}
.mb-2 {{
    margin-bottom: 1rem;
}}

/* ========== CHAMADA PAGE SPECIFIC ========== */
.chamada-row {{
    display: flex;
    align-items: center;
    padding: 0.5rem 0;
    border-bottom: 1px solid #eee;
    flex-wrap: wrap;
    gap: 0.5rem;
}}
.chamada-row .nome {{
    flex: 1;
    min-width: 150px;
}}
.chamada-row .controls {{
    display: flex;
    gap: 0.5rem;
    align-items: center;
    flex-wrap: wrap;
}}

@media (max-width: 768px) {{
    .chamada-row {{
        flex-direction: column;
        align-items: flex-start;
    }}
    .chamada-row .nome {{
        width: 100%;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }}
    .chamada-row .controls {{
        width: 100%;
        justify-content: space-between;
    }}
}}
</style>
"""


def inject_mobile_css():
    """Injeta CSS responsivo na pagina"""
    import streamlit as st
    st.markdown(MOBILE_CSS, unsafe_allow_html=True)
