import sys

def quienGana(j1: str, j2: str) -> str : 
  
    def ganar(ja: str, jb: str) -> bool:
      piedra_tijera: bool = ja == "Piedra" and jb == "Tijera"
      tijera_papel: bool = ja == "Tijera" and jb == "Papel"
      papel_piedra: bool = ja == "Papel" and jb == "Piedra"
      return piedra_tijera or tijera_papel or papel_piedra
    
    if ganar(j1,j2):
      return "Jugador1"
    elif ganar(j2,j1):
      return "Jugador2"
    else:
      return "Empate"
        

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))