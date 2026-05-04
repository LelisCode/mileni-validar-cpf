cpf = int(input("Digite o seu CPF: "))  

if len(cpf) == 11 and cpf.isdigit():  #Estrutura de decisão a qual ira ler sua váriavel e ver se foram digitados apenas números
    
    
    print ("CPF válido!")

else:
    print("CPF inválido!")
