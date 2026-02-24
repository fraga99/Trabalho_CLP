# Trabalho_CLP
Trabalho de implementação de duas linguagens da disciplina de Conceitos de Linguagem de Programação

## Descrição

Este projeto implementa a geração do Fractal de Mandelbrot utilizando duas linguagens de programação:

- Python → Interface gráfica e visualização
- C → Serviço de cálculo matemático

A integração entre as linguagens é realizada por meio de uma biblioteca dinâmica (DLL) e o módulo `ctypes` do Python.

---
## Estrutura do Repositório

- `mandelbrot.c` → Implementação do algoritmo em C
- `interface.py` → Interface gráfica e chamada da DLL
- `Makefile` → Automatização da compilação e execução
- `DOCUMENTAÇÃO.pdf` → Documentação técnica do projeto

---
## Requisitos

- Python 3.x (64 bits)
- GCC (MinGW-w64 64 bits)
- Pacotes Python:
  - numpy
  - matplotlib
- instalação dos pacotes
  - pip install numpy matplotlib

---
## Arquivos
- mandelbrot.c
- mandelbrot.dll
- interface.py
- makefile
- DOCUMENTAÇÃO.pdf
  
---
## Comando do makefile
- mingw32-make build
- mingw32-make run
  
---
## Comandos manuais
- gcc -shared -o mandelbrot.dll -fPIC mandelbrot.c
- python interface.py

