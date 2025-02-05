import os
import re
import unidecode

def sanitize_filename(filename, max_length=20):
    """
    Remove caracteres especiais, mantém apenas letras, números e underscores.
    Limita o nome a um máximo de 20 caracteres mantendo a relação com o original.
    """
    name, ext = os.path.splitext(filename)  # Separa o nome da extensão
    
    # Remove acentos e caracteres especiais
    name = unidecode.unidecode(name)  # Remove acentos
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)  # Substitui caracteres especiais por _
    
    # Limita o tamanho do nome do arquivo
    name = name[:max_length]
    
    return f"{name}{ext}"  # Reanexa a extensão

def rename_files_in_folder(root_folder):
    """Percorre a pasta e subpastas renomeando os arquivos conforme as regras definidas."""
    for folder, subfolders, files in os.walk(root_folder):
        for file in files:
            old_path = os.path.join(folder, file)
            new_name = sanitize_filename(file)
            new_path = os.path.join(folder, new_name)
            
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renomeado: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"Erro ao renomear {old_path}: {e}")

if __name__ == "__main__":
    pasta_alvo = input("Digite o caminho da pasta onde deseja renomear os arquivos: ")
    rename_files_in_folder(pasta_alvo)
    print("Processo concluído!")

