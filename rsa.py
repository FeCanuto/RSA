#!/bin/bash/env python
# coding=UTF-8

import random
import primo


def totient(number):
    '''
    Calcula o totiente do numero primo: para um número natural n, 
    a função phi (totient) é definida como sendo igual à quantidade de números menores que n, 
    coprimos com respeito a ele. Se number é primo a função phi(x) = number - 1.
    '''
    if (primo.verificar_primo(number)):
        return number-1
    else:
        return False


def co_primo(num, value):
    '''
    Verificando se números são co-primos
    '''
    def mdc(n1, n2):
        rest = 1
        while (n2 != 0):
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        if (mdc(num, value) == 1):
            return value


def mod(a, b):  # Função modular
    '''
    Função modular entre dois números
    '''
    if (a < b):
        return a
    else:
        c = a % b
        return c


def cipher(words, e, n):  # obter as palavras e calcular a cifra
    '''
    Cifra um texto
    '''
    tam = len(words)
    i = 0
    lista = []
    while (i < tam):
        letter = words[i]
        # ord () retorna o valor Unicode de um determinado objeto
        k = ord(letter)
        k = k**e
        d = mod(k, n)
        lista.append(d)
        i += 1
    return lista


def descifra(cifra, n, d):
    '''
    Descriptografa um texto criptografado
    '''
    lista = []
    i = 0
    tamanho = len(cifra)
    # texto = cifra ^ d mod n
    while i < tamanho:
        result = cifra[i]**d
        texto = mod(result, n)
        # chr () função Toma um inteiro i e converte-o para o caracter c , de modo que retorna uma sequência de caracteres
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista


def calculando_chave_privada(toti, e):
    '''
    Calcula a chave privada
    '''
    d = 0
    while (mod(d*e, toti) != 1):
        d += 1
    return d
