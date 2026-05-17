@echo off
echo === Instalando Projeto SUS ===
cd /d %~dp0

set /p DB_PASS="Digite a senha do usuario root do MySQL local: "

echo 1. Criando ambiente virtual...
python -m venv venv

echo 2. Ativando ambiente...
call venv\Scripts\activate

echo 3. Instalando pacotes...
pip install -r requirements.txt

echo 4. Ligando servidor...
start http://127.0.0.1:8000/admin/
python manage.py runserver

pause