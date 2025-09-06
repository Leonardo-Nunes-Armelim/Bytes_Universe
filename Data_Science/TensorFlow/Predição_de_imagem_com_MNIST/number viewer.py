from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Carregar o dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print('\nIniciando modo de visualização de números...\n')

loop = True
error = False

while loop:
    if error:
        print('Você digitou uma resposta invalida.')
        error = False

    response = input('Escolha um index de exibição de um número. (0 à 59999)\nOu digite "sair".\nResposta: ')

    if response == 'sair':
        loop = False
    else:
        try:
            index = int(response)
            print('Número:', y_train[index])
            plt.imshow(x_train[index], cmap='binary')
            plt.axis('off')
            plt.show()
        except:
            error = True
    print()