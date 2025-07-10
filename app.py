import streamlit as st

st.set_page_config(
    page_title="Hub de Serviços da Ouvidoria - ANVISA",
    layout="wide",
    page_icon="📌"
)

# ===== Estilo personalizado =====
st.markdown("""
    <style>
        .card {
            border: 2px solid #005BA1;
            border-radius: 10px;
            padding: 20px;
            background-color: #E8F0FE;
            height: 100%;
        }
        .card img {
            width: 100%;
            height: 150px;
            object-fit: contain;
            border-radius: 8px;
        }
        .botao-acessar {
            background-color: #005BA1;
            color: white;
            padding: 0.5em 1.2em;
            border: none;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
        }
        .botao-acessar:hover {
            background-color: #004480;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ===== Título e logo =====
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo_ouvidoria_anvisa.png", width=1000)
with col2:
    st.markdown("<h1 style='margin-top: 40px;'>Hub de Serviços da Ouvidoria - ANVISA</h1>", unsafe_allow_html=True)
    st.markdown("Acesse rapidamente os principais canais de participação e atendimento:")

st.markdown("---")

# ===== Dados dos serviços =====
servicos = [
    {
        "titulo": "Registrar Manifestação (Fala.BR)",
        "descricao": "Envie sugestões, denúncias, reclamações ou elogios por meio da plataforma Fala.BR.",
        "imagem": "images/falabr.png",
        "link": "https://falabr.cgu.gov.br/"
    },
    {
        "titulo": "Carta de Serviços da Anvisa",
        "descricao": "Conheça os serviços prestados pela Anvisa e seus compromissos de atendimento.",
        "imagem": "images/Anvisa-Logo-1.png",
        "link": "https://www.gov.br/anvisa/pt-br/carta-de-servicos"
    },
    {
        "titulo": "Ouvidoria Geral do SUS",
        "descricao": "Acesse o canal nacional de ouvidoria do Sistema Único de Saúde.",
        "imagem": "images/ouvidoriasus.png",
        "link": "https://www.gov.br/saude/pt-br/assuntos/saude-ouvidoria"
    },
    {
        "titulo": "Contato com a Ouvidoria da Anvisa",
        "descricao": "Fale diretamente com a ouvidoria institucional da Anvisa.",
        "imagem": "images/logo_ouvidoria_anvisa.png",
        "link": "https://www.gov.br/anvisa/pt-br/canais_atendimento/ouvidoria"
    },
]

# ===== Layout dos cards com imagem padronizada =====
for i in range(0, len(servicos), 2):
    cols = st.columns(2)
    for col, servico in zip(cols, servicos[i:i+2]):
        with col:
            st.markdown(f"""
                <div class='card'>
                    <img src='{servico["imagem"]}' alt='Imagem do serviço'>
                    <h4>{servico["titulo"]}</h4>
                    <p>{servico["descricao"]}</p>
                    <a href="{servico["link"]}" class="botao-acessar" target="_blank">Acessar</a>
                </div>
            """, unsafe_allow_html=True)

# ===== Rodapé =====
st.markdown("---")
st.caption("© 2025 - Ouvidoria ANVISA. Este hub é um canal facilitador de acesso público aos serviços de escuta social e atendimento institucional.")
