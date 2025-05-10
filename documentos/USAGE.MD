
# **2. Comentários no Código**

Certifique-se de que cada função e bloco de código tenha comentários explicativos, como mostrado no exemplo acima.

---

## **3. Documentação Técnica**

Adicione um arquivo `docs/USAGE.md` para documentar como os desenvolvedores podem usar e estender o código.

**Exemplo de `docs/USAGE.md`:**

```markdown
# Documentação Técnica - WssAi-Framework

## Estrutura do Código
- **`app.py`**: Aplicativo Flask para upload e processamento de arquivos.
- **`helena_core/data_loader.py`**: Módulo principal para extração de texto de PDFs e imagens.

## Funções Principais
### `preprocess_pdf(pdf_path: str) -> str`
- Pré-processa um arquivo PDF para extrair texto.
- Aplica OCR em páginas que não contêm texto.
- **Parâmetros:**
  - `pdf_path` (str): Caminho para o arquivo PDF.
- **Retorno:**
  - Texto extraído do PDF.

### `process_image(image_path: str) -> str`
- Processa uma imagem e extrai texto usando OCR.
- **Parâmetros:**
  - `image_path` (str): Caminho para a imagem.
- **Retorno:**
  - Texto extraído da imagem.

## Extensões Futuras
- Adicionar suporte para múltiplos idiomas no OCR.
- Criar uma interface gráfica para facilitar o uso.
- Implementar aprendizado contínuo para melhorar a análise de texto.
