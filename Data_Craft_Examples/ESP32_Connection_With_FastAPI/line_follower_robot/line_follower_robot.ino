#include <WiFi.h>
#include <esp_now.h>

typedef struct {
  int numero;
} Telemetria;

Telemetria dados;

uint8_t gatewayMac[] = {0x34, 0x85, 0x18, 0xAB, 0xCD, 0xEF};

int contador = 1;
unsigned long ultimoEnvio = 0;

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Erro ESP-NOW");
    return;
  }

  esp_now_peer_info_t peerInfo = {};

  memcpy(peerInfo.peer_addr, gatewayMac, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  esp_now_add_peer(&peerInfo);
}

void loop() {

  if (millis() - ultimoEnvio > 2000) {

    ultimoEnvio = millis();

    dados.numero = contador;

    esp_now_send(
      gatewayMac,
      (uint8_t*)&dados,
      sizeof(dados)
    );

    Serial.print("Enviado: ");
    Serial.println(contador);

    contador++;

    if (contador > 10)
      contador = 1;
  }
}