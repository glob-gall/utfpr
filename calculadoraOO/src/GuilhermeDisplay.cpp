#include "./Class/GuilhermeDisplay.hpp"

void GuilhermeDisplay::clearScreen(){
  cout << "\033[2J\033[1;1H";
};

char showOperator(Operation op){
  switch (op){
  case ADDITION: return '+';
  case SUBTRACTION: return '-';
  case DIVISION: return '/';
  case MULTIPLICATION: return '*';
  case SQUARE_ROOT: return '^';
  case PERCENTAGE: return '%';
  default: return ' ';
  }
}

void GuilhermeDisplay::show(){
  this->clearScreen();
  for (int i = 0; i < 8; i++){
    cout << this->memory[i];
  }
  cout << showOperator(this->operation);
  for (int i = 0; i < 8; i++){
    cout << this->memory2[i];
  }
};

void GuilhermeDisplay::add(Digit digit){
  this->memory[this->memoryPosition] = digit;
  this->memoryPosition = this->memoryPosition+1;
  // this->clearScreen();
  this->show();
};

void GuilhermeDisplay::setDecimalSeparator(){
  this->separatorPosition = this->memoryPosition;
  // this->clearScreen();
  this->show();
};

void GuilhermeDisplay::setSignal(Signal signal){
  this->signal = signal;
  // this->clearScreen();
  this->show();
};

void GuilhermeDisplay::setError(){
  this->memoryPosition=0;
  this->hasOperation=false;
  this->hasSignal=false;
  // this->clearScreen();
  cout << "ERROR!";
};

void GuilhermeDisplay::clear(){
  this->memoryPosition=0;
  this->hasOperation=false;
  this->hasSignal=false;
  // this->clearScreen();
};
