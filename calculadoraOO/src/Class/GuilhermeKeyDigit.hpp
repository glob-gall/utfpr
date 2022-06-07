#pragma once
#include "../Interface/IKeyDigit.hpp"


class GuilhermeKeyDigit: public KeyDigit{
     Digit digit;
   public:
      GuilhermeKeyDigit(Digit );
      GuilhermeKeyDigit();
      void setReceiver(Receiver* );
};