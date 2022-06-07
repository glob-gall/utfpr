#pragma once
#include "./enums.hpp"
#include "./IKey.hpp"

class KeyControl: public Key{
     Control control;
   public:
      KeyControl(Control );
      void press();
};