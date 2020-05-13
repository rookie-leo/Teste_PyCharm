def linha():
    print('-=-' * 30)


def soma(x, z):
    s = x + z
    linha()
    print(f'{x}+{y}={s}')


lang = str(input('Português/English? [P/E]')).upper()

if lang in 'PPORTUGUÊSPORTUGUES':
    x = int(input('Digite um número: '))
    y = int(input('Digite um número: '))
    soma(x, y)

elif lang in 'EENGLISH':
    x = int(input('Type a number: '))
    y = int(input('Type a number: '))
    soma(x, y)
