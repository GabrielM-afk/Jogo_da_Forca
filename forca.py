palavra = str(input("Digite uma palavra para o Jogo da Forca: ").upper())

letras_desc = []

print("\n*** Jogo da Forca ***\n")

for i in range(0, len(palavra)) :
    letras_desc.append("-")

acertou = False

while acertou == False :
    letra = str(input("Digita uma letra: ").upper())
    
    for i in range(0, len(palavra)) : 
        if letra == palavra[i] :
            letras_desc[i] = letra
        
        print(letras_desc[i])
    
    acertou = True

    for x in range(0, len(letras_desc)) :
        if letras_desc[x] == "-" :
            acertou = False

print('Boa cidadão !')