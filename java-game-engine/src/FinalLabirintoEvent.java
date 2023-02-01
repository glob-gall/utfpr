import gameEngine.Constants;
import gameEngine.Event;

 public class FinalLabirintoEvent extends Event {
     private int currentMap = 1;
    public void exec(){
        if(this.gm == null)
            return;


        Mapa1 mp1 = new Mapa1();
        Mapa2 mp2 = new Mapa2();

        if (gm.getMapa() == null){
            this.gm.setMapa(mp1.mapa);
        }else if(this.currentMap == 2){
            this.gm.setMapa(mp2.mapa);
        }


        if (gm.rects[0].x == 122 && gm.rects[0].y == 37){
            if(currentMap == 2){
                System.out.println("VOCE GANHOU");
            }else if(currentMap == 1){
                currentMap=2;
                gm.rects[0].x = 1;
                gm.rects[0].y = 37;
            }
        }else{
            System.out.println("x:"+gm.rects[0].x+"y:"+gm.rects[0].y);
        }
    }
}
