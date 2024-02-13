@echo off
set VENV_PATH=C:\Users\Pedro\Documents\GitHub\Omega\.venv

REM Ativa o ambiente virtual
call "%VENV_PATH%\Scripts\activate"

REM Verifica se a ativação do ambiente virtual foi bem-sucedida
if errorlevel 1 (
    echo Erro ao ativar o ambiente virtual.
    exit /b 1
)

REM Abre um prompt de comando com alta prioridade
start "Console do Script" /high cmd /k

REM Desativa o ambiente virtual após o fechamento do prompt (opcional)
call "%VENV_PATH%\Scripts\deactivate"
