# 🖼️ Removedor de Fundo de Imagens
![screenshot](image.png)
Este é um aplicativo web desenvolvido com Streamlit que permite remover o fundo de imagens utilizando a biblioteca `rembg`. O aplicativo suporta imagens nos formatos JPG, JPEG e PNG, e oferece a opção de baixar a imagem processada sem o fundo.

## 🚀 Como Usar

Você pode rodar este projeto de duas maneiras: localmente ou usando Docker. Escolha a opção que melhor se adapta ao seu ambiente.

---

### 🐳 Rodando com Docker

Se você prefere rodar o projeto em um container Docker, siga os passos abaixo:

1. **Certifique-se de ter o Docker instalado**:
   - [Instale o Docker](https://docs.docker.com/get-docker/) se ainda não o tiver.

2. **Clone este repositório**:
   ```bash
   git clone https://github.com/esscova/removedor-de-fundo.git
   cd removedor-de-fundo
   ```

3. **Construa a imagem Docker**:
   ```bash
   docker build -t removedor-de-fundo .
   ```

4. **Execute o container**:
   ```bash
   docker run -p 8501:8501 removedor-de-fundo
   ```

5. **Acesse o aplicativo**:
   Abra o navegador e acesse `http://localhost:8501`.

---

### 💻 Rodando Localmente

Se você prefere rodar o projeto diretamente no seu ambiente local, siga os passos abaixo:

#### Pré-requisitos

- Python 3.10 ou superior instalado.
- `pip` para gerenciamento de dependências.

#### Passos

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/esscova/removedor-de-fundo.git
   cd removedor-de-fundo
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o aplicativo**:
   ```bash
   streamlit run app.py
   ```

5. **Acesse o aplicativo**:
   Abra o navegador e acesse `http://localhost:8501`.

---

## 🛠️ Funcionalidades

- **Remoção de Fundo**: Remove o fundo de imagens nos formatos JPG, JPEG e PNG.
- **Visualização de Imagens**: Permite visualizar a imagem original e a imagem processada lado a lado.
- **Download da Imagem Processada**: Oferece a opção de baixar a imagem sem o fundo.
- **Detalhes da Imagem**: Exibe informações sobre a largura e altura da imagem processada.

---

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas:

- `streamlit`: Para criar a interface web.
- `rembg`: Para remover o fundo das imagens.
- `Pillow (PIL)`: Para manipulação de imagens.
- `onnxruntime`: Para execução de modelos ONNX usados pelo `rembg`.

Todas as dependências estão listadas no arquivo `requirements.txt`.

---

## 📝 Exemplo de Uso

1. Acesse o aplicativo no seu navegador.
2. Faça o upload de uma imagem clicando no botão de upload na barra lateral.
3. Aguarde o processamento da imagem.
4. Visualize a imagem original e a imagem sem fundo.
5. Baixe a imagem processada clicando no botão de download.

---

## 📞 Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- **GitHub**: [esscova](https://github.com/esscova)
- **LinkedIn**: [Wellington Moreira Santos](https://linkedin.com/in/wellington-moreira-santos)

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Nota**: Este projeto foi desenvolvido como uma demonstração de uso da biblioteca `rembg` em conjunto com o Streamlit. Sinta-se à vontade para contribuir ou adaptá-lo conforme suas necessidades.
