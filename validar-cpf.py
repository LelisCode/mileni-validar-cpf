# Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
#   CPF válido! ou
#   CPF inválido!

cpf = int(input("Digite o seu CPF: "))

if len(cpf) == 11 and cpf.isdigit():
    print ("CPF válido!")

else:
    print("CPF inválido!")
