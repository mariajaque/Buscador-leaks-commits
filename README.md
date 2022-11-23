# Buscador-leaks-commits
Este repositorio contiene un buscador de leaks en commits.
Para ello, el repositorio consta de:
- Una carpeta "skale" que es la copia del repositorio de Git en el que se van a buscar los leaks
- Un fichero ".gitignore"
- Un fichero "requirements.txt" con las librerías necesarias para la ejecución del código
- Fichero "git_leaks.py" que buscará los leaks en commits. Para ello, se empleará una ETL que buscará unas palabras clave prefijadas en los commits del repositorio clonado

Para la ejecución de este repositorio primero se deberá hacer un pip install requirements.txt, el cual descargará las librerías necesarias para la ejecución del fichero y, posteriormente, ya se podrá ejecutar el fichero ".py".