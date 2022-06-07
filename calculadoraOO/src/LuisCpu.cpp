#include "./Class/LuisCpu.hpp"
#include<iostream>
LuisCpu::LuisCpu(){
  this->hasOperation=false;
}


bool LuisCpu::isInteger(double k){
  return std::floor(k) == k;
}

void LuisCpu::setDisplay(Display* display){
  this->display = display;
}

void LuisCpu::calculateCurrentOperation(){
  switch (this->currentOperation){
    case ADDITION:
      this->registors[0] = this->registors[0] + this->registors[1];
    break;
    case SUBTRACTION:
      this->registors[0] = this->registors[0] - this->registors[1];
    break;
    case DIVISION:
      this->registors[0] = this->registors[0] / this->registors[1];
    break;
    case MULTIPLICATION:
      this->registors[0] = this->registors[0] * this->registors[1];
    break;
    case SQUARE_ROOT:
      this->registors[this->currentRegistor] = this->registors[this->currentRegistor]*this->registors[this->currentRegistor];
    break;
    case PERCENTAGE:
      this->registors[0] = this->registors[0] / this->registors[1]; // AJUSTAR
    break;
  default:
    break;
  }
  this->registors[1]=0;
}

void LuisCpu::receiveDigit(Digit digit){
  int current = this->currentRegistor;
  this->registors[current] = this->registors[current]*10;
  this->registors[current] = this->registors[current]+ (double)digit;
  
  if (this->decimalSeparetor[current]){
    this->registors[current] = this->registors[current]/10;
    this->decimalSeparetor[current] = false;
  }
}

void LuisCpu::receiveOperation(Operation operation){
  if (this->hasOperation) calculateCurrentOperation();

  this->currentOperation = operation;
  this->hasOperation=true;
  this->currentRegistor=1;
}

void LuisCpu::receiveControl(Control control){
  double current = this->registors[this->currentRegistor];
  switch(control){
    case CLEAR:
      this->display->clear();
    break;
    case RESET:
      this->display->clear();
      this->hasOperation=false;
      this->currentRegistor=0;
      this->registors[0]=0;
      this->registors[1]=0;
    break;
    case DECIMAL_SEPARATOR:
      if (LuisCpu::isInteger(current)){
        this->decimalSeparetor[this->currentRegistor] = true;
      }
    break;
    case MEMORY_READ_CLEAR: this->memory = 0; break;
    case MEMORY_ADDITION:
      this->memory = this->memory + current; break;
    case MEMORY_SUBTRACTION:
      this->memory = this->memory - current; break;
    case EQUAL: this->calculateCurrentOperation();
    break;
    default:
    break;
  }
}
