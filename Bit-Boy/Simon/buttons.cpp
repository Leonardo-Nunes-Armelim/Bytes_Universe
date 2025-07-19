#include "buttons.h"
#include "display.h"
#include "speaker.h"

Buttons buttons;

void Buttons::init() {
  pinMode(b_menu , INPUT);
  pinMode(b_R1   , INPUT);
  pinMode(b_L1   , INPUT);
  pinMode(b_up   , INPUT);
  pinMode(b_right, INPUT);
  pinMode(b_down , INPUT);
  pinMode(b_left , INPUT);
  pinMode(b_a    , INPUT);
  pinMode(b_b    , INPUT);
  pinMode(b_x    , INPUT);
  pinMode(b_y    , INPUT);
}