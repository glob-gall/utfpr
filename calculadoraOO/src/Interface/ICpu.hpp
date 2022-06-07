#pragma once
#include "./enums.hpp"
#include "./IDisplay.hpp"
#include "./IReceiver.hpp"

class IDisplay;
class Cpu: public Receiver{

  public:
    Display* display;
    void setDisplay(Display* );

    virtual void receiveDigit(Digit ) = 0;
    virtual void receiveOperation(Operation ) = 0;
    virtual void receiveControl(Control ) = 0;
};