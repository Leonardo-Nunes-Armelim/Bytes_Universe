#include "pong.h"
#include "buttons.h"
#include "display.h"
#include "speaker.h"
#include "sounds.h"
#include "utils.h"

Pong pong;

const char *pong_menu_list[] = {"Restart"};

int8_t Pong::new_random_number() {
  randomSeed(analogRead(A0));
  return random(1, 3);
}

void Pong::restart_game() {
  ball_angle = 1;
  ball_x = 2;
  ball_y = 7;
  ball_direction_x = true;
  ball_direction_y = false;
  player_y = 0;
  oponent_y = 0;
  player_score = 0;
  oponent_score = 0;
}

void Pong::game() {
  buttons.b_state_up   = digitalRead(buttons.b_up);
  buttons.b_state_down = digitalRead(buttons.b_down);
  buttons.b_state_menu = digitalRead(buttons.b_menu);
  buttons.b_state_a    = digitalRead(buttons.b_a);

  if (buttons.b_state_up == HIGH) {
    player_y -= 1;
  } else if (buttons.b_state_down == HIGH) {
    player_y += 1;
  }
  if (player_y < 0) {
    player_y = 0;
  } else if (player_y > 48) {
    player_y = 48;
  }

  if (ball_direction_x) {
    if (ball_direction_y) {
      ball_x += 1;
      ball_y -= ball_angle;
    } else {
      ball_x += 1;
      ball_y += ball_angle;
    }
  } else {
    if (ball_direction_y) {
      ball_x -= 1;
      ball_y -= ball_angle;
    } else {
      ball_x -= 1;
      ball_y += ball_angle;
    }
  }
  if (ball_y <= 0) {
    ball_direction_y = !ball_direction_y;
    speaker.play_note(NOTE_C4, 50);
  } else if (ball_y >= 63) {
    ball_direction_y = !ball_direction_y;
    speaker.play_note(NOTE_C4, 50);
  }
  if (ball_x == 1) {
    if (ball_y >= player_y && ball_y <= (player_y + 16)) {
      ball_direction_x = !ball_direction_x;
      ball_angle = new_random_number();
      speaker.play_note(NOTE_C5, 50);
    } else {
      ball_x = 124;
      ball_y = oponent_y + 8;
      oponent_score += 1;
    }
  } else if (ball_x == 125) {
    if (ball_y >= oponent_y && ball_y <= (oponent_y + 16)) {
      ball_direction_x = !ball_direction_x;
      ball_angle = new_random_number();
      speaker.play_note(NOTE_C5, 50);
    } else {
      ball_x = 2;
      ball_y = player_y + 8;
      player_score += 1;
    }
  }

  if (ball_y < oponent_y) {
    oponent_y -= 1;
  } else if (ball_y > (oponent_y + 16)) {
    oponent_y += 1;
  }

  display.drawRect(0, player_y, 2, 16, SSD1306_WHITE);
  display.drawRect(126, oponent_y, 2, 16, SSD1306_WHITE);
  display.drawRect(ball_x, ball_y, 2, 2, SSD1306_WHITE);
  display.drawRect(64, 0, 1, 64, SSD1306_WHITE);

  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(32, 0);
  display.println(player_score);
  display.setCursor(96, 0);
  display.println(oponent_score);

  // Menu Button
  if (buttons.b_state_menu == HIGH) {
    if (!game_menu) {
      game_menu = true;
    } else {
      game_menu = false;
      utils.popup_menu_index = 0;
    }
    delay(200);
  }

  // Game Menu
  if (game_menu) {
    if (buttons.b_state_up == HIGH) {
      if (utils.popup_menu_index > 0) {
        utils.popup_menu_index -= 1;
      }
    } else if (buttons.b_state_down == HIGH) {
      if (utils.popup_menu_index < 1) {
        utils.popup_menu_index += 1;
      }
    } else if (buttons.b_state_a == HIGH) {
      if (utils.popup_menu_index == 0) {
        restart_game();
        utils.popup_menu_index = 0;
        game_menu = false;
        delay(200);
      }
    }
    utils.draw_popup_menu("Menu", pong_menu_list);
  }
}