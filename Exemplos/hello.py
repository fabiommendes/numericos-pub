nome = input('Nome: ')
idade = input('Idade: ')
idade = float(idade)
idade_para_aposentar = 65
anos = idade_para_aposentar - idade
print('Hello', nome + '!')
print('Você vai se aposentar daqui a %.2f anos!' % anos)
