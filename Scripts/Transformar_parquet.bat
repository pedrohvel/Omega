@echo off
setlocal
set SCRIPT_PATH=%~dp0

echo Iniciando script de transformação...

rem Ativar o ambiente virtual (se necessário)
rem call %SCRIPT_PATH%myenv\Scripts\activate

echo Executando script Python...
python %SCRIPT_PATH%Transformar_parquet.py

rem Desativar o ambiente virtual (se necessário)
rem call deactivate

echo Script concluído. Pressione qualquer tecla para fechar.
pause
