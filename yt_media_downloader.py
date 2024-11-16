import os
import yt_dlp


def download_video(url, output_path):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "quiet": True,
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download de {url} como vídeo concluído!")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")


def download_audio(url, output_path):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "noplaylist": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download e conversão de {url} para áudio concluídos!")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")


def main(urls, download_type, output_path="YT Media Downloader Folder"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    if download_type == "video":
        for url in urls:
            download_video(url, output_path)
    else:
        for url in urls:
            download_audio(url, output_path)


if __name__ == "__main__":
    
    urls = []
    download_type = ""

    while True:
        download_type = input('Digite "audio" para baixar música ou "video" para baixar vídeo: ').strip().lower()

        if download_type in ["audio", "video"]:
            break
        print('Opção inválida! Digite "audio" ou "video".')
    
    while True: 
        url = input("URL [apenas pressione enter para finalizar]: ").strip()
        if url == "":
            break
        urls.append(url)
    
    if urls:
        main(urls, download_type)

    else:
        print("Nenhuma URL foi fornecida.")
