frase = str(input('Digite uma frase: ')).strip()
print('A Letra A aparece {} vezes'.format(frase.lower().count('a')))
print('O Primeiro A se encontra na posição {}.'.format(frase.lower().find('a')+1))
print('A última vez que parece o A é na posição {} '.format(frase.lower().rfind('a')+1))
print(len(frase))