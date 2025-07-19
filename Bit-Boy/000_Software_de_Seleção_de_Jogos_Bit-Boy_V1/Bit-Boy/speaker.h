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
    void star_wars_cantina_song();
    void play_song(const uint16_t* song, size_t length);
};

extern Speaker speaker;

#endif