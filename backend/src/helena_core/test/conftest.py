# tests/conftest.py
import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir / "backend" / "src"))