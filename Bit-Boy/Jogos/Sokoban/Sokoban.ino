#include "buttons.h"
#include "display.h"
#include "speaker.h"
#include "utils.h"

#include "sokoban.h"


void setup() {
  //Serial.begin(9600);
  //Serial.println();

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }

  display.clearDisplay();

  // Logo Bit-Boy
  display.drawRoundRect(33, 4, 59, 53, 3, SSD1306_WHITE);
  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(37, 8);
  display.println(F("BIT"));
  display.setCursor(37, 32);
  display.println(F("BOY"));
  display.display();
  delay(500);

  buttons.init();
  speaker.init();

  display.display();
}

void loop() {
  display.clearDisplay();

  sokoban.game();

  display.display();
}