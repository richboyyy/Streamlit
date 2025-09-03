import streamlit as st
import base64
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Hub de Serviços da Ouvidoria - ANVISA",
    layout="wide",
    page_icon="📌"
)

# Função para converter imagem local para Base64
def img_to_base64(image_path: Path) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Bloco de estilo CSS
st.markdown("""
    <style>
        :root {
            --cor-primaria: #005BA1;
            --cor-fundo-card: #E8F0FE;
            --cor-fundo-pagina: #F0F2F6;
        }

        [data-testid="stAppViewContainer"] {
            padding-top: 0rem !important;
            background-color: var(--cor-fundo-pagina);
        }

        [data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }

        .card {
            border: 2px solid var(--cor-primaria);
            border-radius: 10px;
            padding: 20px;
            background-color: var(--cor-fundo-card);

            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            aspect-ratio: 1 / 1;
            max-width: 350px;
            margin: auto;
        }

        .card-content {
            flex-grow: 1;
            text-align: center;
        }

        .card img {
            height: 100%;
            max-height: 180px;
            width: auto;
            object-fit: contain;
            border-radius: 8px;
            margin-bottom: 15px;
            transition: transform 0.2s;
        }

        .card a:hover img {
            transform: scale(1.05);
        }

        .card img.logo-ouvidoria-anvisa-card {
            max-height: 200px !important;
            width: auto !important;
            height: auto !important;
            object-fit: contain;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# ===== Título Centralizado =====
st.markdown("""
    <div style='text-align: center; margin-top: -30px;'>
        <h1 style='margin: 0;'>Hub de Serviços da Ouvidoria - ANVISA</h1>
        <p style='margin-top: 0;'>Acesse rapidamente os principais canais de participação e atendimento:</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ===== Dados dos Serviços =====
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
        "imagem": "images/carta_de_servico.png",
        "link": "https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/central-de-qualidade/painel-de-monitoramento-de-servicos-federaisv2"
    },
    {
        "titulo": "Ouvidoria Geral do SUS",
        "descricao": "Acesse o canal nacional de ouvidoria do Sistema Único de Saúde.",
        "imagem": "images/ouvidoriasus.png",
        "link": "https://www.gov.br/saude/pt-br/canais-de-atendimento/ouvsus"
    },
    {
        "titulo": "Contato com a Ouvidoria da Anvisa",
        "descricao": "Fale diretamente com a ouvidoria institucional da Anvisa.",
        "imagem": "images/logo_ouvidoria_anvisa.png",
        "link": "https://www.gov.br/anvisa/pt-br/canais_atendimento/ouvidoria/fale-ouvidoria"
    },
    {
        "titulo": "Painel Resolveu",
        "descricao": "O painel Resolveu? é uma ferramenta que reúne informações sobre manifestações de ouvidoria que a Administração Pública recebe diariamente pela Plataforma Fala.BR",
        "imagem": "images/painel_resolveu.jpeg",
        "link": "https://centralpaineis.cgu.gov.br/visualizar/resolveu"
    },
    {
        "titulo": "Painel Monitoramento",
        "descricao": "Painel de Monitoramento da Agenda Regulatória da ANVISA",
        "imagem": "images/Anvisa-Logo-1.png",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiMDBkZjhjYjQtNDM2YS00MjQ3LTk5Y2YtODNlOGYwZjM3NDhlIiwidCI6ImI2N2FmMjNmLWMzZjMtNGQzNS04MGM3LWI3MDg1ZjVlZGQ4MSJ9"
    }
]

# ===== Layout dos Cards (3 por linha) =====
for i in range(0, len(servicos), 3):
    cols = st.columns(3, gap="small")
    
    for col, servico in zip(cols, servicos[i:i+3]):
        with col:
            img_path = Path(servico["imagem"])
            if img_path.is_file():
                img_base64 = img_to_base64(img_path)
                img_src = f"data:image/png;base64,{img_base64}"
            else:
                img_src = ""
                st.warning(f"Imagem não encontrada em: {img_path}")

            imagem_classe = ""
            if servico["titulo"] == "Contato com a Ouvidoria da Anvisa":
                imagem_classe = "logo-ouvidoria-anvisa-card"
            
            st.markdown(f"""
                <div class='card'>
                    <a href="{servico["link"]}" target="_blank">
                        <img src='{img_src}' alt='Imagem do serviço' class='{imagem_classe}'>
                    </a>
                    <div class='card-content'>
                        <h4>{servico["titulo"]}</h4>
                        <p>{servico["descricao"]}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.write("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# ===== Rodapé =====
st.markdown("---")
st.caption("© 2025 - Ouvidoria ANVISA. Este hub é um canal facilitador de acesso público aos serviços de escuta social e atendimento institucional.")
