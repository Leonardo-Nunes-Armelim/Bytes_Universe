# Configuração e Execução

## 1. Obter o MAC Address do Gateway

Grave e execute o arquivo `gateway_mac.ino` no ESP32 que será utilizado como gateway.

Após abrir o Monitor Serial, será exibida uma mensagem semelhante a:

```text
MAC: 34:85:18:AB:CD:EF
```

Anote esse endereço MAC, pois ele será utilizado pelo robô para enviar os dados ao gateway.

---

## 2. Configurar o MAC do Gateway no Robô

No código do robô, localize a variável `gatewayMac` e substitua pelos valores obtidos na etapa anterior:

```cpp
uint8_t gatewayMac[] = {0x34, 0x85, 0x18, 0xAB, 0xCD, 0xEF};
```

Esse endereço identifica o ESP32 gateway que receberá os dados enviados pelo robô via ESP-NOW.

---

## 3. Gravar o Gateway

Após configurar o endereço MAC no robô, grave e execute o arquivo `gateway.ino` no ESP32 que atuará como receptor dos dados.

Este dispositivo será responsável por receber as mensagens via ESP-NOW e encaminhá-las para o computador através da porta serial.

---

## 4. Configurar a Porta Serial no Python

No arquivo `main.py`, ajuste a porta serial para a porta COM correspondente ao ESP32 gateway.

Exemplo:

```python
ser = serial.Serial("COM5", 115200, timeout=1)
```

Caso o ESP32 esteja conectado em outra porta, substitua `COM5` pelo valor correto.

Você pode verificar a porta utilizada pelo dispositivo no Gerenciador de Dispositivos do Windows.

---

## 5. Criar e Configurar o Ambiente Virtual Python

Criar o ambiente virtual:

```bash
python -m venv ./venv_LFR
```

Ativar o ambiente virtual:

```bash
.\venv_LFR\Scripts\activate.bat
```

Atualizar o pip:

```bash
python -m pip install --upgrade pip
```

Instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

Ou instalar manualmente:

```bash
pip install pyserial fastapi uvicorn
```

---

## 6. Executar o Servidor de Recepção de Dados

Inicie a API FastAPI com:

```bash
uvicorn main:app --reload
```

O servidor irá receber os dados enviados pelo gateway através da porta serial e disponibilizá-los via HTTP.

---

## 7. Visualizar os Dados Recebidos

Abra o navegador e acesse:

```text
http://127.0.0.1:8000/telemetry
```

Exemplo de resposta:

```json
{
    "numero": 2
}
```

Esse endpoint retorna o último valor recebido do ESP32 gateway.
