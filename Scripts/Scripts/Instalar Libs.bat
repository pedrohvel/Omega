@echo off
echo Instalando bibliotecas do requirements.txt...

REM Ativar o ambiente virtual
call C:\Users\Pedro\Documents\GitHub\Omega\.venv\Scripts\activate

REM Verificar se a ativação do ambiente virtual foi bem-sucedida
if errorlevel 1 (
    echo Erro ao ativar o ambiente virtual.
    exit /b 1
)

REM Instalar as dependências
pip install -r C:\Users\Pedro\Documents\GitHub\Omega\Scripts\requirements.txt

REM Desativar o ambiente virtual após a instalação (opcional)
deactivate

echo Instalação concluída.
