nome = input('digite seu nome completo: ')
n = nome.index(' ')
primeiro_nome = nome[0:n] 
#o : é um intervalo = vai de 0 ate n
print(f'bem-vindo ao Python, {primeiro_nome}')

#usando split

nome = input('digite seu nome completo: ')
p = nome.split()
print('bem-vindo ao Python,', p[0])