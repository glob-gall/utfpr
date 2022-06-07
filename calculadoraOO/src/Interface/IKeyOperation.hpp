#pragma once
#include "./enums.hpp"
#include "./IKey.hpp"

class KeyOperation: public Key{
     Operation operation;
   public:
      KeyOperation(Operation );
      void press();
};