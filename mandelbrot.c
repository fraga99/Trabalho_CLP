#include <math.h>

#ifdef _WIN64
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT void calcular_mandelbrot(
    int largura,
    int altura,
    double xmin,
    double xmax,
    double ymin,
    double ymax,
    int max_iter,
    int *resultado)

{
    for (int y = 0; y < altura; y++)    {
        for (int x = 0; x < largura; x++)   {
            double cr = xmin + x * (xmax - xmin) / largura;
            double ci = ymin + y * (ymax - ymin) / altura;

            double zr = 0.0, zi = 0.0;
            int iter = 0;

            while (zr*zr + zi*zi <= 4.0 && iter < max_iter) {
                double temp = zr*zr - zi*zi + cr;
                zi = 2.0*zr*zi + ci;
                zr = temp;
                iter++;
            }
            resultado[y * largura + x] = iter;
        }
    }
}