import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def executar_bat(caminho_bat):
    os.startfile(caminho_bat)

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

            # Verificar se o tema escuro é suportado
            if 'theme' in root.tk_get_themes():
                root.tk_setPalette(background='#333', foreground='white')
                style = ttk.Style()
                style.configure('TButton', background='#444', foreground='white', padding=6, relief="flat")
                style.configure('TLabel', background='#333', foreground='white')

                # Adicionar um rótulo
                label = ttk.Label(root, text="Selecione um BAT para executar:")
                label.pack(pady=10)

                # Criar um botão para cada BAT
                for bat in bats:
                    caminho_bat = os.path.join(pasta_scripts, bat)
                    botao_bat = ttk.Button(root, text=bat, command=lambda b=caminho_bat: executar_bat(b))
                    botao_bat.pack(pady=5)

                # Iniciar o loop de eventos da interface gráfica
                root.mainloop()

            else:
                print("Tema escuro não suportado no sistema operacional.")

        else:
            print("Nenhum arquivo BAT encontrado na pasta Scripts.")
    else:
        print("Pasta Scripts não encontrada.")

# Chamar a função para criar a interface
criar_interface()
