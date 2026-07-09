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

const uint16_t star_wars_cantina[] PROGMEM = {
  NOTE_A4,  125, 125,
  NOTE_D5,  125, 125,
  NOTE_A4,  125, 125,
  NOTE_D5,  125, 63,
  NOTE_A4,  100, 0,
  NOTE_D5,  125, 63,
  NOTE_A4,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_A4,  125, 0,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 0,
  NOTE_G4,  125, 125,
  NOTE_FS4, 125, 0,
  NOTE_G4,  125, 0,
  NOTE_FS4, 125, 0,
  NOTE_F4,  375, 0,
  NOTE_D4,  375, 125,
  // 0:08 -----------------------------------------------------------
  NOTE_A4,  125, 125,
  NOTE_D5,  125, 125,
  NOTE_A4,  125, 125,
  NOTE_D5,  125, 63,
  NOTE_A4,  100, 0,
  NOTE_D5,  125, 63,
  NOTE_A4,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_G4,  125, 125,
  NOTE_G4,  375, 0,
  NOTE_FS4, 125, 0,
  NOTE_G4,  125, 125,
  NOTE_C5,  125, 0,
  NOTE_AS4, 125, 125,
  NOTE_A4,  125, 125,
  NOTE_G4,  125, 200,
  // 0:13 -----------------------------------------------------------
  NOTE_A4,  125, 125,
  NOTE_D5,  125, 125,
  NOTE_A4,  125, 125,
  NOTE_D5,  125, 63,
  NOTE_A4,  100, 0,
  NOTE_D5,  125, 63,
  NOTE_A4,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_C5,  125, 125,
  NOTE_C5,  375, 0,
  NOTE_A4,  125, 10,
  NOTE_G4,  125, 125,
  NOTE_F4,  375, 0,
  NOTE_D4,  300, 250,
  NOTE_D4,  500, 0,
  NOTE_F4,  500, 0,
  NOTE_A4,  500, 0,
  NOTE_C5,  500, 0,
  NOTE_DS5, 125, 125,
  NOTE_D5,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_F4,  125, 1063,
  // 0:21 -----------------------------------------------------------
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_A4, 125, 500,
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_A4, 125, 500,
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_GS4, 63, 0,
  NOTE_A4, 125, 125,
  NOTE_F4, 500, 0,
  NOTE_D4, 500, 250,
  // 0:27 -----------------------------------------------------------
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_A4, 125, 500,
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_A4, 125, 500,
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_GS4, 63, 0,
  NOTE_A4, 125, 125,
  NOTE_G4, 500, 0,
  NOTE_C4, 500, 125,
  // 0:32 -----------------------------------------------------------
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_A4, 125, 500,
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_A4, 125, 500,
  NOTE_A4, 125, 125,
  NOTE_F4, 100, 0,
  NOTE_GS4, 63, 0,
  NOTE_A4, 125, 125,
  NOTE_F4, 500, 0,
  NOTE_D4, 313, 250,
  // 0:37 -----------------------------------------------------------
  NOTE_AS3, 125, 0,
  NOTE_D4,  125, 0,
  NOTE_F4,  125, 125,
  NOTE_B3,  125, 0,
  NOTE_D4,  125, 0,
  NOTE_F4,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_D4,  250, 125,
  NOTE_D4,  125, 10,
  NOTE_F4,  125, 10,
  NOTE_AS4, 125, 10,
  NOTE_D5,  125, 10,
  NOTE_GS4, 125, 10,
  NOTE_A4,  125, 125,
  NOTE_F4,  375, 375,
  // 0:41 -----------------------------------------------------------
  NOTE_AS3, 125, 0,
  NOTE_D4,  125, 0,
  NOTE_F4,  125, 125,
  NOTE_B3,  125, 0,
  NOTE_D4,  125, 0,
  NOTE_F4,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_D5,  250, 125,
  NOTE_DS5, 125, 125,
  NOTE_D5,  125, 125,
  NOTE_GS4, 125, 0,
  NOTE_A4,  125, 125,
  NOTE_F4,  125, 0,
};

void Speaker::star_wars_cantina_song() {
  play_song(star_wars_cantina, sizeof(star_wars_cantina)/sizeof(uint16_t));
}

void Speaker::play_song(const uint16_t* song, size_t length) {
  for (size_t i = 0; i < length; i += 3) {
    uint16_t note   = pgm_read_word(&song[i]);
    uint16_t time   = pgm_read_word(&song[i + 1]);
    uint16_t pause  = pgm_read_word(&song[i + 2]);
    tone(speaker, note, time);
    delay(time + pause);
  }
}