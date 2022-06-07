#pragma once
#include "../Interface/ICpu.hpp"
#include <cmath>

class LuisCpu: public Cpu{
  Display* display;
  double registors[2];
  bool decimalSeparetor[2];
  int currentRegistor;

  Operation currentOperation;
  bool hasOperation;
  double memory;

  void calculateCurrentOperation();
  void printAll();
  bool isInteger(double k);

  public:
    LuisCpu();
    void setDisplay(Display* );

    void receiveDigit(Digit );
    void receiveOperation(Operation );
    void receiveControl(Control );
}; 