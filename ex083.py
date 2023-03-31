expr = str(input('Digite a expressão: '))
pilha = list ()
for simbolo in expr:
    if simbolo == '(':
       pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0: # se tiver algo na expr
            pilha.pop() # vai retirar pq ele já encontrou o seu par
        else: # se não tiver nada
            pilha.append(')')
            break
if len(pilha) == 0: # cada parenteses que abriu teve a sua relação com o parenteses fechando]
    print('Sua expressão está válida!')
else: # se o len da pilha foi acima de 0
    print('Sua expressão está errada!')
