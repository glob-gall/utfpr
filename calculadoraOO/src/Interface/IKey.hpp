#pragma once
#include "./IReceiver.hpp"

class Key{
   protected:
     Receiver* receiver;
   public:
      void setReceiver(Receiver* );

      virtual void press() = 0;
};