#include "./src/Class/LuisCalculator.hpp"
#include "./src/Class/LuisCpu.hpp"
#include "./src/Class/GuilhermeDisplay.hpp"
#include "./src/Class/GuilhermeKeyControl.hpp"
#include "./src/Class/GuilhermeKeyDigit.hpp"
#include "./src/Class/LuisKeyOperation.hpp"
#include "./src/Class/LuisKeyboard.hpp"

GuilhermeKeyDigit* generateNumbers(Keyboard* keyboard){
  GuilhermeKeyDigit* digits = (GuilhermeKeyDigit*) malloc(sizeof(GuilhermeKeyDigit)*10);

  digits[0] = ZERO;
  digits[1] = ONE;
  digits[2] = TWO;
  digits[3] = THREE;
  digits[4] = FOUR;
  digits[5] = FIVE;
  digits[6] = SIX;
  digits[7] = SEVEN;
  digits[8] = EIGHT;
  digits[9] = NINE;

  for (int i = 0; i < 10; i++){
    digits[i].setReceiver(keyboard);
    keyboard->addKey(&digits[i]);
  }

  return digits;
}
LuisKeyOperation* generateOperations(Keyboard* keyboard){
  LuisKeyOperation* operations = (LuisKeyOperation*) malloc(sizeof(LuisKeyOperation)*10);

  operations[0] = ADDITION;
  operations[1] = SUBTRACTION;
  operations[2] = DIVISION;
  operations[3] = MULTIPLICATION;
  operations[4] = SQUARE_ROOT;
  operations[5] = PERCENTAGE;
  
  for (int i = 0; i < 5; i++){
    operations[i].setReceiver(keyboard);
    keyboard->addKey(&operations[i]);
  }

  return operations;
}
GuilhermeKeyControl* generateControls(Keyboard* keyboard){
  GuilhermeKeyControl* controls = (GuilhermeKeyControl*) malloc(sizeof(GuilhermeKeyControl)*10);

  controls[0] = CLEAR;
  controls[1] = RESET;
  controls[2] = DECIMAL_SEPARATOR;
  controls[3] = MEMORY_READ_CLEAR;
  controls[4] = MEMORY_ADDITION;
  controls[5] = MEMORY_SUBTRACTION;
  controls[6] = EQUAL;

  for (int i = 0; i < 6; i++){
    controls[i].setReceiver(keyboard);
    keyboard->addKey(&controls[i]);
  }

  return controls;
}

LuisCalculator* generateLuisCalculator(){
  GuilhermeDisplay* display = new GuilhermeDisplay();
  LuisKeyboard* keyboard = new LuisKeyboard();
  LuisCpu* cpu = new LuisCpu();
  LuisCalculator* calculadora = new LuisCalculator();
  keyboard->setCpu(cpu);
  cpu->setDisplay(display);
  calculadora->setCpu(cpu);
  calculadora->setDisplay(display);
  calculadora->setKeyboard(keyboard);

  // keyboard [0-9]
  GuilhermeKeyDigit* numbers = generateNumbers(keyboard);
  // keyboard [10-14]
  LuisKeyOperation* operations = generateOperations(keyboard);
  // keyboard [15-21]
  GuilhermeKeyControl* controls = generateControls(keyboard);

  return calculadora;
}

// enum Digit {ZERO, ONE, TWO, THRE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE};
// enum Operation {ADDITION, SUBTRACTION, DIVISION, MULTIPLICATION, SQUARE_ROOT, PERCENTAGE};
// enum Control {CLEAR, RESET, DECIMAL_SEPARATOR, MEMORY_READ_CLEAR, MEMORY_ADDITION, MEMORY_SUBTRACTION, EQUAL};
// enum Signal {POSITIVE, NEGATIVE};
int main(){
  LuisCalculator* calculadora = generateLuisCalculator();
  //12,54
  calculadora->receiveDigit(ONE);
  calculadora->receiveDigit(TWO);
  
  // +
  calculadora->receiveDigit(ADDITION);

  //13,5
  calculadora->receiveDigit(ONE);
  calculadora->receiveDigit(THREE);
  calculadora->receiveDigit(DECIMAL_SEPARATOR);
  calculadora->receiveDigit(FIVE);

  // = 25,5
  calculadora->receiveDigit(EQUAL);

}