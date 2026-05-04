scpf = int(input("Digite o seu CPF: "))  
cpf = scpf.replace(".", "").replace("-","")

if len(cpf) == 11 and cpf.isdigit(): 
  print ("CPF válido!")
    else:
    print("CPF inválido!")
 
 #Estrutura de decisão a qual ira ler sua váriavel e ver se foram digitados apenas números(is.digit), retirar traços digitados(replace) e confirmar que são 11 digitos.
