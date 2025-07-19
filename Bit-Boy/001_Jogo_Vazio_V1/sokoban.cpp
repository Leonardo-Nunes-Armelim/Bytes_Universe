#include "sokoban.h"
#include "buttons.h"
#include "display.h"
#include "speaker.h"
#include "sounds.h"
#include "utils.h"

Sokoban sokoban;

const char *sokoban_menu_list[] = {"Restart"};

// 0 tree
// 1 wall
// 2 flor
// 3 target
// 4 box
// 5 box on target
// 6 agent
// 7 agent on target

const uint8_t level_1[9][9] PROGMEM = {
  {0, 0, 1, 1, 1, 0, 0, 0, 0},
  {0, 0, 1, 3, 1, 0, 0, 0, 0},
  {0, 0, 1, 2, 1, 1, 1, 1, 0},
  {1, 1, 1, 4, 2, 4, 3, 1, 0},
  {1, 3, 2, 4, 6, 1, 1, 1, 0},
  {1, 1, 1, 1, 4, 1, 0, 0, 0},
  {0, 0, 0, 1, 3, 1, 0, 0, 0},
  {0, 0, 0, 1, 1, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_2[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 0, 0, 0, 0},
  {1, 2, 2, 2, 1, 0, 0, 0, 0},
  {1, 2, 4, 6, 1, 0, 1, 1, 1},
  {1, 2, 4, 4, 1, 0, 1, 3, 1},
  {1, 1, 1, 2, 1, 1, 1, 3, 1},
  {0, 1, 1, 2, 2, 2, 2, 3, 1},
  {0, 1, 2, 2, 2, 1, 2, 2, 1},
  {0, 1, 2, 2, 2, 1, 1, 1, 1},
  {0, 1, 1, 1, 1, 1, 0, 0, 0}
};

const uint8_t level_3[9][9] PROGMEM = {
  {0, 1, 1, 1, 1, 0, 0, 0, 0},
  {1, 1, 2, 2, 1, 0, 0, 0, 0},
  {1, 2, 6, 4, 1, 0, 0, 0, 0},
  {1, 1, 4, 2, 1, 1, 0, 0, 0},
  {1, 1, 2, 4, 2, 1, 0, 0, 0},
  {1, 3, 4, 2, 2, 1, 0, 0, 0},
  {1, 3, 3, 5, 3, 1, 0, 0, 0},
  {1, 1, 1, 1, 1, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_4[9][9] PROGMEM = {
  {0, 1, 1, 1, 1, 0, 0, 0, 0},
  {0, 1, 6, 2, 1, 1, 1, 0, 0},
  {0, 1, 2, 4, 2, 2, 1, 0, 0},
  {1, 1, 1, 2, 1, 2, 1, 1, 0},
  {1, 3, 1, 2, 1, 2, 2, 1, 0},
  {1, 3, 4, 2, 2, 1, 2, 1, 0},
  {1, 3, 2, 2, 2, 4, 2, 1, 0},
  {1, 1, 1, 1, 1, 1, 1, 1, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_5[9][9] PROGMEM = {
  {0, 0, 1, 1, 1, 1, 1, 1, 0},
  {0, 0, 1, 2, 2, 2, 2, 1, 0},
  {1, 1, 1, 4, 4, 4, 2, 1, 0},
  {1, 6, 2, 4, 3, 3, 2, 1, 0},
  {1, 2, 4, 3, 3, 3, 1, 1, 0},
  {1, 1, 1, 1, 2, 2, 1, 0, 0},
  {0, 0, 0, 1, 1, 1, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_6[9][9] PROGMEM = {
  {0, 0, 1, 1, 1, 1, 1, 0, 0},
  {1, 1, 1, 2, 2, 6, 1, 0, 0},
  {1, 2, 2, 4, 3, 2, 1, 1, 0},
  {1, 2, 2, 3, 4, 3, 2, 1, 0},
  {1, 1, 1, 2, 5, 4, 2, 1, 0},
  {0, 0, 1, 2, 2, 2, 1, 1, 0},
  {0, 0, 1, 1, 1, 1, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_7[9][9] PROGMEM = {
  {0, 0, 1, 1, 1, 1, 0, 0, 0},
  {0, 0, 1, 3, 3, 1, 0, 0, 0},
  {0, 1, 1, 2, 3, 1, 1, 0, 0},
  {0, 1, 2, 2, 4, 3, 1, 0, 0},
  {1, 1, 2, 4, 2, 2, 1, 1, 0},
  {1, 2, 2, 1, 4, 4, 2, 1, 0},
  {1, 2, 2, 6, 2, 2, 2, 1, 0},
  {1, 1, 1, 1, 1, 1, 1, 1, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_8[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 1, 1, 1, 0},
  {1, 2, 2, 1, 2, 2, 2, 1, 0},
  {1, 6, 4, 3, 3, 4, 2, 1, 0},
  {1, 2, 4, 3, 5, 2, 1, 1, 0},
  {1, 2, 4, 3, 3, 4, 2, 1, 0},
  {1, 2, 2, 1, 2, 2, 2, 1, 0},
  {1, 1, 1, 1, 1, 1, 1, 1, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_9[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 1, 0, 0, 0},
  {1, 2, 2, 2, 2, 1, 0, 0, 0},
  {1, 2, 4, 4, 4, 1, 1, 0, 0},
  {1, 2, 2, 1, 3, 3, 1, 1, 1},
  {1, 1, 2, 2, 3, 3, 4, 2, 1},
  {0, 1, 2, 6, 2, 2, 2, 2, 1},
  {0, 1, 1, 1, 1, 1, 1, 1, 1},
  {0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_10[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 1, 1, 0, 0},
  {1, 3, 3, 4, 3, 3, 1, 0, 0},
  {1, 3, 3, 1, 3, 3, 1, 0, 0},
  {1, 2, 4, 4, 4, 2, 1, 0, 0},
  {1, 2, 2, 4, 2, 2, 1, 0, 0},
  {1, 2, 4, 4, 4, 2, 1, 0, 0},
  {1, 2, 2, 1, 6, 2, 1, 0, 0},
  {1, 1, 1, 1, 1, 1, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_11[9][9] PROGMEM = {
  {0, 1, 1, 1, 1, 1, 0, 0, 0},
  {0, 1, 2, 6, 2, 1, 1, 1, 0},
  {1, 1, 2, 1, 4, 2, 2, 1, 0},
  {1, 2, 5, 3, 2, 3, 2, 1, 0},
  {1, 2, 2, 4, 4, 2, 1, 1, 0},
  {1, 1, 1, 2, 1, 3, 1, 0, 0},
  {0, 0, 1, 2, 2, 2, 1, 0, 0},
  {0, 0, 1, 1, 1, 1, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_12[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 1, 0, 0, 0},
  {1, 2, 2, 2, 2, 1, 0, 0, 0},
  {1, 2, 4, 2, 6, 1, 0, 0, 0},
  {1, 1, 5, 2, 2, 1, 0, 0, 0},
  {1, 2, 5, 2, 1, 1, 0, 0, 0},
  {1, 2, 5, 2, 1, 0, 0, 0, 0},
  {1, 2, 5, 2, 1, 0, 0, 0, 0},
  {1, 2, 3, 2, 1, 0, 0, 0, 0},
  {1, 1, 1, 1, 1, 0, 0, 0, 0}
};

const uint8_t level_13[9][9] PROGMEM = {
  {0, 0, 1, 1, 1, 1, 0, 0, 0},
  {0, 0, 1, 2, 2, 1, 0, 0, 0},
  {1, 1, 1, 4, 2, 1, 1, 0, 0},
  {1, 2, 2, 5, 2, 6, 1, 0, 0},
  {1, 2, 2, 5, 2, 2, 1, 0, 0},
  {1, 2, 2, 5, 2, 1, 1, 0, 0},
  {1, 1, 1, 5, 2, 1, 0, 0, 0},
  {0, 0, 1, 3, 1, 1, 0, 0, 0},
  {0, 0, 1, 1, 1, 0, 0, 0, 0}
};

const uint8_t level_14[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 0, 0, 0, 0},
  {1, 2, 2, 2, 1, 1, 1, 1, 1},
  {1, 2, 1, 2, 1, 2, 2, 2, 1},
  {1, 2, 4, 2, 2, 2, 4, 2, 1},
  {1, 3, 3, 1, 4, 1, 4, 1, 1},
  {1, 3, 6, 4, 2, 2, 2, 1, 0},
  {1, 3, 3, 2, 2, 1, 1, 1, 0},
  {1, 1, 1, 1, 1, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_15[9][9] PROGMEM = {
  {0, 1, 1, 1, 1, 1, 1, 0, 0},
  {0, 1, 2, 2, 2, 2, 1, 1, 0},
  {1, 1, 3, 1, 1, 4, 2, 1, 0},
  {1, 2, 3, 3, 4, 2, 2, 1, 0},
  {1, 2, 2, 1, 4, 2, 2, 1, 0},
  {1, 2, 2, 6, 2, 1, 1, 1, 0},
  {1, 1, 1, 1, 1, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0}
};

const uint8_t level_16[9][9] PROGMEM = {
  {1, 1, 1, 1, 1, 1, 1, 1, 1},
  {1, 3, 2, 2, 3, 2, 2, 3, 1},
  {1, 2, 2, 2, 2, 2, 2, 2, 1},
  {1, 2, 2, 4, 4, 4, 2, 2, 1},
  {1, 3, 2, 4, 6, 4, 2, 3, 1},
  {1, 2, 2, 4, 4, 4, 2, 2, 1},
  {1, 2, 2, 2, 2, 2, 2, 2, 1},
  {1, 3, 2, 2, 3, 2, 2, 3, 1},
  {1, 1, 1, 1, 1, 1, 1, 1, 1}
};

void Sokoban::load_level(const uint8_t source[9][9]) {
  for (uint8_t y = 0; y < 9; y++) {
    for (uint8_t x = 0; x < 9; x++) {
      current_level[y][x] = pgm_read_byte(&(source[y][x]));
    }
  }
}

void Sokoban::update_map(uint8_t agent_x, uint8_t agent_y, int8_t x, int8_t y) {
  display.clearDisplay();
  if (current_level[agent_y+y][agent_x+x] == 1) { // Crashing into the wall
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 4) { // Stuck box on other box
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 5) { // Stuck box on other box
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 4) { // Stuck box on other box
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 5) { // Stuck box on other box
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 1) { // Stuck box on wall
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 1) { // Stuck box on wall
    speaker.play_note(NOTE_CS3, 200);
  } else if (current_level[agent_y][agent_x] == 6 && current_level[agent_y+y][agent_x+x] == 2) { // Walking in open space
    current_level[agent_y+y][agent_x+x] = 6;
    current_level[agent_y][agent_x] = 2;
    draw_map();
    display.display();
    speaker.play_note(NOTE_D4, 200);
  } else if (current_level[agent_y][agent_x] == 6 && current_level[agent_y+y][agent_x+x] == 3) { // Walking to a taget
    current_level[agent_y+y][agent_x+x] = 7;
    current_level[agent_y][agent_x] = 2;
    draw_map();
    display.display();
    speaker.play_note(NOTE_D4, 200);
  } else if (current_level[agent_y][agent_x] == 7 && current_level[agent_y+y][agent_x+x] == 2) { // Walking outside target to open sapace
    current_level[agent_y+y][agent_x+x] = 6;
    current_level[agent_y][agent_x] = 3;
    draw_map();
    display.display();
    speaker.play_note(NOTE_D4, 200);
  } else if (current_level[agent_y][agent_x] == 7 && current_level[agent_y+y][agent_x+x] == 3) { // Walking outside target to a target
    current_level[agent_y+y][agent_x+x] = 7;
    current_level[agent_y][agent_x] = 3;
    draw_map();
    display.display();
    speaker.play_note(NOTE_D4, 200);
  } else if (current_level[agent_y][agent_x] == 6 && current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 2) { // Pushing box
    current_level[agent_y+y+y][agent_x+x+x] = 4;
    current_level[agent_y+y][agent_x+x] = 6;
    current_level[agent_y][agent_x] = 2;
    draw_map();
    display.display();
    speaker.play_note(NOTE_G4, 200);
  } else if (current_level[agent_y][agent_x] == 7 && current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 2) { // Pushing box (Agent on target)
    current_level[agent_y+y+y][agent_x+x+x] = 4;
    current_level[agent_y+y][agent_x+x] = 6;
    current_level[agent_y][agent_x] = 3;
    draw_map();
    display.display();
    speaker.play_note(NOTE_G4, 200);
  } else if (current_level[agent_y][agent_x] == 6 && current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 2) { // Pushing box (Box on target)
    current_level[agent_y+y+y][agent_x+x+x] = 4;
    current_level[agent_y+y][agent_x+x] = 7;
    current_level[agent_y][agent_x] = 2;
    draw_map();
    display.display();
    speaker.play_note(NOTE_G5, 100);
    speaker.play_note(NOTE_E5, 100);
  } else if (current_level[agent_y][agent_x] == 7 && current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 2) { // Pushing box (Agent on target && Box on target)
    current_level[agent_y+y+y][agent_x+x+x] = 4;
    current_level[agent_y+y][agent_x+x] = 7;
    current_level[agent_y][agent_x] = 3;
    draw_map();
    display.display();
    speaker.play_note(NOTE_G5, 100);
    speaker.play_note(NOTE_E5, 100);
  } else if (current_level[agent_y][agent_x] == 6 && current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 3) { // Pushing box to target
    current_level[agent_y+y+y][agent_x+x+x] = 5;
    current_level[agent_y+y][agent_x+x] = 6;
    current_level[agent_y][agent_x] = 2;
    draw_map();
    display.display();
    speaker.play_note(NOTE_E5, 100);
    speaker.play_note(NOTE_G5, 100);
  } else if (current_level[agent_y][agent_x] == 7 && current_level[agent_y+y][agent_x+x] == 4 && current_level[agent_y+y+y][agent_x+x+x] == 3) { // Pushing box to target (Agent on target)
    current_level[agent_y+y+y][agent_x+x+x] = 5;
    current_level[agent_y+y][agent_x+x] = 6;
    current_level[agent_y][agent_x] = 3;
    draw_map();
    display.display();
    speaker.play_note(NOTE_E5, 100);
    speaker.play_note(NOTE_G5, 100);
  } else if (current_level[agent_y][agent_x] == 6 && current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 3) { // Pushing box to target (Agent on target)
    current_level[agent_y+y+y][agent_x+x+x] = 5;
    current_level[agent_y+y][agent_x+x] = 7;
    current_level[agent_y][agent_x] = 2;
    draw_map();
    display.display();
    speaker.play_note(NOTE_E5, 100);
    speaker.play_note(NOTE_G5, 100);
  } else if (current_level[agent_y][agent_x] == 7 && current_level[agent_y+y][agent_x+x] == 5 && current_level[agent_y+y+y][agent_x+x+x] == 3) { // Pushing box to target (Agent on target)
    current_level[agent_y+y+y][agent_x+x+x] = 5;
    current_level[agent_y+y][agent_x+x] = 7;
    current_level[agent_y][agent_x] = 3;
    draw_map();
    display.display();
    speaker.play_note(NOTE_E5, 100);
    speaker.play_note(NOTE_G5, 100);
  }
}

void Sokoban::move_agent(uint8_t direction) {
  uint8_t agent_x = 0;
  uint8_t agent_y = 0;
  for (uint8_t y = 0; y < 9; y++) {
    for (uint8_t x = 0; x < 9; x++) {
      if (current_level[y][x] == 6 || current_level[y][x] == 7) {
        agent_x = x;
        agent_y = y;
      }
    }
  }

  if (direction == 1) {                   // Up
    update_map(agent_x, agent_y, 0, -1);
  } else if (direction == 2) {            // Right
    update_map(agent_x, agent_y, 1, 0);
  } else if (direction == 3) {            // Down
    update_map(agent_x, agent_y, 0, 1);
  } else if (direction == 4) {            // Left
    update_map(agent_x, agent_y, -1, 0);
  }
}

const uint8_t (*Sokoban::get_level(uint8_t level))[9] {
  switch (level) {
    case 1:  return level_1;
    case 2:  return level_2;
    case 3:  return level_3;
    case 4:  return level_4;
    case 5:  return level_5;
    case 6:  return level_6;
    case 7:  return level_7;
    case 8:  return level_8;
    case 9:  return level_9;
    case 10: return level_10;
    case 11: return level_11;
    case 12: return level_12;
    case 13: return level_13;
    case 14: return level_14;
    case 15: return level_15;
    case 16: return level_16;
    default: return nullptr;
  }
}

void Sokoban::draw_tree(uint8_t x, uint8_t y) {
  display.drawLine((x*7)+32+3, (y*7)+1, (x*7)+32+1, (y*7)+3, SSD1306_WHITE);
  display.drawLine((x*7)+32+3, (y*7)+1, (x*7)+32+5, (y*7)+3, SSD1306_WHITE);
  display.drawLine((x*7)+32+1, (y*7)+4, (x*7)+32+5, (y*7)+4, SSD1306_WHITE);
  display.drawPixel((x*7)+32+3, (y*7)+5, SSD1306_WHITE);
}

void Sokoban::draw_wall(uint8_t x, uint8_t y) {
  bool pixel = false;
  for (uint8_t yy = 0; yy < 7; yy++) {
    for (uint8_t xx = 0; xx < 7; xx++) {
      if (pixel == true) {
        display.drawPixel((x*7)+32+xx, (y*7)+yy, SSD1306_WHITE);
        pixel = false;
      } else {
        pixel = true;
      }
    }
  }
}

void Sokoban::draw_target(uint8_t x, uint8_t y) {
  display.drawCircle((x*7)+32+3, (y*7)+3, 2, SSD1306_WHITE);
}

void Sokoban::draw_box(uint8_t x, uint8_t y) {
  display.drawRect((x*7)+32, y*7, 7, 7, SSD1306_WHITE);
  display.drawLine((x*7)+32, (y*7), (x*7)+32+6, (y*7)+6, SSD1306_WHITE);
  display.drawLine((x*7)+32+6, (y*7), (x*7)+32, (y*7)+6, SSD1306_WHITE);
}

void Sokoban::draw_box_on_target(uint8_t x, uint8_t y) {
  display.fillRect((x*7)+32, y*7, 7, 7, SSD1306_WHITE);
  display.drawLine((x*7)+32, (y*7), (x*7)+32+6, (y*7)+6, SSD1306_BLACK);
  display.drawLine((x*7)+32+6, (y*7), (x*7)+32, (y*7)+6, SSD1306_BLACK);
}

void Sokoban::draw_agent(uint8_t x, uint8_t y) {
  display.fillCircle((x*7)+32+3, (y*7)+3, 2, SSD1306_WHITE);
  display.drawPixel((x*7)+32+2, (y*7)+2, SSD1306_BLACK);
  display.drawPixel((x*7)+32+4, (y*7)+2, SSD1306_BLACK);
  display.drawPixel((x*7)+32+2, (y*7)+4, SSD1306_BLACK);
  display.drawPixel((x*7)+32+3, (y*7)+4, SSD1306_BLACK);
  display.drawPixel((x*7)+32+4, (y*7)+4, SSD1306_BLACK);
}

void Sokoban::is_level_completed() {
  int8_t box_count = 0;
  for (uint8_t y = 0; y < 9; y++) {
    for (uint8_t x = 0; x < 9; x++) {
      if (current_level[y][x] == 4) {
        box_count += 1;
      }
    }
  }

  if (box_count == 0) {
    level += 1;
    load = true;
    delay(500);
  }
}

void Sokoban::draw_map() {
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(F("Level"));
  display.println(level);

  for (uint8_t y = 0; y < 9; y++) {
    for (uint8_t x = 0; x < 9; x++) {
      if (current_level[y][x] == 0) {
        draw_tree(x, y);
      } else if (current_level[y][x] == 1) {
        draw_wall(x, y);
      } else if (current_level[y][x] == 3) {
        draw_target(x, y);
      } else if (current_level[y][x] == 4) {
        draw_box(x, y);
      } else if (current_level[y][x] == 5) {
        draw_box_on_target(x, y);
      } else if (current_level[y][x] == 6) {
        draw_agent(x, y);
      } else if (current_level[y][x] == 7) {
        draw_agent(x, y);
      }
    }
  }
}

void Sokoban::game() {
  buttons.b_state_up    = digitalRead(buttons.b_up);
  buttons.b_state_right = digitalRead(buttons.b_right);
  buttons.b_state_down  = digitalRead(buttons.b_down);
  buttons.b_state_left  = digitalRead(buttons.b_left);
  buttons.b_state_menu  = digitalRead(buttons.b_menu);
  buttons.b_state_R1    = digitalRead(buttons.b_R1);
  buttons.b_state_L1    = digitalRead(buttons.b_L1);
  buttons.b_state_a     = digitalRead(buttons.b_a);

  if (buttons.b_state_R1 == HIGH) {
    level += 1;
    load = true;
    speaker.play_note(NOTE_C4, 200);
  } else if (buttons.b_state_L1 == HIGH) {
    level -= 1;
    load = true;
    speaker.play_note(NOTE_C4, 200);
  }
  if (level == 0) {
    level = 16;
  } else if (level == 17) {
    level = 1;
  }

  if (load) {
    load_level(get_level(level));
    load = false;
  }

  if (!game_menu) {
    if (buttons.b_state_up == HIGH) {
      move_agent(1);
    } else if (buttons.b_state_right == HIGH) {
      move_agent(2);
    } else if (buttons.b_state_down == HIGH) {
      move_agent(3);
    } else if (buttons.b_state_left == HIGH) {
      move_agent(4);
    }
  }

  is_level_completed();
  draw_map();

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
        load = true;
        utils.popup_menu_index = 0;
        game_menu = false;
        delay(200);
      }
    }
    utils.draw_popup_menu("Menu", sokoban_menu_list);
  }
}