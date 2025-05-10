 # extrai dados técnicos estruturados (PERFIS, PENDURAIS etc.)

import re

def parse_technical_data(text):
    data = {}
    perfis = re.findall(r'Perfil\s+[A-Z0-9]+', text)
    pendurais = re.findall(r'[Pp]endurais?.*?\d+[.,]\d+\s*m', text)
    if perfis:
        data['perfis'] = perfis
    if pendurais:
        data['pendurais'] = pendurais
    return data