

cpf = int(input("Digite o seu CPF: "))  #Esta parte do código pede para escrever seu cpf e o torna uma váriavel

if cpf < 11:   #Cria a condição de que se a váriavel não tiver os 11 digitos será considerado inválido
    print ("CPF inválido!")

else: #Caso contrário o CPF será considerdo válido
    print("CPF válido!")
