# Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
#   CPF válido! ou
#   CPF inválido!


scpf = input("Digite o seu CPF: ")


cpf = scpf.replace(".", "").replace("-", "")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido!")
else:
    print("CPF inválido!")
