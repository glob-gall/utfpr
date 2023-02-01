package gameEngine;

public class Triangle extends Shape{
    public char texture;

    public Triangle(int x, int y, int height, char texture){
        this.x = x;
        this.y = y;
        this.height = height;
        this.texture = texture;
        this.width = height + (height-1) ;
    }

}
