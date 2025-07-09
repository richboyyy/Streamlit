import streamlit as st

st.set_page_config(page_title="Hub de Serviços da Ouvidoria", layout="centered")

st.title("🔗 Hub de Serviços da Ouvidoria - ANVISA")
st.markdown("Acesse abaixo os principais serviços da Ouvidoria:")

links = {
    "📝 Registrar Manifestação (Fala.BR)": "https://falabr.cgu.gov.br/",
    "📄 Carta de Serviços da Anvisa": "https://www.gov.br/anvisa/pt-br/assuntos/snvs",
    "🩺 Ouvidoria Geral do SUS": "https://www.gov.br/saude/pt-br/canais-de-atendimento/ouvsus",
    "📬 Formulário de Contato da Ouvidoria Anvisa": "https://www.gov.br/anvisa/pt-br/canais_atendimento/ouvidoria",
    # Adicione mais links conforme necessário
}

for label, url in links.items():
    st.link_button(label, url)

st.markdown("---")
st.info("Este é um canal facilitador de acesso aos principais serviços da Ouvidoria da Anvisa.")
