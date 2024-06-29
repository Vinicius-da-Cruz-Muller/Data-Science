def torre_hanoi(n, origem, destino, auxiliar):

  if n == 1:
    print(f"Mover anel {n} de {origem} para {destino}")
    return

  # Move os anéis menores para a torre do meio, usando a torre de destino como auxiliar.
  torre_hanoi(n - 1, origem, auxiliar, destino)

  # Move o anel maior para a torre de destino.
  print(f"Mover anel {n} de {origem} para {destino}")

  # Move os anéis menores da torre do meio para a torre de destino, usando a torre de origem como auxiliar.
  torre_hanoi(n - 1, auxiliar, destino, origem)

def main():

  while True:
    try:
      n = int(input("Digite o número de anéis (entre 2 e 6): "))
      if 2 <= n <= 6:
        break
      else:
        print("Número inválido. Digite um valor entre 2 e 6.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

  origem = 1
  destino = 3

  torre_hanoi(n, origem, destino, origem + 1)

if __name__ == "__main__":
  main()
