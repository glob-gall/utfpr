#pragma once
#include "../Interface/IKeyControl.hpp"


class GuilhermeKeyControl: public KeyControl{
     Control control;
   public:
      GuilhermeKeyControl(Control);
      void setReceiver(Receiver* );
};