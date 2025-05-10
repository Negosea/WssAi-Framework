from PIL import Image
import os

def gerar_pdf_pasta(imagens_dir, nome_arquivo_pdf):
    imagens = []

    for arquivo in sorted(os.listdir(imagens_dir)):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            caminho = os.path.join(imagens_dir, arquivo)
            img = Image.open(caminho).convert('RGB')
            imagens.append(img)

    if imagens:
        imagens[0].save(nome_arquivo_pdf, save_all=True, append_images=imagens[1:])
        print(f"✅ PDF gerado com sucesso em: {nome_arquivo_pdf}")
    else:
        print("⚠️ Nenhuma imagem válida encontrada.")

if __name__ == "__main__":
    gerar_pdf_pasta(
        imagens_dir="/home/sea/Downloads/foto_plantas_forro",
        nome_arquivo_pdf="dataset/planta_forro_drywall.pdf"  # Ajuste se quiser outro destino
    )
