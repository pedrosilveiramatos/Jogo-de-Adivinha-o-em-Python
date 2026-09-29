# Jogo de adivinhação: o jogador tenta descobrir um número secreto entre 1 e 100.
# A cada chute, o programa diz se o número secreto é maior ou menor.

import random

secreto = random.randint(1, 100)
chute = 0
chutes = []

while chute != secreto:
    chute = int(input("chute um numero de 1 a 100: "))
    chutes.append(chute)
    
    if chute > secreto:
        print(f"Tente um numero menor que {chute}.")   
    elif chute < secreto:
        print(f"Tente um numero maior que {chute}.")

print()
print("PARABENS!!")
print("Você acertou!!")
print(f"numero de tentativas: {len(chutes)}")
print(f"tentativas: {chutes}")

input("\nPressione Enter para sair...")
