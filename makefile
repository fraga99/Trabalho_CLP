CC = gcc
CFLAGS = -shared -fPIC
TARGET = mandelbrot.dll

build:
	$(CC) $(CFLAGS) -o $(TARGET) mandelbrot.c

run:
	python interface.py

clean:
	del $(TARGET)