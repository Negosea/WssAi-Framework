#!/usr/bin/env python3
"""
Script aprimorado para criar __init__.py apenas em diretórios Python relevantes
Versão corrigida em 03/06/2024
"""

import os
import argparse
from pathlib import Path

# Diretórios que devem ser ignorados
IGNORE_DIRS = {
    '__pycache__', '.git', '.venv', '.vscode', 'venv',
    'node_modules', 'dist', 'build', 'docs', 'dataset',
    'uploads', 'data', 'static', 'images', 'css', 'js',
    'video', 'templates', 'egg-info', '.egg-info'
}

def should_ignore(path: Path) -> bool:
    """Verifica se o diretório deve ser ignorado"""
    if not path.parts:  # Verifica se o caminho está vazio
        return False
    return (
        path.parts[-1].startswith(('.', '__')) or
        any(part.lower() in IGNORE_DIRS for part in path.parts)
    )

def create_init_files(root_dir: str, verbose: bool = False, dry_run: bool = False):
    """Versão aprimorada com filtros"""
    root_path = Path(root_dir).resolve()
    created_count = 0
    existing_count = 0
    
    if not root_path.exists():
        print(f"❌ Diretório não encontrado: {root_path}")
        return
    
    print(f"🔍 Procurando em: {root_path}")

    for dirpath, dirnames, filenames in os.walk(root_path):
        current_dir = Path(dirpath)
        
        if should_ignore(current_dir):
            if verbose:
                print(f"↪ Ignorado: {current_dir.relative_to(root_path)}")
            continue
            
        # Verificação robusta de diretório Python
        has_py_files = any(
            f.endswith('.py') and not f.startswith('_') and f != '__init__.py'
            for f in filenames
        )
        has_init_file = '__init__.py' in filenames
        has_python_subpackages = any(
            d.is_dir() and (d / '__init__.py').exists()
            for d in current_dir.iterdir()
            if not d.name.startswith('_')
        )
        
        is_python_dir = has_py_files or has_init_file or has_python_subpackages
        
        if not is_python_dir:
            if verbose:
                print(f"⏭ Não-Python: {current_dir.relative_to(root_path)}")
            continue
            
        init_file = current_dir / '__init__.py'
        
        if init_file.exists():
            existing_count += 1
            if verbose:
                print(f"✓ Existente: {init_file.relative_to(root_path)}")
        else:
            if not dry_run:
                init_file.touch()
                content = generate_init_content(current_dir, filenames) # type: ignore
                init_file.write_text(content)
            created_count += 1
            status = "✨ Simulado:" if dry_run else "✨ Criado:"
            print(f"{status} {init_file.relative_to(root_path)}")

    print(f"\n✅ Concluído!")
    print(f"- Arquivos Python existentes: {existing_count}")
    print(f"- Arquivos Python {'simulados' if dry_run else 'criados'}: {created_count}")