#pragma once
#include "../Interface/ICalculator.hpp"

class LuisCalculator: public Calculator{
  Cpu* cpu;
  Display* display;
  Keyboard* keyboard;

    void pressNumber(int i);
    void pressControl(int i);
    void pressOperation(int i);
  public:
    void setDisplay(Display* );
    void setCpu(Cpu* );
    void setKeyboard(Keyboard* );

    void receiveDigit(Digit);
    void receiveDigit(Operation);
    void receiveDigit(Control);
};