import random
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# ==========================
# CARREGA O DATASET
# ==========================

(_, _), (test_X, test_y) = mnist.load_data()

test_X = torch.tensor(test_X, dtype=torch.float32) / 255.0
test_X = test_X.view(-1, 28 * 28)

test_y = torch.tensor(test_y, dtype=torch.long)

# ==========================
# DISPOSITIVO
# ==========================

device = torch.device("cpu")

# ==========================
# RECRIA A REDE
# ==========================

model = nn.Sequential(
    nn.Linear(784, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

# ==========================
# CARREGA O MODELO TREINADO
# ==========================

model.load_state_dict(torch.load("mnist_model_cpu.pth", map_location=device))
model.to(device)
model.eval()

print("Modelo carregado com sucesso!")

# ==========================
# ESCOLHE UMA IMAGEM ALEATÓRIA
# ==========================

indice = random.randint(0, len(test_X) - 1)

imagem = test_X[indice].unsqueeze(0).to(device)
label_real = test_y[indice].item()

# ==========================
# FAZ A PREDIÇÃO
# ==========================

with torch.no_grad():
    output = model(imagem)

    probabilidades = torch.softmax(output, dim=1)

    predicao = torch.argmax(probabilidades, dim=1).item()

    confianca = probabilidades[0][predicao].item() * 100

# ==========================
# EXIBE O RESULTADO
# ==========================

print(f"Rótulo verdadeiro : {label_real}")
print(f"Predição do modelo: {predicao}")
print(f"Confiança         : {confianca:.2f}%")

plt.figure(figsize=(5, 5))
plt.imshow(test_X[indice].view(28, 28), cmap="gray")

plt.title(
    f"Real: {label_real}\n"
    f"Predição: {predicao}\n"
    f"Confiança: {confianca:.2f}%"
)

plt.axis("off")
plt.show()