#ifndef BUTTONS_H
#define BUTTONS_H

#include <Arduino.h>

class Buttons
{
  public:
    void init();

    const int8_t b_menu  = 2;
    const int8_t b_R1    = 12;
    const int8_t b_L1    = 6;
    const int8_t b_up    = 5;
    const int8_t b_right = 3;
    const int8_t b_down  = 4;
    const int8_t b_left  = 7;
    const int8_t b_a     = 10;
    const int8_t b_b     = 11;
    const int8_t b_x     = 8;
    const int8_t b_y     = 9;

    bool b_state_menu  = false;
    bool b_state_R1    = false;
    bool b_state_L1    = false;
    bool b_state_up    = false;
    bool b_state_right = false;
    bool b_state_down  = false;
    bool b_state_left  = false;
    bool b_state_y     = false;
    bool b_state_b     = false;
    bool b_state_a     = false;
    bool b_state_x     = false;
};

extern Buttons buttons;

#endif