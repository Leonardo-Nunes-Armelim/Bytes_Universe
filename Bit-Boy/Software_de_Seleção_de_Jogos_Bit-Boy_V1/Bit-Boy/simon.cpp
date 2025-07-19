#include "simon.h"
#include "buttons.h"
#include "display.h"
#include "speaker.h"
#include "sounds.h"
#include "menu.h"
#include "utils.h"

Simon simon;

const char *simon_menu_list[] = {"Restart",
                                 "Change game"};

int8_t Simon::new_random_number() {
  randomSeed(analogRead(A0));
  return random(0, 4);
}

void Simon::draw_buttons(int8_t *numb) {
  // Laterais dos botoes
  display.drawRect(32,  0, 30, 30, SSD1306_WHITE);
  display.drawRect(66,  0, 30, 30, SSD1306_WHITE);
  display.drawRect(32, 34, 30, 30, SSD1306_WHITE);
  display.drawRect(66, 34, 30, 30, SSD1306_WHITE);

  if (numb == 0) {
    display.fillRect(32,  0, 30, 30, SSD1306_WHITE);
  } else if (numb == 1) {
    display.fillRect(66,  0, 30, 30, SSD1306_WHITE);
  } else if (numb == 2) {
    display.fillRect(32, 34, 30, 30, SSD1306_WHITE);
  } else if (numb == 3) {
    display.fillRect(66, 34, 30, 30, SSD1306_WHITE);
  }

  // Apagando quadrados
  for (int8_t i = 0; i < 20; i++) {
    display.drawCircle(63, 31, 30 + i, SSD1306_BLACK);
    display.drawCircle(64, 31, 30 + i, SSD1306_BLACK);
    display.drawCircle(64, 32, 30 + i, SSD1306_BLACK);
    display.drawCircle(64, 32, 30 + i, SSD1306_BLACK);
  }

  // Anel de fora
  display.drawCircle(63, 31, 30, SSD1306_WHITE);
  display.drawCircle(64, 31, 30, SSD1306_WHITE);
  display.drawCircle(64, 32, 30, SSD1306_WHITE);
  display.drawCircle(64, 32, 30, SSD1306_WHITE);

  // Anel de dentro
  display.drawCircle(63, 31, 20, SSD1306_WHITE);
  display.drawCircle(64, 31, 20, SSD1306_WHITE);
  display.drawCircle(64, 32, 20, SSD1306_WHITE);
  display.drawCircle(64, 32, 20, SSD1306_WHITE);
  display.drawCircle(63, 31, 21, SSD1306_WHITE);
  display.drawCircle(64, 31, 21, SSD1306_WHITE);
  display.drawCircle(64, 32, 21, SSD1306_WHITE);
  display.drawCircle(64, 32, 21, SSD1306_WHITE);

  // Separação dos botoes
  display.fillRect(62, 0, 4, 64, SSD1306_BLACK);
  display.fillRect(0, 30, 128, 4, SSD1306_BLACK);

  // Centro
  display.fillCircle(63, 31, 19, SSD1306_BLACK);
  display.fillCircle(64, 31, 19, SSD1306_BLACK);
  display.fillCircle(63, 32, 19, SSD1306_BLACK);
  display.fillCircle(64, 32, 19, SSD1306_BLACK);
  display.fillCircle(63, 31, 16, SSD1306_WHITE);
  display.fillCircle(64, 31, 16, SSD1306_WHITE);
  display.fillCircle(63, 32, 16, SSD1306_WHITE);
  display.fillCircle(64, 32, 16, SSD1306_WHITE);

  if (!game_over) {
    display.setTextSize(1);
    display.setTextColor(SSD1306_BLACK);
    display.setCursor(49, 29);
    display.println(F("Simon"));
  } else {
    display.setTextSize(1);
    display.setTextColor(SSD1306_BLACK);
    display.setCursor(52, 25);
    display.println(F("GAME"));
    display.setCursor(52, 33);
    display.println(F("OVER"));
  }
}

bool Simon::check_sequence() {
  if (sequence[player_sequence_step] == player_choice) {
      player_sequence_step += 1;
    if (player_sequence_step == sequence_step) {
      player_sequence_step = 0;
      in_play = true;
      delay(350);
    }
    return true;
  }
  return false;
}

void Simon::button_click(int8_t *choice) {
  display.clearDisplay();
  draw_buttons(choice);
  display.display();
}

void Simon::restart_game() {
  in_play = true;
  game_over = false;
  sequence_step = 0;
  player_sequence_step = 0;
  player_choice = 0;
  game_menu = false;
}

void Simon::game() {
  buttons.b_state_up   = digitalRead(buttons.b_up);
  buttons.b_state_down = digitalRead(buttons.b_down);
  buttons.b_state_menu = digitalRead(buttons.b_menu);
  buttons.b_state_a    = digitalRead(buttons.b_a);
  buttons.b_state_y    = digitalRead(buttons.b_y);

  if (!game_over) {
    if (in_play) {
      sequence[sequence_step] = new_random_number();
      for (int8_t i = 0; i < sequence_step + 1; i++) {
        button_click(sequence[i]);
        if (sequence[i] == 0) {
        speaker.play_note(NOTE_E4, 200);
        } else if (sequence[i] == 1) {
          display.fillRect(66,  0, 30, 30, SSD1306_WHITE);
          speaker.play_note(NOTE_C4, 200);
        } else if (sequence[i] == 2) {
          display.fillRect(32, 34, 30, 30, SSD1306_WHITE);
          speaker.play_note(NOTE_G4, 200);
        } else if (sequence[i] == 3) {
          speaker.play_note(NOTE_D4, 200);
        }
        button_click(4);
        delay(100);
      }
      in_play = false;
      sequence_step += 1;
    } else {
      if (!game_menu) {
        if (buttons.b_state_up == HIGH) {
          player_choice = 0;
          button_click(player_choice);
          speaker.play_note(NOTE_E4, 200);
          if (!check_sequence()) {
            game_over = true;
          }
        } else if (buttons.b_state_y == HIGH) {
          player_choice = 1;
          button_click(player_choice);
          speaker.play_note(NOTE_C4, 200);
          if (!check_sequence()) {
            game_over = true;
          }
        } else if (buttons.b_state_down == HIGH) {
          player_choice = 2;
          button_click(player_choice);
          speaker.play_note(NOTE_G4, 200);
          if (!check_sequence()) {
            game_over = true;
          }
        } else if (buttons.b_state_a == HIGH) {
          player_choice = 3;
          button_click(player_choice);
          speaker.play_note(NOTE_D4, 200);
          if (!check_sequence()) {
            game_over = true;
          }
        }
      }
    }

    if (game_over) {
      button_click(player_choice);
      speaker.play_note(NOTE_E4, 100);
      speaker.play_note(NOTE_D4, 100);
      speaker.play_note(NOTE_C4, 100);
    }

  }

  draw_buttons(4);

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
      } else if (utils.popup_menu_index == 1) {
        restart_game();
        menu.in_game = false;
        utils.popup_menu_index = 0;
        game_menu = false;
      }
      delay(200);
    }
    utils.draw_popup_menu("Menu", simon_menu_list);
  }
}