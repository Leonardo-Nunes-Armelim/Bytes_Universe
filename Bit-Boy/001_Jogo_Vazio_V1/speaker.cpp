#include "speaker.h"
#include "sounds.h"

Speaker speaker;

void Speaker::init() {
  pinMode(speaker, OUTPUT);
  action_sound();
}

void Speaker::action_sound() {
  tone(speaker, NOTE_C4,  100);
  delay(100);
  tone(speaker, NOTE_D4,  100);
  delay(100);
  tone(speaker, NOTE_E4,  100);
  delay(100);
}

void Speaker::play_note(int note, int time) {
  tone(speaker, note,  time);
  delay(time);
}