import pandas as pd
from asyncio.format_helpers import extract_stack
from git import Repo
import re,signal,sys,time,pwn,pdb

"""
def handler_signal(signal,frame):

    print("\n\n [!] out .......\ n")

    sys.exit(1)

signal.signal(signal.SIGINT,handler_signal)
"""


def extract(url):

    repo = Repo(url)
    lista = list(repo.iter_commits())   # Devuelve una lista de objetos
    return lista


def transform(lista, palabras):

    leaks = []

    for commit in lista:
        for buscar in KEY_WORDS:
            if re.search(buscar, commit.message, re.I):
                leaks.append(commit.message)

    time.sleep(1)
    return leaks


def load(leaks):

    for i in leaks:
        print(i)
    time.sleep(1)


if __name__ == "__main__":

    REPO_DIR = './skale/skale-manager'
    KEY_WORDS = ['credentials', 'password','key']
    lista = extract(REPO_DIR)
    leaks = transform(lista, KEY_WORDS)
    load(leaks)
