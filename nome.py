import os
import re
import subprocess

def sanitize_filename(filename):
    """Remove caracteres inválidos e substitui espaços por hifens."""
    sanitized = re.sub(r'[^a-zA-Z0-9_.-]', '-', filename)  # Substitui caracteres inválidos
    sanitized = sanitized.replace(' ', '-')  # Substitui espaços por hifens
    return sanitized

def rename_invalid_files(repo_path):
    """Renomeia arquivos e diretórios inválidos dentro do repositório."""
    for root, dirs, files in os.walk(repo_path, topdown=False):
        for name in files + dirs:
            new_name = sanitize_filename(name)
            if new_name != name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f'Renomeado: {old_path} -> {new_path}')

def sync_git_repo(repo_path):
    """Confirma as mudanças no Git e as envia para o repositório remoto."""
    try:
        subprocess.run(['git', '-C', repo_path, 'add', '.'], check=True)
        subprocess.run(['git', '-C', repo_path, 'commit', '-m', 'Corrigindo nomes de arquivos inválidos'], check=True)
        subprocess.run(['git', '-C', repo_path, 'push'], check=True)
        print("Alterações enviadas para o repositório remoto.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao sincronizar o repositório: {e}")

if __name__ == "__main__":
    repo_path = input("Digite o caminho do repositório Git local: ")
    if os.path.exists(repo_path):
        rename_invalid_files(repo_path)
        sync_git_repo(repo_path)
    else:
        print("Caminho inválido. Verifique se o repositório existe.")

