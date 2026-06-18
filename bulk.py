import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

def organizar_arquivos(pasta_alvo):
    conteudo = os.listdir(pasta_alvo)
    categorias = {
    # Imagens
        '.jpg': 'Imagens', '.jpeg': 'Imagens', '.png': 'Imagens', '.gif': 'Imagens', '.bmp': 'Imagens', '.svg': 'Imagens', '.webp': 'Imagens',
    # Documentos
        '.pdf': 'Documentos', '.docx': 'Documentos', '.doc': 'Documentos', '.txt': 'Documentos', '.rtf': 'Documentos',
    # Planilhas e Apresentações
        '.xlsx': 'Planilhas', '.xls': 'Planilhas', '.csv': 'Planilhas',
        '.pptx': 'Apresentações', '.ppt': 'Apresentações',
    # Áudio e Vídeo
        '.mp3': 'Áudio', '.wav': 'Áudio', '.flac': 'Áudio',
        '.mp4': 'Vídeos', '.avi': 'Vídeos', '.mkv': 'Vídeos', '.mov': 'Vídeos',
    # Compactados
        '.zip': 'Compactados', '.rar': 'Compactados', '.7z': 'Compactados', '.tar': 'Compactados', '.gz': 'Compactados',
    # Programas e Executáveis
        '.exe': 'Programas', '.msi': 'Programas', '.msix': 'Programas', '.bat': 'Programas', '.sh': 'Programas',
    # Código e Dev
        '.py': 'Código', '.js': 'Código', '.html': 'Código', '.css': 'Código', '.json': 'Código', '.ipynb': 'Notebooks',
    # E-books e Quadrinhos
        '.epub': 'Ebooks', '.mobi': 'Ebooks', '.azw3': 'Ebooks', '.cbz': 'Ebooks', '.cbr': 'Ebooks',
    # Outros
        '.ini': 'Configurações', '.iso': 'Imagens_de_Disco'
    }

    for item in conteudo:
        caminho_antigo = os.path.join(pasta_alvo, item)
        
        if os.path.isdir(caminho_antigo):
            continue

        nome, extensao = os.path.splitext(item)

        nome_da_pasta_nova = categorias.get(extensao.lower(), 'Outros')
        caminho_pasta_nova = os.path.join(pasta_alvo, nome_da_pasta_nova)
    
        if not os.path.exists(caminho_pasta_nova):
            os.mkdir(caminho_pasta_nova)

        shutil.move(caminho_antigo, caminho_pasta_nova)

def acionar_organizador():
    pasta_escolhida = filedialog.askdirectory(title="Selecione a pasta bagunçada")
    
    if pasta_escolhida:
        organizar_arquivos(pasta_escolhida)
        
        messagebox.showinfo("Sucesso", "Pasta organizada com sucesso!")

ctk.set_appearance_mode("System")  # Segue o tema do sistema (Dark/Light)
ctk.set_default_color_theme("blue")  # Tema de cores

janela = ctk.CTk()
janela.title("Organizador de Arquivos")

largura_janela = 450
altura_janela = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int((largura_tela / 2) - (largura_janela / 2))
pos_y = int((altura_tela / 2) - (altura_janela / 2))
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

janela.resizable(False, False)

# Frame principal com bordas arredondadas
frame = ctk.CTkFrame(janela, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label_titulo = ctk.CTkLabel(frame, 
                            text="Organizador Automático", 
                            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"))
label_titulo.pack(pady=(20, 10))

label_desc = ctk.CTkLabel(frame, 
                          text="Selecione a pasta bagunçada e deixe o\nprograma organizar tudo por categorias.", 
                          font=ctk.CTkFont(family="Segoe UI", size=13),
                          justify="center")
label_desc.pack(pady=(0, 30))

botao_iniciar = ctk.CTkButton(frame, 
                              text="📂 Escolher Pasta",
                              command=acionar_organizador,
                              font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
                              height=45,
                              corner_radius=8,
                              cursor="hand2")
botao_iniciar.pack()

label_rodape = ctk.CTkLabel(frame, 
                            text="v1.0", 
                            font=ctk.CTkFont(family="Segoe UI", size=11),
                            text_color="gray")
label_rodape.pack(side="bottom", pady=10)

janela.mainloop()
