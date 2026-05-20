#Criação e Acesso: Crie uma lista com 5 nomes de cidades. Imprima apenas a primeira e a última cidade da lista

cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza']
print(cidades[0])
print(cidades[-1])

print('.'*30)

#Alteração Manual: Dada a lista numeros = [10, 20, 30, 40, 50], altere o valor do terceiro elemento para 100 e imprima a lista atualizada

numeros = [10, 20, 30, 40, 50]
numeros[2] = 100
print(numeros)

print('.'*30)

#Entrada Dinâmica: Crie um programa que peça ao usuário 5 números, adicione-os em uma
#lista usando .append() e, ao final, exiba a soma de todos os itens (use a função sum()

numeros = []
for i in range(1, 6):
    num = int(input('digite um numero: '))
    numeros.append(num)
soma = sum(numeros)

print('.'*30)

print(numeros)
print('.'*30)
print(f'A soma dos numeros é: {soma}')
print('.'*30) 