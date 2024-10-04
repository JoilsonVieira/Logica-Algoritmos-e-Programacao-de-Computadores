# Defina uma função chamada “loginUsuario”. Tal instrução receberá cini
# parâmetro a variável perfil;
# No escopo da função, verifique se o valor do parâmetro perfil é igual a
# ‘admin’. Dica: considere que o usuário poderá digitar letras maiúsculas e/
# ou minúsculas na entrada de dados. Portanto, utilize a instrução lower no
# momento de fazer a verificação;
# Caso o valor do parâmetro seja igual a ‘admin’, imprima na tela: ‘Bem-
# vindo, Administrador’. Do contrário, imprima: ‘Bem-vindo, Usuário’;
# Por último, fora do escopo da função, faça a chamada da mesma passando
# diferentes valores como parâmetro. Ex:
# Admin
# admin
# User
# usuário
# etc.

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('maria')
loginUsuario('joilson')
    
    