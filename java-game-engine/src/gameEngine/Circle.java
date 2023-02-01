package gameEngine;

public class Circle extends Shape{
    public int rad;
    public int xCenter;
    public int yCenter;
    public char texture;

    public Circle(int x, int y, int rad, char texture){
        this.x = x;
        this.y = y;
        this.rad = rad;
        this.texture = texture;

        this.width = (2*rad)+1;
        this.height = (2*rad)+1;
    }

}
