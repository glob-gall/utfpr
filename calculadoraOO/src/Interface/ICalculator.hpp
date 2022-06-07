#pragma once
#include "./IDisplay.hpp"
#include "./ICpu.hpp"
#include "./IKeyboard.hpp"

class Calculator{
  public:
    virtual void setDisplay(Display* ) = 0;
    virtual void setCpu(Cpu* ) = 0;
    virtual void setKeyboard(Keyboard* ) = 0;
};