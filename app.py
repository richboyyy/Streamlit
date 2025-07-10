import streamlit as st

st.set_page_config(
    page_title="Hub de Serviços da Ouvidoria - ANVISA",
    layout="wide",
    page_icon="📌"
)

# Imagem de topo (certifique-se de que o arquivo esteja na raiz do repositório)
st.image("logo_ouvidoria_anvisa.png", width=300)

st.markdown("## 🧭 Hub de Serviços da Ouvidoria - ANVISA")
st.markdown("Acesse rapidamente os principais canais de participação e atendimento:")

st.markdown("---")

servicos = [
    {
        "titulo": "Registrar Manifestação (Fala.BR)",
        "descricao": "Envie sugestões, denúncias, reclamações ou elogios por meio da plataforma Fala.BR.",
        "icone": "📝",
        "link": "https://falabr.cgu.gov.br/"
    },
    {
        "titulo": "Carta de Serviços da Anvisa",
        "descricao": "Conheça os serviços prestados pela Anvisa e seus compromissos de atendimento.",
        "icone": "📄",
        "link": "https://www.gov.br/anvisa/pt-br/carta-de-servicos"
    },
    {
        "titulo": "Ouvidoria Geral do SUS",
        "descricao": "Acesse o canal nacional de ouvidoria do Sistema Único de Saúde.",
        "icone": "🩺",
        "link": "https://www.gov.br/saude/pt-br/assuntos/saude-ouvidoria"
    },
    {
        "titulo": "Contato com a Ouvidoria da Anvisa",
        "descricao": "Fale diretamente com a ouvidoria institucional da Anvisa.",
        "icone": "📬",
        "link": "https://www.gov.br/anvisa/pt-br/canais_atendimento/ouvidoria"
    },
]

# Layout estilo grade de cartões
for i in range(0, len(servicos), 2):
    cols = st.columns(2)
    for col, servico in zip(cols, servicos[i:i+2]):
        with col:
            with st.container(border=True):
                st.markdown(f"### {servico['icone']} {servico['titulo']}")
                st.markdown(servico["descricao"])
                st.link_button("Acessar", servico["link"])

st.markdown("---")
st.caption("© 2025 - Ouvidoria ANVISA. Este hub é um canal facilitador de acesso público aos serviços de escuta social e atendimento institucional.")
