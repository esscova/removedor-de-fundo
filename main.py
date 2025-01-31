import streamlit as st
from rembg import remove
from PIL import Image
import io
import base64

######################################################################################################
# [FUNCTIONS]
######################################################################################################

def convert_image_to_bytes(img): # imagem para bytes
    """
    Convert a PIL Image to bytes.

    Args:
        img (PIL.Image): A PIL Image.

    Returns:
        bytes: The image as bytes.
    """
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

def get_image_download_link(img, filename, text): # link de download
    """
    Generate a link allowing the user to download the given image.

    The link text will be {text} and the file will be named {filename}.

    Args:
        img (PIL.Image): The image to embed in the link.
        filename (str): The filename to use for the downloaded image.
        text (str): The text of the link.

    Returns:
        str: The generated link.
    """
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">{text}</a>'
    return href

def remove_bg(image): # remover bg
    """
    Remove the background of an image.

    Args:
        image (str or PIL.Image): The input image.

    Returns:
        tuple: A tuple containing the output image and an error message (if any).
    """
    try:
        input_image = Image.open(image)
        output_image = remove(input_image)
        
        return output_image, None

    except Exception as e:
        return None, f"Erro ao processar a imagem: {str(e)}"


######################################################################################################
# [STREAMLIT]
######################################################################################################

# configs
st.set_page_config(
    page_title="Removedor de Fundo de Imagens",
    page_icon="🖼️",
    layout="wide"
)

# CSS
st.markdown(
    """
        <style>
            .main {
                padding: 0 2rem;
            }
            .contact-badge {
                padding: 0.8rem;
                margin: 0.5rem 0;
                border-radius: 8px;
                background-color: #f0f2f6;
                transition: transform 0.2s;
            }
            .contact-badge:hover {
                transform: translateX(5px);
                background-color: #e3e8f2;
            }
        </style>
    """, 
    unsafe_allow_html=True)

# [header]
st.markdown("### 🖼️ Removedor de Fundo de Imagens")
st.markdown("---")

# [sidebar]
with st.sidebar:
    st.header("📤 Upload da Imagem")
    uploaded_file = st.file_uploader(
        "Arraste ou selecione uma imagem",
        type=["jpg", "jpeg", "png"],
        help="Arraste uma imagem ou clique para selecionar"
    )
    show_original = st.checkbox("Mostrar imagem original", value=True)

    st.markdown("---")
    st.header("ℹ️ Sobre")
    st.markdown("""
    Este aplicativo permite remover o fundo de imagens usando a biblioteca `rembg`.
    
    **Formatos suportados:**
    - JPG/JPEG ou PNG.

    **Dicas:**
    - Use imagens com boa resolução
    - Certifique-se que o objeto principal está bem visível
    - Tamanho máximo recomendado: 5MB
    """)
    
    st.markdown("---")
    st.markdown("""
    <div>
        <h3>📩 Contatos</h3>
        <div class="contact-badge">
            <a href="https://github.com/esscova" target="_blank" style="text-decoration:none; color:#2c3e50;">
            💻 GitHub
            </a>
        </div>
        <div class="contact-badge">
            <a href="https://linkedin.com/in/wellington-moreira-santos" target="_blank" style="text-decoration:none; color:#2c3e50;">
            💼 LinkedIn
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# [main]
main_container = st.container()

with main_container:
    if uploaded_file is not None:
        with st.spinner('Processando imagem...'):
            output_image, error = remove_bg(uploaded_file)

        if error:
            st.error(error)
        else:
            if show_original:
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Imagem Original")
                    st.image(uploaded_file, use_container_width=True)
                with col2:
                    st.subheader("Imagem sem Fundo")
                    st.image(output_image, use_container_width=True)
            else:
                st.subheader("Imagem sem Fundo")
                st.image(output_image, use_container_width=True)

            # download
            col1, col2 = st.columns(2)
            with col1:
                    download_btn = st.download_button(
                        label="📥 Baixar Imagem sem Fundo",
                        data=convert_image_to_bytes(output_image),
                        file_name="imagem_sem_fundo.png",
                        mime="image/png"
                    )
            
            # detalhes
            with st.expander("📊 Detalhes da Imagem"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Largura", f"{output_image.size[0]}px")
                with col2:
                    st.metric("Altura", f"{output_image.size[1]}px")