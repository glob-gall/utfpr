#include "./Class/GuilhermeKeyDigit.hpp"


GuilhermeKeyDigit::KeyDigit::KeyDigit(Digit digit){
  this->digit = digit;
}

void GuilhermeKeyDigit::setReceiver(Receiver* receiver){
  this->receiver = receiver;
}

GuilhermeKeyDigit::GuilhermeKeyDigit(Digit digit):KeyDigit(digit){
  this->digit = digit;
}

GuilhermeKeyDigit::GuilhermeKeyDigit():KeyDigit(ZERO){};

void GuilhermeKeyDigit::KeyDigit::press(){
  this->receiver ? this->receiver->receiveDigit(this->digit)
  : void();
}