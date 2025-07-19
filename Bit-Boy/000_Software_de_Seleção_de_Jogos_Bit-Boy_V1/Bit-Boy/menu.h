#ifndef MENU_H
#define MENU_H

#include <Arduino.h>

class Menu
{
  private:
   bool popup_menu = false;
  public:
    void game_selection();
    //void options();
    //void play();

    int8_t game_index = 0;
    bool in_game = false;
    char buffer[20];
};

extern Menu menu;

#endif