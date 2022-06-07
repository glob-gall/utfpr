#pragma once
#include "../Interface/IKeyboard.hpp"
#include <vector>

class LuisKeyboard: public Keyboard{
   Cpu* cpu;
   std::vector< Key* > keys;
   public:
      void addKey(Key* );
      void receiveDigit(Digit );
      void receiveOperation(Operation );
      void receiveControl(Control );
};