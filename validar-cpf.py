# Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
#   CPF válido! ou
#   CPF inválido!
scpf = input("Digite o seu CPF: ")

cpf = scpf.replace('.', '').replace('-', '').replace(' ', '')


if len(cpf) == 11 and cpf.isdigit():
    

    nums = [int(d) for d in cpf]
    

    soma1 = sum(nums[i] * (10 - i) for i in range(9))
    dv1 = (soma1 * 10) % 11
    if dv1 == 10: dv1 = 0
    
  
    soma2 = sum(nums[i] * (11 - i) for i in range(10))
    dv2 = (soma2 * 10) % 11
    if dv2 == 10: dv2 = 0
    

    if dv1 == nums[9] and dv2 == nums[10] and not all(nums[i] == nums[i+1] for i in range(10)):
        print("CPF válido!")
    else:
        print("CPF inválido!")
else:
    print("CPF inválido! Formato ou tamanho incorreto.")

