from entradasSaidas import tokens, numeros, letras, outros, saidas

class Automato:
    transition: str = ''
    currentStates: set = {'q0'}
    nextStates: set = set()
    curentToken: str = ''

    def goto(self,to):
        self.nextStates.add(to)

    def q0(self):
        # if self.transition in outros:
        #     return
        self.goto('wordState')
        self.goto('numberState')
        self.goto('tokenState')

    def numberState(self):
        if self.transition in numeros:
            self.goto('numberStateLoop')
        elif self.transition in letras:
            self.goto('notNumberLoop')
        else:
            self.goto('numberState')
    
    def notNumberLoop(self):
        if (
            self.transition in numeros
            or self.transition in letras
        ):
            self.goto('notNumberLoop')
        else:
            self.goto('numberState')

    def numberStateValid(self):
        print('NUMBER')
        if self.transition in numeros:
            self.goto('numberStateLoop')
        else:
            self.goto('numberState')
    
    def tokenState(self):
        if self.transition == "<":
            self.goto('lessState')
            self.curentToken = self.transition
        elif self.transition == ">":
            self.goto('greaterState')
            self.curentToken = self.transition
        elif self.transition == "=":
            self.goto('equalsState')
            self.curentToken = self.transition
        elif self.transition == "!":
            self.goto('differentState')
            self.curentToken = self.transition
        elif self.transition in tokens:
            self.goto('tokenStateValid')
            self.curentToken = self.transition
        else:
            self.goto('tokenState')

    def tokenStateValid(self):
        print(saidas[tokens.index(self.curentToken)])
        
        if self.transition in tokens:
            self.goto('tokenStateValid')
            self.curentToken = self.transition
        else:
            self.goto('tokenState')


    def wordStateLoop(self):
        if self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')

    def numberStateLoop(self):
        if self.transition in numeros or self.transition == '.':
            self.goto('numberStateLoop')
        else:
            self.goto('numberStateValid')

    def wordState(self):
            if(self.transition == 'i'):
                self.goto('ifIntState1')
            elif(self.transition == 'e'):
                self.goto('elseState1')
            elif(self.transition == 'r'):
                self.goto('returnState1')
            elif(self.transition == 'v'):
                self.goto('voidState1')
            elif(self.transition == 'w'):
                self.goto('whileState1')
            elif(self.transition == 'f'):
                self.goto('floatForState1')
            elif(self.transition  in letras):
                self.goto('wordStateLoop')
            else:
                self.goto('wordState')

    def ifIntState1(self):
        if self.transition == 'f':
            self.goto('ifStateFinal')
        elif self.transition == 'n':
            self.goto('intState2')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def intState2(self):
        if self.transition == 't':
            self.goto('intStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')

    def elseState1(self):
        if self.transition == 'l':
            self.goto('elseState2')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def elseState2(self):
        if self.transition == 's':
            self.goto('elseState3')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def elseState3(self):
        if self.transition == 'e':
            self.goto('elseStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')

    def returnState1(self):
        if self.transition == 'e':
            self.goto('returnState2')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def returnState2(self):
        if self.transition == 't':
            self.goto('returnState3')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def returnState3(self):
        if self.transition == 'u':
            self.goto('returnState4')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def returnState4(self):
        if self.transition == 'r':
            self.goto('returnState5')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def returnState5(self):
        if self.transition == 'n':
            self.goto('returnStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')

    def voidState1(self):
        if self.transition == 'o':
            self.goto('voidState2')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def voidState2(self):
        if self.transition == 'i':
            self.goto('voidState3')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def voidState3(self):
        if self.transition == 'd':
            self.goto('voidStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')

    def whileState1(self):
        if self.transition == 'h':
            self.goto('whileState2')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def whileState2(self):
        if self.transition == 'i':
            self.goto('whileState3')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def whileState3(self):
        if self.transition == 'l':
            self.goto('whileState4')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def whileState4(self):
        if self.transition == 'e':
            self.goto('whileStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def floatForState1(self):
        if self.transition == 'l':
            self.goto('floatState2')
        elif self.transition == 'o':
            self.goto('forState2')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def floatState2(self):
        if self.transition == 'o':
            self.goto('floatState3')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def floatState3(self):
        if self.transition == 'a':
            self.goto('floatState4')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def floatState4(self):
        if self.transition == 't':
            self.goto('floatStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    def forState2(self):
        if self.transition == 'r':
            self.goto('forStateFinal')
        elif self.transition in letras or self.transition in numeros:
            self.goto('wordStateLoop')
        else:
            self.goto('wordStateValid')
    

    def wordStateValid(self):
        print('ID')
        if(self.transition == 'i'):
            self.goto('ifIntState1')
        elif(self.transition == 'e'):
            self.goto('elseState1')
        elif(self.transition == 'r'):
            self.goto('returnState1')
        elif(self.transition == 'v'):
            self.goto('voidState1')
        elif(self.transition == 'w'):
            self.goto('whileState1')
        elif(self.transition == 'f'):
            self.goto('floatForState1')
        elif self.transition in letras:
            self.goto('wordStateLoop')
        else: 
            self.goto('wordState')

    def ifStateFinal(self):
        print('IF')
        self.goto('wordState')
    def elseStateFinal(self):
        print('ELSE')
        self.goto('wordState')
    def intStateFinal(self):
        print('INT')
        self.goto('wordState')
    def returnStateFinal(self):
        print('RETURN')
        self.goto('wordState')
    def voidStateFinal(self):
        print('VOID')
        self.goto('wordState')
    def whileStateFinal(self):
        print('WHILE')
        self.goto('wordState')
    def floatStateFinal(self):
        print('FLOAT')
        self.goto('wordState')
    def forStateFinal(self):
        print('FOR')
        self.goto('wordState')

    def lessState(self):
        if self.transition == '=':
            self.goto('lessEqualState')
        else:
            self.goto('tokenStateValid')
    def lessEqualState(self):
        print("LESS_EQUALS")
        self.curentToken=''
        self.goto('tokenState')

    def greaterState(self):
        if self.transition == '=':
            self.goto('greaterEqualState')
        else:
            self.goto('tokenStateValid')
    def greaterEqualState(self):
        print("GREATER_EQUALS")
        self.curentToken=''
        self.goto('tokenState')

    def equalsState(self):
        if self.transition == '=':
            self.goto('equalsEqualState')
        else:
            self.goto('tokenStateValid')
    def equalsEqualState(self):
        print("EQUALS")
        self.curentToken=''
        self.goto('tokenState')

    def differentState(self):
        if self.transition == '=':
            self.goto('differentdifferentState')
        else:
            self.goto('tokenState')
    def differentdifferentState(self):
        print("DIFFERENT")
        self.curentToken=''
        self.goto('tokenState')

    def execActiveNodes(self):
        if 'numberState' in self.currentStates:
            self.numberState()
        if 'wordState' in self.currentStates:
            self.wordState()
        if 'tokenState' in self.currentStates:
            self.tokenState()
        if 'wordStateValid' in self.currentStates:
            self.wordStateValid()
        if 'wordStateLoop' in self.currentStates:
            self.wordStateLoop()
        if 'numberStateValid' in self.currentStates:
            self.numberStateValid()
        if 'notNumberLoop' in self.currentStates:
            self.notNumberLoop()
        if 'numberStateLoop' in self.currentStates:
            self.numberStateLoop()
        if 'tokenStateValid' in self.currentStates:
            self.tokenStateValid()
        if 'ifIntState1' in self.currentStates:
            self.ifIntState1()
        if 'intState2' in self.currentStates:
            self.intState2()
        if 'elseState1' in self.currentStates:
            self.elseState1()
        if 'elseState2' in self.currentStates:
            self.elseState2()
        if 'elseState3' in self.currentStates:
            self.elseState3()
        if 'returnState1' in self.currentStates:
            self.returnState1()
        if 'returnState2' in self.currentStates:
            self.returnState2()
        if 'returnState3' in self.currentStates:
            self.returnState3()
        if 'returnState4' in self.currentStates:
            self.returnState4()
        if 'returnState5' in self.currentStates:
            self.returnState5()
        if 'voidState1' in self.currentStates:
            self.voidState1()
        if 'voidState2' in self.currentStates:
            self.voidState2()
        if 'voidState3' in self.currentStates:
            self.voidState3()
        if 'whileState1' in self.currentStates:
            self.whileState1()
        if 'whileState2' in self.currentStates:
            self.whileState2()
        if 'whileState3' in self.currentStates:
            self.whileState3()
        if 'whileState4' in self.currentStates:
            self.whileState4()
        if 'ifStateFinal' in self.currentStates:
            self.ifStateFinal()
        if 'intStateFinal' in self.currentStates:
            self.intStateFinal()
        if 'elseStateFinal' in self.currentStates:
            self.elseStateFinal()
        if 'voidStateFinal' in self.currentStates:
            self.voidStateFinal()
        if 'returnStateFinal' in self.currentStates:
            self.returnStateFinal()
        if 'whileStateFinal' in self.currentStates:
            self.whileStateFinal()
        if 'floatStateFinal' in self.currentStates:
            self.floatStateFinal()
        if 'forStateFinal' in self.currentStates:
            self.forStateFinal()
        if 'lessState' in self.currentStates:
            self.lessState()
        if 'lessEqualState' in self.currentStates:
            self.lessEqualState()
        if 'greaterState' in self.currentStates:
            self.greaterState()
        if 'greaterEqualState' in self.currentStates:
            self.greaterEqualState()
        if 'equalsState' in self.currentStates:
            self.equalsState()
        if 'equalsEqualState' in self.currentStates:
            self.equalsEqualState()
        if 'differentState' in self.currentStates:
            self.differentState()
        if 'differentdifferentState' in self.currentStates:
            self.differentdifferentState()
        if 'floatForState1' in self.currentStates:
            self.floatForState1()
        if 'floatState2' in self.currentStates:
            self.floatState2()
        if 'floatState3' in self.currentStates:
            self.floatState3()
        if 'floatState4' in self.currentStates:
            self.floatState4()
        if 'forState2' in self.currentStates:
            self.forState2()
        
        # if 'q0' in self.currentStates:
        #     self.q0()

    def run(self,code:str):
        self.currentStates= {'tokenState', 'numberState', 'wordState'}
        self.transition =''

        for c in code:
            self.transition = c
            # print(self.currentStates)
            # print(self.transition)
            self.execActiveNodes()
            
            self.transition=''
            self.currentStates = self.nextStates.copy()
            self.nextStates.clear()
        self.execActiveNodes()


def main():
    automato = Automato()

    # text_file1 = open("./testes/teste-001.cm", "r")
    # data1 = text_file1.read()
    # print("\n\nteste-001.cm")
    # automato.run(data1)
    # text_file1.close()


    # text_file2 = open("./testes/teste-002.cm", "r")
    # data2 = text_file2.read()
    # print("\n\nteste-002.cm")
    # automato.run(data2)
    # text_file2.close()


    # text_file3 = open("./testes/teste-003.cm", "r")
    # data3 = text_file3.read()
    # print("\n\nteste-003.cm")
    # automato.run(data3)
    # text_file3.close()


    text_file4 = open("./testes/teste-004.cm", "r")
    data4 = text_file4.read()
    print("\n\nteste-004.cm")
    automato.run(data4)
    text_file4.close()


    # text_file5 = open("./testes/teste-005.cm", "r")
    # data5 = text_file5.read()
    # print("\n\nteste-005.cm")
    # automato.run(data5)
    # text_file5.close()

main()
        
