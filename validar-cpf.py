# Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
#   CPF válido! ou
#   CPF inválido!

cpf = int(input("Digite o seu CPF: "))

if cpf < 11:
    print ("CPF inválido!")

else:
    print("CPF válido!")