#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe asaudação na língua correspondente.

Como usar:

Tenha a variável LANG devidamente configurada. Ex.:

    export LANG=pt_BR.UTF-8

Execução:

    python3 hello.py
    ou 
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Luiz Teixeira"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US").split(".")[0]
msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao Mondo!"
elif current_language == "es_SP":
    msg = "Hola Mundo!"
elif current_language == "fi_FI":
    msg = "Tervetuloa Ohjelmoimaan!"

print(msg)
