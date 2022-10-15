# Problema de lavanderia

## Objetivo

Determinar la cantidad de lavados y la ropa que contiene cada uno para minimizar el tiempo de lavado total, entre los lavados, en el plazo de 1 dia.

## Constantes
T_i: Tiempo de la ropa i-esima en lavarse
M: Lavado muy grande

## Variables
***ropa_ij***: Es 1 si la ropa i-esima entra en el lavado j-esimo; 0 si no.
***lavado_j***: Es 1 si el lavado j-esimo efectivamente es un lavado real.
***mt_j***: Es el mayor tiempo del lavado j-esimo.

## Modelo

### Lavados existentes
"La ropa ij solamente puede valer 1, si el lavado j es uno que se utilizará".

***ropa_ij*** <= ***lavado_j*** ; para toda ropa i y lavado j.

### Ropa incompatible
Suponiendo que tenemos una incompatibilidad entre la ropa ***x*** y la ropa ***y***, entonces:

ropa_xj + ropa_yj <= 1 ; para todo lavado j.


### Tiempo maximo de lavado

mt_j <= M . lavado_j ; para todo lavado j.
mt_j >= T_i * ropa_ij ; para toda ropa i y lavado j.

## Funcional

min Z = ∑ mt_j ; siendo j desde 1 hasta m (siendo m la cantidad de lavados)
