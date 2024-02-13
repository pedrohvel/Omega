import os
import tkinter as tk
from tkinter import ttk, messagebox

def executar_bat(caminho_bat):
    try:
        os.startfile(caminho_bat)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar o BAT: {e}")

def listar_bats(pasta):
    bats = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.bat')]
    return bats

def obter_pasta_scripts():
    # Obtém o diretório do script Python
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    
    # Concatena "Scripts" ao diretório do script
    pasta_scripts = os.path.join(diretorio_script, "Scripts")

    return pasta_scripts

def criar_interface():
    # Obtém a pasta Scripts automaticamente
    pasta_scripts = obter_pasta_scripts()

    if os.path.exists(pasta_scripts):
        bats = listar_bats(pasta_scripts)

        if bats:
            # Criar a janela principal
            root = tk.Tk()
            root.title("Executar BATs")

            # Configurar tema escuro
            root.tk_setPalette(background='#333', foreground='white')
            style = ttk.Style()
            style.theme_use('clam')  # Escolher um tema que suporte o modo escuro
            style.configure('TButton', background='#444', foreground='white', padding=10, relief="flat")
            style.configure('TLabel', background='#333', foreground='white')
            style.configure('TFrame', background='#333')

            # Adicionar um rótulo
            label = ttk.Label(root, text="Selecione um BAT para executar:")
            label.pack(pady=10)

            # Criar um frame para os botões
            frame_botoes = ttk.Frame(root)
            frame_botoes.pack(pady=10)

            # Criar um botão para cada BAT
            for bat in bats:
                caminho_bat = os.path.join(pasta_scripts, bat)
                botao_bat = ttk.Button(frame_botoes, text=bat, command=lambda b=caminho_bat: executar_bat(b))
                botao_bat.pack(side=tk.LEFT, padx=10, pady=5)

            # Iniciar o loop de eventos da interface gráfica
            root.mainloop()

        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo BAT encontrado na pasta Scripts.")
    else:
        messagebox.showerror("Erro", "Pasta Scripts não encontrada.")

# Chamar a função para criar a interface
criar_interface()
