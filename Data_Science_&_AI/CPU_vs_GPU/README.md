# CPU vs GPU - Treinando Redes Neurais com PyTorch

Este repositório reúne os códigos utilizados no vídeo do YouTube em que comparei o desempenho do treinamento de redes neurais utilizando **CPU** e **GPU** com **PyTorch**.

Foram realizados testes utilizando diferentes datasets para mostrar como o hardware influencia o tempo de treinamento mantendo a mesma arquitetura e configuração de treinamento.

## 📺 Vídeo no YouTube

> **Assista ao vídeo:** *(adicione o link aqui)*

---

# Datasets utilizados

- MNIST
- CIFAR-10
- CIFAR-100

Todos os modelos foram implementados em **PyTorch**.

---

# Estrutura do projeto

```text
.
│   README.md
│
├───CPU
│       MNIST.py
│       MNIST_predict.py
│       mnist_model_cpu.pth
│
│       CIFAR-10.py
│       CIFAR-10_predict.py
│       cifar_10_model_cpu.pth
│
│       CIFAR-100.py
│       CIFAR-100_predict.py
│       cifar_100_model_cpu.pth
│
│       requirements.txt
│
└───GPU
        MNIST.py
        MNIST_predict.py
        mnist_model_gpu.pth

        CIFAR-10.py
        CIFAR-10_predict.py
        cifar_10_model_gpu.pth

        CIFAR-100.py
        CIFAR-100_predict.py
        cifar_100_model_gpu.pth

        requirements.txt
```

---

# Criando o ambiente virtual

```bash
python -m venv ./venv
.\venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

> Execute os comandos dentro da pasta **CPU** ou **GPU**, dependendo do benchmark que deseja executar.

---

# Como executar

### CPU

```bash
cd CPU

python MNIST.py
python CIFAR-10.py
python CIFAR-100.py
```

### GPU

```bash
cd GPU

python MNIST.py
python CIFAR-10.py
python CIFAR-100.py
```

---

# Modelos treinados

Após o treinamento serão gerados os seguintes arquivos:

### CPU

- `mnist_model_cpu.pth`
- `cifar_10_model_cpu.pth`
- `cifar_100_model_cpu.pth`

### GPU

- `mnist_model_gpu.pth`
- `cifar_10_model_gpu.pth`
- `cifar_100_model_gpu.pth`

---

# Predições

Após treinar um modelo é possível realizar inferências utilizando:

```bash
python MNIST_predict.py
python CIFAR-10_predict.py
python CIFAR-100_predict.py
```

---

# Objetivo

O objetivo deste projeto é comparar o desempenho entre CPU e GPU durante o treinamento de modelos de Deep Learning, observando fatores como:

- Tempo de treinamento
- Acurácia
- Utilização de hardware
- Diferença de desempenho entre diferentes datasets

---

# Tecnologias

- Python
- PyTorch
- TensorFlow (apenas para carregamento dos datasets)
- NumPy

---

# Licença

Este projeto é disponibilizado para fins de estudo e aprendizado.