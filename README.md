
# CODE OF READ CPF

``` scpf = input("Digite o seu CPF: ") ```

``` cpf = scpf.replace('.', '').replace('-', '').replace(' ', '') ```


``` if len(cpf) == 11 and cpf.isdigit(): ```
     
  ```   nums = [int(d) for d in cpf] ```
    

 ```   s1 = sum(nums[i] * (10 - i) for i in range(9)) ```
  ```  dv1 = (s1 * 10) % 11 ```
 ```   if dv1 == 10: dv1 = 0 ```
    
  
 ```   s2 = sum(nums[i] * (11 - i) for i in range(10)) ```
  ```  dv2 = (s2 * 10) % 11 ```
   ```  if dv2 == 10: dv2 = 0 ```
    

     ``` if dv1 == nums[9] and dv2 == nums[10] and not all(nums[i] == nums[i+1] for i in range(10)): 
        print("CPF válido!")  
   else: 
   print("CPF inválido!") ```
 










## EXAMPLE OF CPF
![Logo](https://cr.inf.br/blog/wp-content/uploads/2021/04/cpf-modelo-gestao-estrategia-cr-sistemas-e-web-linko-comercial.png)

## CLONE CODE

Clone the project

```bash
  git clone https://github.com/LelisCode/mileni-validar-cpf.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```




## Authors

- [@leliscode](https://github.com/LelisCode)
