#include "./Class/LuisCalculator.hpp"

void LuisCalculator::setCpu(Cpu* cpu){
  this->cpu = cpu;
}

void LuisCalculator::setDisplay(Display* display){
  this->display = display;
}

void LuisCalculator::setKeyboard(Keyboard* keyboard){
  this->keyboard = keyboard;
}

void LuisCalculator::receiveDigit(Digit digit){
  this->cpu->receiveDigit(digit);

};
void LuisCalculator::receiveDigit(Operation operation){
  this->cpu->receiveOperation(operation);
};
void LuisCalculator::receiveDigit(Control control){
  this->cpu->receiveControl(control);
};