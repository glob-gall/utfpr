import gameEngine.*;

import java.awt.event.KeyEvent;

public class Main {
    public static void main(String[] args){

        Rect objeto1 = new Rect(1,37,3,3,'@');
        Control controlRect1 = new  Control(objeto1, KeyEvent.VK_DOWN,KeyEvent.VK_UP,KeyEvent.VK_RIGHT,KeyEvent.VK_LEFT,true);
//
//        Triangle objeto3 = new Triangle(20, 30, 4, '&');
//        Control controlTriangle = new Control(objeto3, KeyEvent.VK_S,KeyEvent.VK_W,KeyEvent.VK_D,KeyEvent.VK_A,true);
//
//        Circle objeto5 = new Circle(6, 17, 4, '@');
//        Control controlCircle5 = new  Control(objeto5, KeyEvent.VK_K,KeyEvent.VK_I,KeyEvent.VK_L,KeyEvent.VK_J,true);

        Shape[] rects = new Shape[1];
        rects[0] = objeto1;
//        rects[1] = objeto3;
//        rects[2] = objeto5;

        Control[] controllers = new Control[1];
        controllers[0] = controlRect1;
//        controllers[1] = controlTriangle;
//        controllers[2] = controlCircle5;

        FinalLabirintoEvent finalEvent = new FinalLabirintoEvent();

        Event[] events = new Event[1];
        events[0] = finalEvent;


        GameEngine gm = new GameEngine(controllers,rects,events);


        Thread t1 = new Thread(gm);
        t1.start();
    }
}