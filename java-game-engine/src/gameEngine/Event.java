package gameEngine;

public abstract class Event {
    public GameEngine gm;
    public abstract void exec();

    public void setGm(GameEngine gm) {
        this.gm = gm;
    }
}
