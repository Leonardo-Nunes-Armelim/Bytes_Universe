import random

play = True
sort = True


while play:

    if sort == True:
        number = random.randint(1, 10)
        sort = False
        print('Adivinha o número que estou pensando')
    
    guess = int(input('Resposta: '))

    if guess == number:
        print('Isso mesmo, você acertou!')
        replay = input('Quer jogar de novo? (sim/não)\nResposta: ')
        if replay == 'sim':
            sort = True
        else:
            play = False
    elif guess < number:
        print('Não, o número que estou pensando é maior')
    else:
        print('Não, o número que estou pensando é menor')
