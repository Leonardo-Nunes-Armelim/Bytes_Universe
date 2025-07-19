#ifndef SIMON_H
#define SIMON_H

#include <Arduino.h>

#define MAX_SEQUENCE 32

class Simon
{
  private:
    int8_t new_random_number();
    void draw_buttons(int8_t *numb);
    bool check_sequence();
    void button_click(int8_t *choice);
    void restart_game();

    bool in_play = true;
    bool game_over = false;
    int8_t sequence[32];
    int8_t sequence_step = 0;
    int8_t player_sequence_step = 0;
    int8_t player_choice = 0;

    bool game_menu = false;

  public:
    void game();

    //bool menu = false;
    //int8_t sequence_length = 0;
    //int8_t player_sequence_length = 0;
};

extern Simon simon;

#endif