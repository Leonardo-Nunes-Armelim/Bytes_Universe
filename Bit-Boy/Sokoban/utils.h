#ifndef UTILS_H
#define UTILS_H

#include <Arduino.h>

#define EEPROM_ADDR_BEEP 0

class Utils
{
  private:
    int8_t count_characters(const char *texto);
  public:
    void update_eeprom_beep(bool estado);
    bool read_eeprom_beep();
    void draw_popup_menu(const char *menu_title, const char *options_list[]);
    
    int8_t popup_menu_index = 0;
};

extern Utils utils;

#endif