#ifndef SOKOBAN_H
#define SOKOBAN_H

#include <Arduino.h>

class Sokoban
{
  private:
    void load_level(const uint8_t source[9][9]);
    void update_map(uint8_t agent_x, uint8_t agent_y, int8_t x, int8_t y);
    void move_agent(uint8_t direction);
    void is_level_completed();

    const uint8_t (*get_level(uint8_t level))[9];

    void draw_tree(uint8_t x, uint8_t y);
    void draw_wall(uint8_t x, uint8_t y);
    void draw_target(uint8_t x, uint8_t y);
    void draw_box(uint8_t x, uint8_t y);
    void draw_box_on_target(uint8_t x, uint8_t y);
    void draw_agent(uint8_t x, uint8_t y);
    void draw_map();

    uint8_t level = 1;
    bool load = true;
    uint8_t current_level[9][9];
    bool game_menu = false;

  public:
    void game();
};

extern Sokoban sokoban;

#endif