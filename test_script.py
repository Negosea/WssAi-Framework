test_cases = [
    (['module.py', 'test.txt'], True),
    (['__init__.py'], True),
    ([], False),
    (['_private.py'], False)
]

print("🔬 Testando classificação de diretórios Python:")
for files, expected in test_cases:
    result = any(f.endswith('.py') and not f.startswith('_') for f in files) or ('__init__.py' in files)
    status = "✅" if result == expected else "❌"
    print(f"{status} {files} -> Esperado: {expected}, Obtido: {result}")
