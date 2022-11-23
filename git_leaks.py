from git import Repo
import re, signal, sys, time


def handler_signal(signal,frame):

    # Salida controlada del programa en caso de que
    # se presione ctrl C

    print("\n\n [!] out .......\ n")

    sys.exit(1)

signal.signal(signal.SIGINT,handler_signal)



def extract(url):

    # Se extrae la información del repositorio
    # Posteriormente se obtiene una lista con todos los commits
    # del repositorio

    repo = Repo(url)
    lista = list(repo.iter_commits())   # Devuelve una lista de objetos
    return lista


def transform(lista, palabras):

    # Se buscan las palabras clave en cada uno de los commits de la
    # lista. En caso de que se encuentre se añade el mensaje a la lista de
    # leaks

    leaks = []

    for commit in lista:
        for buscar in KEY_WORDS:
            if re.search(buscar, commit.message, re.I):
                leaks.append(commit.message)

    return leaks


def load(leaks):

    # Se imprimen todos los leaks encontrados por pantalla

    for i in leaks:
        print(i)
    time.sleep(1)


if __name__ == "__main__":

    REPO_DIR = './skale/skale-manager'
    KEY_WORDS = ['credentials', 'password','key']
    lista = extract(REPO_DIR)
    leaks = transform(lista, KEY_WORDS)
    load(leaks)
