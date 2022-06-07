#pragma once
#include "./ICpu.hpp"
#include "./IReceiver.hpp"
#include "IKey.hpp"

class Key; // Preset for early reference

class Keyboard: public Receiver{
   Cpu* cpu;
   public:
      void setCpu(Cpu* );

      virtual void addKey(Key* ) = 0;
      virtual void receiveDigit(Digit ) = 0;
      virtual void receiveOperation(Operation ) = 0;
      virtual void receiveControl(Control ) = 0;
};