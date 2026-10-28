import json
import os

# Obtiene la carpeta exacta donde está guardado este script
script_dir = os.path.dirname(os.path.abspath(__file__))

cells = []
for i in range(1, 13):
    filepath = os.path.join(script_dir, f"p1-{i}.py")
    with open(filepath, "r", encoding="utf-8") as f:
        cell = {
            "cell_type": "code",
            "source": f.readlines(),
            "metadata": {},
            "outputs": [],
            "execution_count": None
        }
        cells.append(cell)

notebook = {
    "cells": cells,
    "metadata": {"language_info": {"name": "python"}},
    "nbformat": 4,
    "nbformat_minor": 2
}

output_path = os.path.join(script_dir, "practica1.ipynb")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("¡Notebook creado con éxito en la carpeta P1!")