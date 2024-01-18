perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print('Pergunta: Quanto é 2 + 2?')
print()
print('Opções:')
print('a) 1')
print('b) 3')
print('c) 4')
print('d) 5')

usuario = input('Escolha uma opção: ')

acertos = 0
tentativas = 0
tentativas += 1
letras = 'a'

a = perguntas[0]['Opções'][0]
b = perguntas[0]['Opções'][1]
c = perguntas[0]['Opções'][2]
d = perguntas[0]['Opções'][3]

while len(usuario) > len(letras):
    print('Digitou mais de uma letra, tente novamente!')
    print('Pergunta: Quanto é 2 + 2?')
    print()
    print('Opções:')
    print('a) 1')
    print('b) 3')
    print('c) 4')
    print('d) 5')

    usuario = input('Escolha uma opção: ')

if usuario == 'c' or usuario == c:
    print('Boa, você acertou!')
    acertos += 1
else:
    print('Errou.')

print('Pergunta: Quanto é 5 * 5?')
print()
print('Opções:')
print('a) 25')
print('b) 55')
print('c) 10')
print('d) 51')

usuario = input('Escolha uma opção: ')
tentativas += 1

a = perguntas[1]['Opções'][0]
b = perguntas[1]['Opções'][1]
c = perguntas[1]['Opções'][2]
d = perguntas[1]['Opções'][3]

while len(usuario) > len(letras):
    if usuario.isdigit():
        break
    else:
        print('Digitou mais de uma letra, tente novamente!')
        print('Pergunta: Quanto é 5 * 5?')
        print()
        print('Opções:')
        print('a) 25')
        print('b) 55')
        print('c) 10')
        print('d) 51')
    usuario = input('Escolha uma opção: ')

if usuario == 'a' or usuario == a:
    print('Boa, você acertou!')
    acertos += 1
else:
    print('Errou.')

print('Pergunta: Quanto é 10 / 2?')
print()
print('Opções:')
print('a) 4')
print('b) 5')
print('c) 2')
print('d) 1')

usuario = input('Escolha uma opção: ')
tentativas += 1

a = perguntas[2]['Opções'][0]
b = perguntas[2]['Opções'][1]
c = perguntas[2]['Opções'][2]
d = perguntas[2]['Opções'][3]

while len(usuario) > len(letras):
    print('Digitou mais de uma letra, tente novamente!')
    print('Pergunta: Quanto é 10 / 2?')
    print()
    print('Opções:')
    print('a) 4')
    print('b) 5')
    print('c) 2')
    print('d) 1')

    usuario = input('Escolha uma opção: ')

if usuario == 'b' or usuario == b:
    print('Boa, você acertou!')
    acertos += 1
else:
    print('Errou.')

if len(usuario) > len(letras):
    print('Digitou mais de uma letra')


print(f'Você teve {acertos} acertos de {tentativas} tentativas')

print(f'Você teve {acertos} acertos de {tentativas} tentativas')

print(f'Você teve {acertos} acertos de {tentativas} tentativas')
