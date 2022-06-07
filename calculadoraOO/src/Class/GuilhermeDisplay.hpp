#pragma once
#include "../Interface/IDisplay.hpp"
#include<iostream>
using namespace std;
class GuilhermeDisplay: public Display{
  Digit memory[8];
  Digit memory2[8];
  bool hasOperation;
  Operation operation;
  int memoryPosition;

  int separatorPosition;
  
  bool hasSignal;
  Signal signal;
    void clearScreen();
  public:
    void show();
    void add(Digit );
    void setDecimalSeparator();
    void setSignal(Signal );
    void setError();
    void clear();
};