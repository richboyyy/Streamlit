import streamlit as st

st.set_page_config(
    page_title="Hub de Serviços da Ouvidoria - ANVISA",
    layout="wide",
    page_icon="📌"
)

# ===== Título e Logo =====
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo_ouvidoria_anvisa.png", width=160)
with col2:
    st.markdown("<h1 style='margin-top: 40px;'>Hub de Serviços da Ouvidoria - ANVISA</h1>", unsafe_allow_html=True)
    st.markdown("Acesse rapidamente os principais canais de participação e atendimento:")

st.markdown("---")

# ===== Dados dos Serviços =====
servicos = [
    {
        "titulo": "Registrar Manifestação (Fala.BR)",
        "descricao": "Envie sugestões, denúncias, reclamações ou elogios por meio da plataforma Fala.BR.",
        "imagem": "falabr.png",
        "link": "https://falabr.cgu.gov.br/"
    },
    {
        "titulo": "Carta de Serviços da Anvisa",
        "descricao": "Conheça os serviços prestados pela Anvisa e seus compromissos de atendimento.",
        "imagem": "https://www.gov.br/anvisa/@@site-logo/anvisa-logo.png",
        "link": "https://www.gov.br/anvisa/pt-br/carta-de-servicos"
    },
    {
        "titulo": "Ouvidoria Geral do SUS",
        "descricao": "Acesse o canal nacional de ouvidoria do Sistema Único de Saúde.",
        "imagem": "ouvidoriasus.png",
        "link": "https://www.gov.br/saude/pt-br/assuntos/saude-ouvidoria"
    },
    {
        "titulo": "Contato com a Ouvidoria da Anvisa",
        "descricao": "Fale diretamente com a ouvidoria institucional da Anvisa.",
        "imagem": "https://www.gov.br/anvisa/@@site-logo/anvisa-logo.png",
        "link": "https://www.gov.br/anvisa/pt-br/canais_atendimento/ouvidoria"
    },
]

# ===== Layout em grade com imagem nos cards =====
for i in range(0, len(servicos), 2):
    cols = st.columns(2)
    for col, servico in zip(cols, servicos[i:i+2]):
        with col:
            with st.container(border=True):
                st.image(servico["imagem"], use_column_width=True)
                st.markdown(f"### {servico['titulo']}")
                st.markdown(servico["descricao"])
                st.link_button("Acessar", servico["link"])

st.markdown("---")
st.caption("© 2025 - Ouvidoria ANVISA. Este hub é um canal facilitador de acesso público aos serviços de escuta social e atendimento institucional.")
