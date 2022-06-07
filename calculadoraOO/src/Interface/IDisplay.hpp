#pragma once
#include "./enums.hpp"
class Display{
  public:
    virtual void add(Digit ) = 0;
    virtual void setDecimalSeparator() = 0;
    virtual void setSignal(Signal ) = 0;
    virtual void setError() = 0;
    virtual void clear() = 0;
};