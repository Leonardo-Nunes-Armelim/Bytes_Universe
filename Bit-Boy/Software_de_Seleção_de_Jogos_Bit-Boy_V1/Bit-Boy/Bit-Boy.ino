#include "buttons.h"
#include "display.h"
#include "menu.h"
#include "speaker.h"
#include "utils.h"

#include "simon.h"
#include "sokoban.h"
#include "pong.h"

//#include "system/menu.h"
//#include "config.h"

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

  if (!menu.in_game) {
    menu.game_selection();
  } else {
    if (menu.game_index == 0) {
      simon.game();
    } else if (menu.game_index == 1) {
      sokoban.game();
    } else if (menu.game_index == 2) {
      pong.game();
    } else if (menu.game_index == 3) {
      speaker.star_wars_cantina_song();
      menu.in_game = false;
    } else if (menu.game_index == 4) {
      buttons.example();
    } else if (menu.game_index == 5) {
      // Tetris
      menu.in_game = false;
    } else if (menu.game_index == 6) {
      // Jogo da Velha
      menu.in_game = false;
    } else if (menu.game_index == 7) {
      // Jogo da Cobrinha
      menu.in_game = false;
    }
  }

  display.display();
}