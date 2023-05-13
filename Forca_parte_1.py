seu_nome = input("Digite seu nome para iniciar o jogo: ")

print(f"Bem vindo, {seu_nome}, ao jogo de forca", "\n")

palavra_secreta = "banana".upper()
letras_acertadas = []
for letra in palavra_secreta:
    letras_acertadas.append("_")

enforcou = False
acertou = False
tentativas: int = 1
total_tentativas = len(letras_acertadas)

print(letras_acertadas, "\n")

while (not enforcou and not acertou):
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()

    if (chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrado a letra {} na posição {}".format(chute, index))
                letras_acertadas[index] = letra
            index += 1
    else:
        tentativas += 1

    print("{}, você está na rodada {} de {}".format(seu_nome, tentativas, total_tentativas))

    enforcou = tentativas == len(letras_acertadas)

    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
    print("jogando...", "\n")

if (acertou):
    print("Você ganhou")
else:
    print("Você perdeu")

print("Fim do jogo")