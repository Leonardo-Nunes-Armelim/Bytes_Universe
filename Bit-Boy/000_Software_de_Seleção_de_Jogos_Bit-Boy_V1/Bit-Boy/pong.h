#ifndef PONG_H
#define PONG_H

#include <Arduino.h>

class Pong
{
  private:
    int8_t new_random_number();
    void restart_game();

    bool game_menu = false;

    uint8_t ball_angle = 1;
    uint8_t ball_x = 2;
    uint8_t ball_y = 7;
    bool ball_direction_x = true;
    bool ball_direction_y = false;
    int8_t player_y = 0;
    int8_t oponent_y = 0;
    int8_t player_score = 0;
    int8_t oponent_score = 0;


  public:
    void game();
};

extern Pong pong;

#endif