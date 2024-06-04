# tela.spec
# ...

# Inclua este import no topo do seu arquivo .spec
import os

# Função para coletar imagens
def collect_images(directory):
    data_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                file_path = os.path.join(root, file)
                data_files.append((file_path, file_path))
    return data_files

# Caminho para a pasta de imagens
image_folder = 'path/to/your/images/folder'

# Colete as imagens
images = collect_images(image_folder)

# Adicione as imagens coletadas ao parâmetro `datas`
a = Analysis(
    ['tela.py'],
    pathex=['path/to/your/project'],
    binaries=[],
    datas=images,  # Aqui você adiciona a lista de imagens
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Continue com o resto do arquivo .spec como de costume
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='tela',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='tela',
)
