#pragma once
#include "./enums.hpp"
#include "./IKey.hpp"

class KeyDigit: public Key{
     Digit digit;
   public:
      KeyDigit(Digit );
      void press();
};