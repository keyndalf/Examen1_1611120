/*
 * Estudiante: Keyber Yosnar Sequera Avendaño.
 * Carnet: 16-11120
 * 
 * Descripción: Se resuelven los problemas asignados y se
 * crean funciones que los manejan. Recordar que Kotlin
 * es un lenguaje fuertemente tipado, por lo que es necesario
 * introducir bien los tipos de los elementos a usar en las funciones
 */

import kotlin.math.pow  // Importamos el módulo pow para calcular potencias.

// Para el cálculo de la potencia acumulada:
fun potenciaAcumulada(a: Int, b: Int, c: Int): Int {
    /**
     * -------------------- Descripción ---------------------------
     * Se calcula la potencia acumulada definida por la fórmula
     * a^b mod c, tener en cuenta que a, b y c deben ser no negativos
     * y además c >= 2.
     * --------------------- Parámetros ---------------------------
     * Globales:
     *     No se usan parámetros globales.
     * Locales:
     *     a (Int): primer elemento de la función.
     *     b (Int): segundo elemento de la función.
     *     c (Int): tercer elemento de la función.
     *     valorRetorno (Int): potencia acumulada en función de los
     * elementos suministrados por el usuario.
     * -------------------- Precondición --------------------------
     * a,b >= 0 /\ c > 0
     * ------------------- Postcondición --------------------------
     * valorRetorno = 1
     *     \/ valorRetorno = ((a mod c) * (a^(b - 1) % c)) % c
     *     \/ Se lanza una excepción puesto que a, b, c < 0
     *     \/ Se lanza una excepción puesto que c = 0
     */
    var valorRetorno: Int
    // Comprobamos que a, b, c >= 0:
    if (a < 0) {
        throw RuntimeException("Error, el valor a = $a, debe ser " +
            "mayor o igual a cero.")
    } else if (b < 0) {
        throw RuntimeException("Error, el valor b = $b, debe ser " +
            "mayor o igual a cero.")
    } else if (c <= 0) {
        throw RuntimeException("Error, el valor c = $c, debe ser " +
            "mayor a cero, pues la división cero lo esta permitida " +
            "y ademas, c no puede ser negativo.")
    }
    // Ahora si, calculamos la potencia acumulada:
    if (b == 0) {
        valorRetorno = 1
    } else {
        valorRetorno = ((a % c) *
                        (((a.toDouble()).pow((b - 1).toDouble())) % c).toInt()) % c
    }
    return valorRetorno
}

// Para calcular el producto de dos matrices, se pasa como parámetros
// dos objetos de tipo Iterable<Iterable<Int>>, la multiplicación se
// hará con números enteros en vista de que no se asignó un tipo de números
// para este problema.
fun productoDeMatrices(A: Iterable<Iterable<Int>>,
                     B: Iterable<Iterable<Int>>): MutableList<MutableList<Int>> {
    /**
     * -------------------- Descripción ---------------------------
     * Se calcula el producto de dos matrices A y B, tener en cuenta
     * que si las dimensiones de A son NxM las de B deben ser MxP.
     * --------------------- Parámetros ---------------------------
     * Globales:
     *     No se usan parámetros globales.
     * Locales:
     *     A (Iterable<Iterable<Int>>): primera matriz a considerar.
     *     B (Iterable<Iterable<Int>>): segunda matriz a considerar.
     *     n (Int): número de filas de la matriz A.
     *     m (Int): número de columnas de la matriz A.
     *     mB (Int): número de filas de la matriz B.
     *     p (Int): número de columnas de la matriz B.
     *     matrizRetorno (MutableList<MutableList<Int>>): producto 
     * de las matrices A y B.
     * -------------------- Precondición --------------------------
     * El número de columnas de A debe coincidir con el de filas de B.
     * ------------------- Postcondición --------------------------
     * matrizRetorno es una matriz con el producto de A por B
     *     \/ Se lanza una excepción pues las dimensiones de A y B
     *        no son adecuadas.
     */
    var n: Int
    var m: Int
    var mB: Int
    var p: Int
    var matrizRetorno: MutableList<MutableList<Int>> = mutableListOf()
    // Comprobamos que las matrices no estén vacías:
    if (A.count() == 0) {
        throw RuntimeException("Error, no se puede hallar el producto " +
            "de las matrices A y B, pues la matriz A no tiene elementos.")
    }
    if (B.count() == 0) {
        throw RuntimeException("Error, no se puede hallar el producto " +
            "de las matrices A y B, pues la matriz B no tiene elementos.")
    }
    // Calculamos el número de filas y columnas de A:
    n = A.count()
    m = (A.elementAt(0)).count()
    for (fila in A) {
        if (fila.count() != m) {
            throw RuntimeException("Error, las columnas de A no tienen " +
                "una dimension fija.")
        } else if (fila.count() == 0) {
            throw RuntimeException("Error, existe una fila con cero " +
                "columnas en la matriz A.")
        }
    }
    // Calculamos el número de filas y columnas de B:
    mB = B.count()
    p = (B.elementAt(0)).count()
    for (fila in B) {
        if (fila.count() != p) {
            throw RuntimeException("Error, las columnas de B no tienen " +
                "una dimension fija.")
        } else if (fila.count() == 0) {
            throw RuntimeException("Error, existe una fila con cero " +
                "columnas en la matriz B.")
        }
    }
    // Comprobamos que el número columnas de A coincida con el
    // número de filas de B:
    if (m != mB) {
        throw RuntimeException("Error, no se puede calcular el producto " +
            "de las matrices A y B, puesto que A el numero de columnas " +
            "de A ($m) no coincide con el numero de filas de B ($mB).")
    }
    // Si no hay problemas con las matrices añadimos en la matriz
    // resultante el número de filas y columnas correctos:
    for (i in 0..(n-1)) {
        matrizRetorno.add(mutableListOf())
        for (j in 0..(p-1)) {
            matrizRetorno[i].add(0)
        }
    }
    // Hacemos la multiplicación:
    for (i in 0..(n-1)) {
        for (j in 0..(p-1)) {
            for (k in 0..(m-1)) {
                matrizRetorno[i][j] += ((A.elementAt(i)).elementAt(k) *
                                        (B.elementAt(k)).elementAt(j))
            }
        }
    }
    return matrizRetorno
}