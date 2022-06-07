#include "./Class/GuilhermeKeyControl.hpp"


GuilhermeKeyControl::KeyControl::KeyControl(Control control){
  this->control = control;
}
GuilhermeKeyControl::GuilhermeKeyControl(Control control):KeyControl(control){
  this->control = control;
}

void GuilhermeKeyControl::setReceiver(Receiver* receiver){
  this->receiver = receiver;
}


void GuilhermeKeyControl::KeyControl::press(){
  this->receiver ? this->receiver->receiveControl(this->control)
  : void();
}
