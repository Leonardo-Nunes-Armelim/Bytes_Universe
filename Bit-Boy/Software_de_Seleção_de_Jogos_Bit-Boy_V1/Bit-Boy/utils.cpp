#include "utils.h"
#include "simon.h"
#include "buttons.h"
#include "display.h"
#include "speaker.h"
#include "sounds.h"

#include <EEPROM.h>

Utils utils;

void Utils::update_eeprom_beep(bool estado) {
  EEPROM.update(EEPROM_ADDR_BEEP, estado);
}

bool Utils::read_eeprom_beep() {
  return EEPROM.read(EEPROM_ADDR_BEEP);
}

void Utils::draw_popup_menu(const char *menu_title, const char *options_list[]) {
  // Menu box
  display.fillRect(14, 7, 100, 50, SSD1306_BLACK);
  display.drawRect(14, 7, 100, 50, SSD1306_WHITE);

  // Menu title
  int8_t menu_title_length = count_characters(menu_title);
  menu_title_length = (menu_title_length * 5) + (menu_title_length - 1);
  display.fillRect(64 - (menu_title_length / 2) - 2, 9, menu_title_length + 4, 11, SSD1306_WHITE);
  display.setTextSize(1);
  display.setTextColor(SSD1306_BLACK);
  display.setCursor(64 - (menu_title_length / 2), 11);
  display.println(menu_title);

  // Options
  char buffer[4];
  display.setTextColor(SSD1306_WHITE);
  for (int8_t i = 0; i < 2; ++i) {
    display.setCursor(27, 20 + (8 * i));
    display.println(options_list[i]);
    //strcpy_P(buffer, (PGM_P)pgm_read_word(&(options_list[i])));
    //display.println(buffer);
  }

  // Option selection arrow
  display.drawLine(17, 23 + (8 * popup_menu_index), 24, 23 + (8 * popup_menu_index), SSD1306_WHITE);
  display.drawLine(22, 21 + (8 * popup_menu_index), 24, 23 + (8 * popup_menu_index), SSD1306_WHITE);
  display.drawLine(22, 25 + (8 * popup_menu_index), 24, 23 + (8 * popup_menu_index), SSD1306_WHITE);

  // Tamanho de cada caracter
  //display.drawRect(10, 0, 5, 7, SSD1306_WHITE);
  //display.drawRect(16, 0, 5, 7, SSD1306_WHITE);
  //display.drawRect(10, 8, 5, 7, SSD1306_WHITE);
}

int8_t Utils::count_characters(const char *texto) {
    int count = 0;
    while (texto[count] != '\0') {
        count++;
    }
    return count;
}