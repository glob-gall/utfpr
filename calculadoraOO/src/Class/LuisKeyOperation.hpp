#pragma once
#include "../Interface/IKeyOperation.hpp"


class LuisKeyOperation: public KeyOperation{
    Operation operation;
   public:
      LuisKeyOperation(Operation );
      void setReceiver(Receiver* );
};