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

void Buttons::example() {
  b_state_up    = digitalRead(b_up);
  b_state_right = digitalRead(b_right);
  b_state_down  = digitalRead(b_down);
  b_state_left  = digitalRead(b_left);
  b_state_menu  = digitalRead(b_menu);
  b_state_R1    = digitalRead(b_R1);
  b_state_L1    = digitalRead(b_L1);
  b_state_a     = digitalRead(b_a);
  b_state_b     = digitalRead(b_b);
  b_state_x     = digitalRead(b_x);
  b_state_y     = digitalRead(b_y);

  if (b_state_right == HIGH || b_state_R1 == HIGH) {
    x += 1;
  } else if (b_state_up == HIGH) {
    y -= 1;
  } else if (b_state_down == HIGH) {
    y += 1;
  } else if (b_state_left == HIGH || b_state_L1 == HIGH) {
    x -= 1;
  }

  if (b_state_y == HIGH) {
    top += 1;
  } else if (b_state_b == HIGH) {
    right += 1;
  } else if (b_state_a == HIGH) {
    down += 1;
  } else if (b_state_x == HIGH) {
    left += 1;
  }

  if (b_state_menu == HIGH) {
    speaker.action_sound();
    x = 10;
    y = 10;
    w = 10;
    h = 10;
    top   = 0;
    right = 0;
    down  = 0;
    left  = 0;
  }

  display.drawRect(x - left, y - top, w + left + right, h + top + down, SSD1306_WHITE);
  display.drawRect(x, y, w, h, SSD1306_WHITE);
  display.drawLine(x        , y        , x - left                       , y - top                     , SSD1306_WHITE);
  display.drawLine(x + w - 1, y        , x - left + w + left + right - 1, y - top                     , SSD1306_WHITE);
  display.drawLine(x + w - 1, y + h - 1, x - left + w + left + right - 1, y - top + h + top + down - 1, SSD1306_WHITE);
  display.drawLine(x        , y + h - 1, x - left                       , y - top + h + top + down - 1, SSD1306_WHITE);
  display.drawRect(0, 0, 128, 64, SSD1306_WHITE);
}