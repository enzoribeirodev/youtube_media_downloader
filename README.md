# YT Media Downloader

Um script Python simples e eficiente para baixar vídeos ou extrair áudio (MP3) de URLs do YouTube utilizando a biblioteca `yt-dlp`.

## 📋 Pré-requisitos

Para que o script funcione corretamente, você precisa ter os seguintes itens instalados no seu sistema:

1.  **Python 3.6+**
2.  **FFmpeg** (Obrigatório)

### ⚠️ Importante: Instalação do FFmpeg

O **FFmpeg** é essencial para unir faixas de áudio e vídeo e para converter arquivos para MP3. Sem ele, o script **não funcionará**.

1.  Baixe o FFmpeg no site oficial: https://www.ffmpeg.org/
2.  Instale e certifique-se de adicionar o binário do FFmpeg às variáveis de ambiente (PATH) do seu sistema operacional.

## 🚀 Instalação

1.  Clone este repositório (ou baixe o arquivo `.py`):
```bash
git clone https://github.com/enzoribeirodev/youtube_media_downloader
```
3.  Instale a dependência Python necessária:
```bash
pip install yt-dlp
``` 

## 💻 Como Usar

1.  Execute o script via terminal:

    python main.py

    *(Substitua `main.py` pelo nome que você deu ao arquivo)*

2.  Siga as instruções na tela:
    * Digite **"video"** para baixar o vídeo completo (melhor qualidade de vídeo + áudio).
    * Digite **"audio"** para baixar apenas o áudio convertido para MP3 (192kbps).
    * Insira as URLs do YouTube uma por uma. Pressione **Enter** sem digitar nada para iniciar o download.

3.  Os arquivos serão salvos automaticamente na pasta:
    `./YT Media Downloader Folder/`

## ⚙️ Funcionalidades

* **Download de Vídeo:** Baixa a melhor qualidade de vídeo e áudio disponíveis e os mescla.
* **Download de Áudio:** Extrai o áudio e converte automaticamente para MP3.
* **Download em Lote:** Permite inserir múltiplas URLs para baixar tudo de uma vez.
* **Organização:** Cria automaticamente a pasta de destino se ela não existir.

