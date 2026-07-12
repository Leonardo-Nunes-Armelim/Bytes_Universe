import random
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar100

# ======================================================
# NOMES DAS 100 CLASSES DO CIFAR-100
# ======================================================

classes = [
    "apple","aquarium_fish","baby","bear","beaver","bed","bee","beetle",
    "bicycle","bottle","bowl","boy","bridge","bus","butterfly","camel",
    "can","castle","caterpillar","cattle","chair","chimpanzee","clock",
    "cloud","cockroach","couch","crab","crocodile","cup","dinosaur",
    "dolphin","elephant","flatfish","forest","fox","girl","hamster",
    "house","kangaroo","keyboard","lamp","lawn_mower","leopard","lion",
    "lizard","lobster","man","maple_tree","motorcycle","mountain",
    "mouse","mushroom","oak_tree","orange","orchid","otter","palm_tree",
    "pear","pickup_truck","pine_tree","plain","plate","poppy",
    "porcupine","possum","rabbit","raccoon","ray","road","rocket",
    "rose","sea","seal","shark","shrew","skunk","skyscraper","snail",
    "snake","spider","squirrel","streetcar","sunflower","sweet_pepper",
    "table","tank","telephone","television","tiger","tractor","train",
    "trout","tulip","turtle","wardrobe","whale","willow_tree","wolf",
    "woman","worm"
]

# ======================================================
# CARREGA O DATASET
# ======================================================

(_, _), (test_X, test_y) = cifar100.load_data(label_mode="fine")

test_X = torch.tensor(test_X, dtype=torch.float32) / 255.0
test_X = test_X.permute(0,3,1,2)

test_y = torch.tensor(test_y.squeeze(), dtype=torch.long)

# ======================================================
# REDE
# ======================================================

class CIFARNet(nn.Module):

    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3,32,3,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32),

            nn.Conv2d(32,32,3,padding=1),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(32,64,3,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(64),

            nn.Conv2d(64,64,3,padding=1),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(64,128,3,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(128),

            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(128*4*4,512),
            nn.ReLU(),

            nn.Dropout(0.5),

            nn.Linear(512,100)
        )

    def forward(self,x):
        x=self.features(x)
        x=self.classifier(x)
        return x

# ======================================================
# CARREGA MODELO
# ======================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CIFARNet()

model.load_state_dict(
    torch.load("cifar_100_model_gpu.pth", map_location=device)
)

model.to(device)
model.eval()

print("Modelo carregado!")

# ======================================================
# ESCOLHE UMA IMAGEM ALEATÓRIA
# ======================================================

indice = random.randint(0,len(test_X)-1)

imagem = test_X[indice].unsqueeze(0).to(device)

label_real = test_y[indice].item()

# ======================================================
# PREDIÇÃO
# ======================================================

with torch.no_grad():

    output = model(imagem)

    probs = torch.softmax(output,dim=1).squeeze()

pred = torch.argmax(probs).item()

# ======================================================
# RESULTADO
# ======================================================

print("="*70)

print("Índice:",indice)
print("Classe verdadeira :",classes[label_real])
print("Classe prevista   :",classes[pred])

print("="*70)

# ======================================================
# TOP 10 MAIS PROVÁVEIS
# ======================================================

ranking = torch.argsort(probs,descending=True)

print("\nTop 10 previsões:\n")

for i in range(10):

    idx = ranking[i].item()

    print(
        f"{i+1:2d}º "
        f"{classes[idx]:20s}"
        f"{probs[idx]*100:7.2f}%"
    )

print("\nClasse correta:", classes[label_real])

# ======================================================
# MOSTRA IMAGEM
# ======================================================

plt.figure(figsize=(6,6))

plt.imshow(test_X[indice].permute(1,2,0))

plt.title(
    f"Classe Real: {classes[label_real]}\n"
    f"Predição: {classes[pred]}"
)

plt.axis("off")

plt.show()