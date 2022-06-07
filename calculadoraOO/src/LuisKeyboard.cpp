#include "./Class/LuisKeyboard.hpp"

void LuisKeyboard::Keyboard::setCpu(Cpu* cpu){
  this->cpu = cpu;
}

void LuisKeyboard::addKey(Key* key){
  this->keys.push_back(key);
}

void LuisKeyboard::receiveDigit(Digit digit){
  this->cpu ? this->cpu->receiveDigit(digit) : void();
}

void LuisKeyboard::receiveOperation(Operation operation){
  this->cpu ? this->cpu->receiveOperation(operation) : void();
}

void LuisKeyboard::receiveControl(Control control){
  this->cpu ? this->cpu->receiveControl(control) : void();
}
