from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  
  def pertenece(algo: str, lista: list) -> bool:
    for i in lista:
      if algo == i: return True
    return False
  
  if len(vuelos) == 0:
    return -1
  quedan_vuelos: bool = True
  origen: str = origen
  combinaciones: int = 0
  viajados: list[str] = []
  # combinaciones_list: list = []
  # print(vuelos)
  i: int = 0
  while quedan_vuelos:
    if vuelos[i][0] == origen:
      if vuelos[i][1] == destino:
        # combinaciones_list.append(vuelos[i])
        # print(combinaciones_list)
        return combinaciones+1
      else:
        combinaciones += 1
        if pertenece(vuelos[i][0], viajados):
          quedan_vuelos = False
        viajados.append(vuelos[i][0])
        origen = vuelos[i][1]
        # combinaciones_list.append(vuelos[i])
        i = -1
    i += 1
    if i == len(vuelos):
      quedan_vuelos = False
  return -1
          

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))