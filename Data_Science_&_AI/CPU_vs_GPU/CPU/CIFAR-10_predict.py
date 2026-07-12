import random
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10

# ==========================
# NOMES DAS CLASSES
# ==========================

classes = [
    "Avião",
    "Automóvel",
    "Pássaro",
    "Gato",
    "Cervo",
    "Cachorro",
    "Sapo",
    "Cavalo",
    "Navio",
    "Caminhão"
]

# ==========================
# CARREGA O DATASET
# ==========================

(_, _), (test_X, test_y) = cifar10.load_data()

test_X = torch.tensor(test_X, dtype=torch.float32) / 255.0
test_X = test_X.permute(0, 3, 1, 2)

test_y = torch.tensor(test_y.squeeze(), dtype=torch.long)

# ==========================
# REDE
# ==========================

class CIFARNet(nn.Module):

    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32),

            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),

            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(128),

            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(128 * 4 * 4, 512),
            nn.ReLU(),

            nn.Dropout(0.5),

            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

# ==========================
# CARREGA O MODELO
# ==========================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CIFARNet()

model.load_state_dict(torch.load("cifar_10_model_cpu.pth", map_location=device))

model.to(device)
model.eval()

print("Modelo carregado com sucesso!")

# ==========================
# ESCOLHE UMA IMAGEM
# ==========================

indice = random.randint(0, len(test_X)-1)

imagem = test_X[indice].unsqueeze(0).to(device)

label_real = test_y[indice].item()

# ==========================
# PREDIÇÃO
# ==========================

with torch.no_grad():

    output = model(imagem)

    probabilidades = torch.softmax(output, dim=1)

    predicao = torch.argmax(probabilidades).item()

# ==========================
# RESULTADOS
# ==========================

print("="*60)
print(f"Índice da imagem : {indice}")
print(f"Classe verdadeira: {classes[label_real]}")
print(f"Classe prevista  : {classes[predicao]}")
print("="*60)

# ==========================
# TODAS AS PROBABILIDADES
# ==========================

probs = probabilidades.squeeze().cpu()

ranking = torch.argsort(probs, descending=True)

print("\nRanking das probabilidades:\n")

for i in ranking:

    print(f"{classes[i]:12s}: {probs[i]*100:6.2f}%")

# ==========================
# MOSTRA IMAGEM
# ==========================

imagem_plot = test_X[indice].permute(1,2,0).numpy()

plt.figure(figsize=(6,6))
plt.imshow(imagem_plot)

plt.title(
    f"Classe Real: {classes[label_real]}\n"
    f"Predição: {classes[predicao]}"
)

plt.axis("off")
plt.show()