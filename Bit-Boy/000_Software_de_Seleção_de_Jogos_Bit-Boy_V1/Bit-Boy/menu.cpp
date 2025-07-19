#include "buttons.h"
#include "display.h"
#include "speaker.h"
#include "sounds.h"
#include "menu.h"
#include "utils.h"

Menu menu;

//const char popup_option_1[] PROGMEM = "Beep sound";
//const char popup_option_2[] PROGMEM = "Clear memory";
//const char *const popup_menu_list[] = {popup_option_1, popup_option_2};

const char *popup_menu_list[] = {"Beep sound",
                                 "Clear memory"};

const char game_1[] PROGMEM = "Simon";
const char game_2[] PROGMEM = "Sokoban";
const char game_3[] PROGMEM = "Pong";
const char game_4[] PROGMEM = "Star Wars";
const char game_5[] PROGMEM = "Buttons Test";
const char game_6[] PROGMEM = "Tetris";
const char game_7[] PROGMEM = "Jogo da Velha";
const char game_8[] PROGMEM = "Jogo da Cobrinha";
const char game_9[] PROGMEM = "Adivinhe o Numero";
const char game_10[] PROGMEM = "Pedra Papel Tesoura";
const char game_11[] PROGMEM = "PPT Lagarto Spock";
const char game_12[] PROGMEM = "Jogo da Memória";
const char game_13[] PROGMEM = "Flappy Birds";
const char game_14[] PROGMEM = "Flow";
const char game_15[] PROGMEM = "Pac-Man";
const char game_16[] PROGMEM = "Uno";
const char game_17[] PROGMEM = "Travesia";

const char *const games_list[] PROGMEM = {game_1, game_2, game_3, game_4, game_5,
                                          game_6, game_7, game_8, game_9, game_10,
                                          game_11, game_12, game_13, game_14, game_15,
                                          game_16, game_17};

void Menu::game_selection() {
  buttons.b_state_up    = digitalRead(buttons.b_up);
  //buttons.b_state_right = digitalRead(buttons.b_right);
  buttons.b_state_down  = digitalRead(buttons.b_down);
  //buttons.b_state_left  = digitalRead(buttons.b_left);
  buttons.b_state_menu  = digitalRead(buttons.b_menu);
  buttons.b_state_R1    = digitalRead(buttons.b_R1);
  buttons.b_state_L1    = digitalRead(buttons.b_L1);
  buttons.b_state_a     = digitalRead(buttons.b_a);
  //buttons.b_state_b     = digitalRead(buttons.b_b);
  //buttons.b_state_x     = digitalRead(buttons.b_x);
  //buttons.b_state_y     = digitalRead(buttons.b_y);

  // Popup Menu
  if (buttons.b_state_menu == HIGH && popup_menu == false) {
    utils.popup_menu_index = 0;
    popup_menu = true;
    delay(200);
  } else if (buttons.b_state_menu == HIGH && popup_menu == true) {
    popup_menu = false;
    delay(200);
  }

  // Directional buttons
  if (buttons.b_state_up == HIGH && game_index >= 0) {
    if (popup_menu) {
      utils.popup_menu_index -= 1;
    } else {
      game_index -= 1;
    }
    if (utils.read_eeprom_beep()) {
      speaker.play_note(NOTE_C4, 100);
    }
    delay(100);
  } else if (buttons.b_state_down == HIGH && game_index <= 7) {
    if (popup_menu) {
      utils.popup_menu_index += 1;
    } else {
      game_index += 1;
    }
    if (utils.read_eeprom_beep()) {
      speaker.play_note(NOTE_C4, 100);
    }
    delay(100);
  }

  // Selection button
  if (buttons.b_state_a == HIGH) {
    if (popup_menu) {
      if (utils.popup_menu_index == 0) {
        if (utils.read_eeprom_beep()) {
          utils.update_eeprom_beep(false);
        } else {
          utils.update_eeprom_beep(true);
        }
      }

    } else {
      in_game = true;
    }
    if (utils.read_eeprom_beep()) {
      speaker.play_note(NOTE_C5, 100);
    }
    delay(100);
  }

  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);

  // Game name loop
  char buffer[20];
  for (int8_t i = 0; i < 8; ++i) {
    strcpy_P(buffer, (PGM_P)pgm_read_word(&(games_list[i])));
    display.setCursor(10, 8 * i);
    display.println(buffer);
  }

  // Game selection arrow
  display.drawLine(0, 3 + (8 * game_index), 7, 3 + (8 * game_index), SSD1306_WHITE);
  display.drawLine(5, 1 + (8 * game_index), 7, 3 + (8 * game_index), SSD1306_WHITE);
  display.drawLine(5, 5 + (8 * game_index), 7, 3 + (8 * game_index), SSD1306_WHITE);

  if (popup_menu) {
    utils.draw_popup_menu("Menu", popup_menu_list);
  }
}