# ----------------------------------
from decouple import config
from pathlib import Path
from datetime import datetime
import subprocess
import gzip
import os
import schedule
from time import sleep


# Instalar as bibliotecas pip install


# ------------------------------------

DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_NAME = config("DB_NAME")


def backup_server():
    backup_dir = Path(__file__).resolve().parent

    file_name = f"{DB_NAME}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    backup_path = backup_dir / f"{file_name}.sql"
    print(backup_path)

    # fazer o backup
    pg_dump_command = (
        f"pg_dump -h {DB_HOST} -p {DB_PORT} -U {DB_USER} {DB_NAME} -f {backup_path}"
    )
    print("Inicando o backup")
    subprocess.run(
        pg_dump_command, shell=True, check=True, env={"PGPASSWORD": DB_PASSWORD}
    )

    # Ira comprimir o arquivo
    compress_backup_path = f"{backup_dir}/{file_name}.sql.gz"
    print("Inicando a compressão")
    with open(backup_path, "rb") as original_file:
        with gzip.open(compress_backup_path, "wb") as compress_file:
            compress_file.write(original_file.read())

    print("Removendo arquivo original")
    os.remove(backup_path)


schedule.every().friday.at("20:00").do(backup_server)  # dia e hora q realizará o backup

while True:
    print("Verificando se a tarefas")
    schedule.run_pending()
    sleep(
        1
    )  # o valor pode mudar mas basicamente, de 1 e 1 segundo verifica se tem tarefa pedente
