#ifndef SPEAKER_H
#define SPEAKER_H

#include <Arduino.h>

class Speaker
{
  private:
    const int8_t speaker = 13;
  public:

    void init();
    void action_sound();
    void play_note(int note, int time);
};

extern Speaker speaker;

#endif