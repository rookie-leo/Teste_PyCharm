def soma(x, z):
    return x + z

lang = str(input('Português/English? [P/E]')).upper()

if lang in 'PPORTUGUÊSPORTUGUES':
    x = int(input('Digite um número: '))

elif lang in 'EENGLISH':
    x = int(input('Type a number: '))
    y = int(input('Type a number: '))
