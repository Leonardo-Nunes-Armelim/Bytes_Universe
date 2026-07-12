import time
import torch
import torch.nn as nn
import torch.optim as optim
from tensorflow.keras.datasets import cifar100
from torch.utils.data import TensorDataset, DataLoader

# ==========================
# CARREGA CIFAR-100
# ==========================

(train_X, train_y), (test_X, test_y) = cifar100.load_data(label_mode="fine")

train_X = torch.tensor(train_X, dtype=torch.float32) / 255.0
test_X = torch.tensor(test_X, dtype=torch.float32) / 255.0

# (N, H, W, C) -> (N, C, H, W)
train_X = train_X.permute(0, 3, 1, 2)
test_X = test_X.permute(0, 3, 1, 2)

train_y = torch.tensor(train_y.squeeze(), dtype=torch.long)
test_y = torch.tensor(test_y.squeeze(), dtype=torch.long)

train_loader = DataLoader(
    TensorDataset(train_X, train_y),
    batch_size=256,
    shuffle=True,
    pin_memory=True
)

test_loader = DataLoader(
    TensorDataset(test_X, test_y),
    batch_size=256,
    pin_memory=True
)

# ==========================
# CNN
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

            # CIFAR-100 = 100 classes
            nn.Linear(512, 100)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

model = CIFARNet()

# ==========================
# GPU SETUP
# ==========================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 30

# ==========================
# TREINAMENTO
# ==========================

torch.cuda.synchronize()
inicio = time.perf_counter()

for epoch in range(epochs):

    model.train()
    loss_medio = 0

    for images, labels in train_loader:

        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        loss_medio += loss.item()

    loss_medio /= len(train_loader)

    print(f"Epoch {epoch+1:02d}/{epochs} - Loss: {loss_medio:.4f}")

torch.cuda.synchronize()
fim = time.perf_counter()

# ==========================
# TESTE
# ==========================

model.eval()

corretos = 0
total = 0

with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        corretos += (predicted == labels).sum().item()

accuracy = 100 * corretos / total

print(f"\nAcurácia: {accuracy:.2f}%")
print(f"Tempo treinamento GPU: {fim - inicio:.2f} segundos")

total_params = sum(p.numel() for p in model.parameters())
print(f"Parâmetros da rede: {total_params:,}")

print(f"GPU utilizada: {torch.cuda.get_device_name(0)}")

# ==========================
# SALVAR MODELO
# ==========================

torch.save(model.state_dict(), "cifar_100_model_gpu.pth")

print("Modelo salvo com sucesso!")