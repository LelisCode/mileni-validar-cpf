
scpf = input("Digite o seu CPF: ") #input do cpf


cpf = scpf.replace(".", "").replace("-", "") #limpeza do cpf de qualquer traço

if len(cpf) == 11 and cpf.isdigit(): #cpf válido apenas com números e 11 dígitos
    print("CPF válido!")
else:
    print("CPF inválido!")

 #Estrutura de decisão a qual ira ler sua váriavel e ver se foram digitados apenas números(is.digit), retirar traços digitados(replace) e confirmar que são 11 digitos.
