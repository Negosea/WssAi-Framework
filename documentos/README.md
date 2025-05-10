# WssAi-Framework_0.1

## Features

- Modular and extensible framework for AI development.
- Easy-to-use APIs for rapid prototyping.
- Comprehensive documentation and examples.

## Installation

```bash
git clone https://github.com/your-repo/WssAi-Framework.git
cd WssAi-Framework
pip install -r requirements.txt
```

## WssAi-Framework - Aplicativo Flask para Processamento de Arquivos

Este aplicativo Flask permite o upload de arquivos PDF ou imagens (JPEG/PNG) para extração de texto. Ele utiliza as bibliotecas `pdfplumber` e `pytesseract` para processar os arquivos.

## Funcionalidades

- Upload de arquivos PDF ou imagens.
- Extração de texto de PDFs (com suporte a OCR para PDFs com imagens).
- Extração de texto de imagens digitalizadas usando OCR.

## Requisitos

- Python 3.10 ou superior
- Flask
- pdfplumber
- pytesseract
- PIL (Pillow)
- pdf2image

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-repositorio/WssAi-Framework.git
   cd WssAi-Framework

## Getting Started

1. Import the framework into your project:

    ```python
    from wssai_framework import WssAi
    ```

2. Initialize and configure your AI model:

    ```python
    ai = WssAi(config="config.yaml")
    ai.train()
    ```

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
