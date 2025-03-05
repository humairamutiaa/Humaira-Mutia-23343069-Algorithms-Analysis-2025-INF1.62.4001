print('Nama  : Humaira Mutia')
print('NIM : 23343069')
print('Gaussian Elimination\n')


def eliminasi_gauss(matriks, vektor):
    n = len(matriks)
    # Forward elimination dengan partial pivoting
    for i in range(n):
        # Cari baris pivot dengan nilai absolut maksimum pada kolom i
        indeks_pivot = i
        for j in range(i + 1, n):
            if abs(matriks[j][i]) > abs(matriks[indeks_pivot][i]):
                indeks_pivot = j
        if indeks_pivot != i:
            matriks[i], matriks[indeks_pivot] = matriks[indeks_pivot], matriks[i]
            vektor[i], vektor[indeks_pivot] = vektor[indeks_pivot], vektor[i]
        
        # Eliminasi baris di bawah pivot
        for j in range(i + 1, n):
            faktor = matriks[j][i] / matriks[i][i]
            for k in range(i, n):
                matriks[j][k] -= faktor * matriks[i][k]
            vektor[j] -= faktor * vektor[i]
    
    # Back substitution
    solusi = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        total = 0
        for k in range(i + 1, n):
            total += matriks[i][k] * solusi[k]
        solusi[i] = (vektor[i] - total) / matriks[i][i]
    
    return solusi

# Contoh penggunaan:
matriks_koefisien = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
vektor_konstanta = [8, -11, -3]

hasil = eliminasi_gauss(matriks_koefisien, vektor_konstanta)
print("Solusi sistem:", hasil)
