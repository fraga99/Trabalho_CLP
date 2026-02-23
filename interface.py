import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Irá carregar a DLL
lib = ctypes.CDLL ("./mandelbrot.dll")

# Definição dos argumentos
lib.calcular_mandelbrot.argtypes = [
    ctypes.c_int, ctypes.c_int,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int)
]

# Parâmetros
largura = 800
altura = 600
max_iter = 100

xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Array para receber o resultado
resultado = np.zeros(largura * altura, dtype=np.int32)

# Chamada de função em C
lib.calcular_mandelbrot (
    largura, altura,
    xmin, xmax,
    ymin, ymax,
    max_iter,
    resultado.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
)

# Converte para matriz 2D
imagem = resultado.reshape((altura, largura))

# Mostra a imagem
plt.imshow(imagem, cmap = "inferno")
plt.colorbar()
plt.title("Fractal de Mendelbrot - C e Python")
plt.show()