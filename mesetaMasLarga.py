from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

# Todos los elementos de la lista entre dos índices tienen que ser iguales.
# mesetaMasLarga([1,2,3,4,5,6]) dará 1, mesetaMasLarga([1,2,2,2,3,4,4]) dará 3, pues hay tres 2 seguidos
def mesetaMasLarga(l: List[int]) -> int :
  
  if len(l) == 0: return 0
  
  def maximo(l1: int, l2: int) -> int:
    if l1 > l2:
      return l1
    else:
      return l2
  
  meseta_mas_larga: int = 1
  meseta_actual: int = 1
  for i in range(1, len(l)):
    if l[i] == l[i-1]:
      meseta_actual += 1
    else:
      meseta_mas_larga = maximo(meseta_actual, meseta_mas_larga)
      meseta_actual = 1
      
  return maximo(meseta_mas_larga,meseta_actual)

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))