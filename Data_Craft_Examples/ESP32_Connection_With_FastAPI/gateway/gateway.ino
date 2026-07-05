#include <WiFi.h>
#include <esp_now.h>

typedef struct {
  int numero;
} Telemetria;

Telemetria dadosRecebidos;

void onReceive(
    const esp_now_recv_info_t *info,
    const uint8_t *incomingData,
    int len)
{
  memcpy(
      &dadosRecebidos,
      incomingData,
      sizeof(dadosRecebidos));

  Serial.println(dadosRecebidos.numero);
}

void setup() {

  Serial.begin(115200);

  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Erro ESP-NOW");
    return;
  }

  esp_now_register_recv_cb(onReceive);

  Serial.println("Gateway pronto");
}

void loop() {
}