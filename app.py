import streamlit as st

st.set_page_config(
    page_title="Hub da Ouvidoria - ANVISA",
    layout="wide",
    page_icon="📌"
)

# Cabeçalho com logo
st.image("https://www.gov.br/anvisa/pt-br/acesso-a-informacao/institucional/identidade-visual/logo-anvisa.png", width=250)
st.title("🧭 Hub de Serviços da Ouvidoria - ANVISA")
st.markdown("Bem-vindo! Aqui você encontra acesso rápido aos principais serviços da Ouvidoria.")

st.markdown("---")

# Layout com colunas
col1, col2 = st.columns(2)

with col1:
    st.success("📝 **Registrar Manifestação (Fala.BR)**")
    st.link_button("Acessar Fala.BR", "https://falabr.cgu.gov.br/")

    st.info("📄 **Carta de Serviços da Anvisa**")
    st.link_button("Ver Carta de Serviços", "https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/central-de-qualidade/painel-de-monitoramento-de-servicos-federaisv2")

with col2:
    st.warning("🩺 **Ouvidoria Geral do SUS**")
    st.link_button("Acessar Ouvidoria SUS", "https://www.gov.br/saude/pt-br/assuntos/saude-ouvidoria")

    st.error("📬 **Contato Direto com a Ouvidoria**")
    st.link_button("Formulário de Contato", "https://www.gov.br/anvisa/pt-br/canais_atendimento/ouvidoria")

st.markdown("---")
st.info("🔔 Este portal foi desenvolvido para facilitar o acesso da população aos canais oficiais de participação e informação.")
