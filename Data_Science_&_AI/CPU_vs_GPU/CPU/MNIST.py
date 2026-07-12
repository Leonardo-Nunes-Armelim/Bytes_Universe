import time
import torch
import torch.nn as nn
import torch.optim as optim
from tensorflow.keras.datasets import mnist
from torch.utils.data import TensorDataset, DataLoader

# ==========================
# CARREGA MNIST
# ==========================

(train_X, train_y), (test_X, test_y) = mnist.load_data()

train_X = torch.tensor(train_X, dtype=torch.float32) / 255.0
test_X = torch.tensor(test_X, dtype=torch.float32) / 255.0

train_X = train_X.view(-1, 28 * 28)
test_X = test_X.view(-1, 28 * 28)

train_y = torch.tensor(train_y, dtype=torch.long)
test_y = torch.tensor(test_y, dtype=torch.long)

train_loader = DataLoader(
    TensorDataset(train_X, train_y),
    batch_size=256,
    shuffle=True
)

test_loader = DataLoader(
    TensorDataset(test_X, test_y),
    batch_size=256
)

# ==========================
# REDE NEURAL
# ==========================

model = nn.Sequential(
    nn.Linear(784, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

device = torch.device("cpu")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 10

# ==========================
# TREINAMENTO
# ==========================

inicio = time.perf_counter()

for epoch in range(epochs):

    model.train()

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

    print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

fim = time.perf_counter()

# ==========================
# TESTE
# ==========================

model.eval()

corretos = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        corretos += (predicted == labels).sum().item()

accuracy = 100 * corretos / total

print(f"\nAcurácia: {accuracy:.2f}%")
print(f"Tempo treinamento CPU: {fim - inicio:.2f} segundos")

# ==========================
# SALVAR MODELO
# ==========================

torch.save(model.state_dict(), "mnist_model_cpu.pth")

print("Modelo salvo com sucesso!")