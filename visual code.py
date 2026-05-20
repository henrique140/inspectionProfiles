usuario = input ('digite seu usuario: ')
usuario == 'admin'
senha == '1234'

while usario != 'admin' or senha != '1234':
    print ('Usuário ou senha incorretos. Tente novamente.')
    usuario = input ('digite seu usuario: ')
    senha = input ('digite sua senha: ')
    print ('Bem-vindo, admin!')
