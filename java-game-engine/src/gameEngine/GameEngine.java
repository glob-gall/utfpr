package gameEngine;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.swing.*;
import java.io.File;

public class GameEngine extends JFrame implements Runnable {
    public KL keyListener = new KL();
    public Draw drawModule;
    public Control[] controllers;
    public Shape[] rects;
    public Pixels pixels = new Pixels();
    public int width,height;

    private char[][] mapa;
    private Event[] events;


    public GameEngine(Control[] controllers,Shape[] rects, Event[] events){

        this.width = Constants.SCREEN_WIDTH;
        this.height = Constants.SCREEN_HEIGHT;

        this.controllers = controllers;
        for (int i = 0; i < controllers.length; i++){
            controllers[i].addEventListener(this.keyListener);
            if (controllers[i].hasCollision){
                controllers[i].setCollision(new Collision(this.pixels));
            }
        }

        Event[] auxEvents = events;
        for (int i = 0; i < events.length; i++) {
            auxEvents[i].setGm(this);
        }
        this.events = auxEvents;

        this.rects = rects;

        this.setSize(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT);
        this.setTitle(Constants.SCREEN_TITLE);
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.addKeyListener(this.keyListener);

        this.drawModule = new Draw(this);
        this.setVisible(true);


    }

    private void update(double dt){
        if(this.mapa != null){
            drawModule.clearPixels(this.pixels,mapa);
        }else{
            drawModule.clearPixels(this.pixels);
        }


        for (int i = 0; i < this.rects.length; i++) {
            if (this.rects[i] instanceof Rect) {
                drawModule.drawRect(this.pixels, (Rect) this.rects[i]);
            }
            if (this.rects[i] instanceof Triangle) {
                drawModule.drawTriangle(this.pixels, (Triangle) this.rects[i]);
            }
            if (this.rects[i] instanceof Circle) {
                drawModule.drawCircle(this.pixels, (Circle) this.rects[i]);
            }
        }
        drawModule.drawPixels(this.pixels);

        for (int i = 0; i < controllers.length; i++)
            controllers[i].update(dt);

        for (int i = 0; i < this.events.length; i++) {
            this.events[i].exec();
        }
    }

    public void run() {
        double lastFrameTime = 0.0;
        while(true){
            double time = Time.getTime();
            double deltaTime = time - lastFrameTime;
            lastFrameTime = time;
            update(deltaTime);

            try {
                Thread.sleep(30);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

    public void setMapa(char[][] mapa) {
        this.mapa = mapa;
    }

    public char[][] getMapa() {
        return mapa;
    }
}