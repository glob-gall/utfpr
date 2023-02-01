package gameEngine;

public class Collision {
    Pixels pixels;

    Collision(Pixels pixels){
        this.pixels = pixels;
    }

    public boolean canMoveUp(Shape rect){
        if (rect.y <= 0) return false;

        for (int i = rect.x; i < rect.x+rect.width; i++) {
            if (this.pixels.matrix[rect.y-1][i] != Constants.BG_CHAR){
                return false;
            }
        }
        return true;
    }

    public boolean canMoveDown(Shape rect){
        if (rect.y+rect.height >= this.pixels.height) return false;


        for (int i = rect.x; i < rect.x+rect.width; i++) {
            if (this.pixels.matrix[rect.y+rect.height][i] != Constants.BG_CHAR){
                return false;
            }
        }
        return true;
    }

    public boolean canMoveRight(Shape rect){
        if (rect.x+rect.width >= this.pixels.width) return false;

        for (int i = rect.y; i < rect.y+rect.height; i++) {
            if (this.pixels.matrix[i][rect.x+rect.width] != Constants.BG_CHAR){
                return false;
            }
        }
        return true;
    }
    public boolean canMoveLeft(Shape rect){
        if (rect.x <= 0) return false;

        for (int i = rect.y; i < rect.y+rect.height; i++) {
            if (this.pixels.matrix[i][rect.x-1] != Constants.BG_CHAR){
                return false;
            }
        }
        return true;
    }


}