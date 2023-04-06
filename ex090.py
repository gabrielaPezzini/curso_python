'''resultado = list()
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
resultado.append(aluno.copy())
print('-=' * 30)
for a in resultado:
    for k, v in a.items():
        print(f' - {k} é igual a {v}')
if aluno['Média'] <= 5:
    print(' - A situação é igual Reprovado! ')
elif aluno['Média'] <= 7:
    print(' - A situação é igual Recuperação! ')
else:
    print(' - A situação é igual Aprovado! ')'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
