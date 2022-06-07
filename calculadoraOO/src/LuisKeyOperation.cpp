#include "./Class/LuisKeyOperation.hpp"

LuisKeyOperation::KeyOperation::KeyOperation(Operation operation){
  this->operation = operation;
}

void LuisKeyOperation::setReceiver(Receiver* receiver){
  this->receiver = receiver;
}

LuisKeyOperation::LuisKeyOperation(Operation operation):KeyOperation(operation){
  this->operation = operation;
}

void LuisKeyOperation::KeyOperation::press(){
  this->receiver ? this->receiver->receiveOperation(this->operation)
  : void();
}