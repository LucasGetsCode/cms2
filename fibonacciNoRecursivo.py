import sys

def fibonacciNoRecursivo(n: int) -> int:
  i = 1
  lista = [0, 1]
  while i < n+1:
    lista.append(lista[i] + lista[i-1])
    i += 1
  # print(lista)
  return lista[len(lista)-2]


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))