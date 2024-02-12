@echo off
set SCRIPT_PATH=C:\Users\Pedro\Documents\GitHub\Omega\Scripts\Omega_Modelagem_Preditiva.py

REM Ativa o ambiente virtual
call C:\Users\Pedro\Documents\GitHub\Omega\.venv\Scripts\activate

REM Verifica se a ativação do ambiente virtual foi bem-sucedida
if errorlevel 1 (
    echo Erro ao ativar o ambiente virtual.
    exit /b 1
)

REM Executa o script Python
start "Console do Script" /high cmd /k python "%SCRIPT_PATH%"

REM Desativa o ambiente virtual após a conclusão do script (opcional)
deactivate
