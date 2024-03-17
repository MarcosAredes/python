import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import winapps
import csv
import sqlite3
import json
import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq
import openpyxl

def listar_programas(install=True, filtro_data=None, filtro_nome=None):
    resultado_listbox.delete(0, tk.END)  # Limpar a lista antes de listar novamente
    if install:
        programas_instalados = winapps.list_installed()
        if filtro_data:
            programas_instalados = [programa for programa in programas_instalados if programa.install_date == filtro_data]
        if filtro_nome:
            programas_instalados = [programa for programa in programas_instalados if filtro_nome.lower() in programa.name.lower()]

        for programa in programas_instalados:
            resultado_listbox.insert(tk.END, f'Nome: {programa.name}\n'
                                              f'Versão: {programa.version}\n'
                                              f'Data de instalação: {programa.install_date}\n'
                                              f'Data da publicação: {programa.publisher}\n'
                                              f'Local de desinstalação: {programa.uninstall_string}\n'
                                              f'Tamanho em disco: {obter_tamanho_disco(programa.install_location)}\n'
                                              f'{"_" * 30}\n')
    else:
        resultado_listbox.insert(tk.END, "A listagem de programas está desativada.\n")

def obter_tamanho_disco(diretorio):
    if diretorio:
        total_bytes = 0
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                filepath = os.path.join(root, file)
                total_bytes += os.path.getsize(filepath)
        # Convertendo bytes para megabytes
        total_mb = total_bytes / (1024 * 1024)
        return f'{total_mb:.2f} MB'
    else:
        return "N/A"

def exportar_para_arquivo(tipo_arquivo):
    nome_arquivo = nome_arquivo_entry.get()
    if not nome_arquivo:
        messagebox.showerror("Erro", "Por favor, insira o nome do arquivo.")
        return
    try:
        if tipo_arquivo == 'csv':
            with open(f"{nome_arquivo}.csv", 'w', newline='', encoding='utf-8') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(['Nome', 'Versão', 'Data de instalação', 'Publicador', 'Local de desinstalação', 'Tamanho em disco'])
                for programa in winapps.list_installed():
                    escritor.writerow([programa.name, programa.version, programa.install_date, programa.publisher, programa.uninstall_string, obter_tamanho_disco(programa.install_location)])
        elif tipo_arquivo == 'json':
            programas_json = [{'Nome': programa.name,
                               'Versão': programa.version,
                               'Data de instalação': programa.install_date.strftime('%Y-%m-%d') if programa.install_date else None,
                               'Publicador': programa.publisher,
                               'Local de desinstalação': programa.uninstall_string,
                               'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()]
            with open(f"{nome_arquivo}.json", 'w', encoding='utf-8') as arquivo:
                json.dump(programas_json, arquivo, ensure_ascii=False, indent=4)
        elif tipo_arquivo == 'parquet':
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            table = pa.Table.from_pandas(programas_df)
            pq.write_table(table, f"{nome_arquivo}.parquet")
        
        elif tipo_arquivo == 'excel':
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            programas_df.to_excel(f"{nome_arquivo}.xlsx", index=False)
        elif tipo_arquivo == 'html':
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            programas_df.to_html(f"{nome_arquivo}.html", index=False)
        elif tipo_arquivo == 'sqlite':
            conn = sqlite3.connect(f"{nome_arquivo}.db")
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            programas_df.to_sql("Programas", conn, index=False)
            conn.close()
        elif tipo_arquivo == 'hdf5':
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            programas_df.to_hdf(f"{nome_arquivo}.h5", key='data', mode='w')
        elif tipo_arquivo == 'feather':
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            programas_df.to_feather(f"{nome_arquivo}.feather")
        
        elif tipo_arquivo == 'apache_parquet':
            programas_df = pd.DataFrame([{'Nome': programa.name,
                                          'Versão': programa.version,
                                          'Data de instalação': programa.install_date,
                                          'Publicador': programa.publisher,
                                          'Local de desinstalação': programa.uninstall_string,
                                          'Tamanho em disco': obter_tamanho_disco(programa.install_location)} for programa in winapps.list_installed()])
            programas_df.to_parquet(f"{nome_arquivo}.parquet", engine='pyarrow')
            
        messagebox.showinfo("Sucesso", f"Programas exportados com sucesso para '{nome_arquivo}.{tipo_arquivo}'")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao exportar para o arquivo: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Lista de Programas")
root.geometry("1280x950")

# Frame para entrada de dados e botão "Listar Programas"
entrada_frame = ttk.Frame(root)
entrada_frame.pack(pady=10)

filtro_label = ttk.Label(entrada_frame, text="Filtro por nome:")
filtro_label.grid(row=0, column=0, padx=5, pady=5)

filtro_entry = ttk.Entry(entrada_frame)
filtro_entry.grid(row=0, column=1, padx=5, pady=5)

listar_button = ttk.Button(entrada_frame, text="Listar Programas", command=lambda: listar_programas(filtro_nome=filtro_entry.get()))
listar_button.grid(row=0, column=2, padx=5, pady=5)

# Frame para visualização dos resultados
resultado_frame = ttk.Frame(root)
resultado_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

resultado_scroll = ttk.Scrollbar(resultado_frame, orient=tk.VERTICAL)
resultado_scroll.pack(side=tk.RIGHT, fill=tk.Y)

resultado_listbox = tk.Listbox(resultado_frame, yscrollcommand=resultado_scroll.set, width=80, height=20)
resultado_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

resultado_scroll.config(command=resultado_listbox.yview)

# Frame para exportar para arquivo
exportar_frame = ttk.Frame(root)
exportar_frame.pack(pady=10)

nome_arquivo_label = ttk.Label(exportar_frame, text="Nome do arquivo:")
nome_arquivo_label.grid(row=0, column=0, padx=5, pady=5)

nome_arquivo_entry = ttk.Entry(exportar_frame)
nome_arquivo_entry.grid(row=0, column=1, padx=5, pady=5)

tipo_arquivo_label = ttk.Label(exportar_frame, text="Tipo de arquivo:")
tipo_arquivo_label.grid(row=0, column=2, padx=5, pady=5)

tipo_arquivo_combobox = ttk.Combobox(exportar_frame, values=['csv', 'json', 'parquet', 'excel', 'html', 'sqlite', 'hdf5', 'feather'])  
tipo_arquivo_combobox.grid(row=0, column=3, padx=5, pady=5)
tipo_arquivo_combobox.current(0)

exportar_button = ttk.Button(exportar_frame, text="Exportar para arquivo", command=lambda: exportar_para_arquivo(tipo_arquivo_combobox.get()))
exportar_button.grid(row=0, column=4, padx=5, pady=5)

# Iniciar a interface gráfica
root.mainloop()
