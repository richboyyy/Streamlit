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
        /* ================================================================
        PALETA DE CORES EDITÁVEL
        ================================================================
        */
        :root {
            --cor-primaria: #005BA1;
            --cor-fundo-card: #E8F0FE;
            --cor-fundo-pagina: #F0F2F6;
        }
        /* ================================================================ */

        /* Aplica a cor de fundo à página */
        [data-testid="stAppViewContainer"] {
            background-color: var(--cor-fundo-pagina);
        }
        
        [data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }

        /* Estilo dos cards de serviço */
        .card {
            /* Aparência */
            border: 2px solid var(--cor-primaria);
            border-radius: 10px;
            padding: 20px;
            background-color: var(--cor-fundo-card);
            
            /* Layout Interno */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            
            /* --- CONTROLE DE TAMANHO E FORMATO --- */
            aspect-ratio: 1 / 1;  /* Mantém o card quadrado */
            max-width: 350px;     /* Define a largura máxima do card */
            margin: auto;         /* Centraliza o card na sua coluna */
        }
        .card-content {
            flex-grow: 1; 
            text-align: center;
        }
        .card img {
            height: 50%; 
            max-height: 150px;
            width: auto;
            object-fit: contain;
            border-radius: 8px;
            margin-bottom: 15px;
            transition: transform 0.2s;
        }

        /* Efeito de zoom na imagem */
        .card a:hover img {
            transform: scale(1.05);
        }

        /* Estilo para a logo específica */
        .logo-ouvidoria-anvisa-card {
            width: 130px !important; 
            height: auto !important;
        }
    </style>
""", unsafe_allow_html=True)


# ===== Título e Logo =====
col1, col2 = st.columns([1, 5])

with col1:
    logo_path = "images/logo_ouvidoria_anvisa.png" 
    if Path(logo_path).is_file():
        st.image(logo_path, width=150)
    else:
        st.warning(f"Logo não encontrada em: {logo_path}")

with col2:
    st.markdown("<h1 style='margin-top: 10px;'>Hub de Serviços da Ouvidoria - ANVISA</h1>", unsafe_allow_html=True)
    st.markdown("Acesse rapidamente os principais canais de participação e atendimento:")

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

# ===== Layout dos Cards (st.columns) =====
for i in range(0, len(servicos), 2):
    
    cols = st.columns(2, gap="large") 
    
    for col, servico in zip(cols, servicos[i:i+2]):
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
            
            # Renderiza cada card em sua própria coluna
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
            
    # Adiciona um espaço vertical entre as linhas
    st.write("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# ===== Rodapé =====
st.markdown("---")
st.caption("© 2025 - Ouvidoria ANVISA. Este hub é um canal facilitador de acesso público aos serviços de escuta social e atendimento institucional.")