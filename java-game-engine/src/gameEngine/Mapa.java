package gameEngine;

public class Mapa {
    public char[][] mapa;

    public Mapa(String mapaStr){
        String aux;
        char[] aux2;

        char[][] mapa = new char[Constants.PIXELS_HEIGHT][Constants.PIXELS_WIDTH];

        for (int i = 0; i < 40; i++) {
            aux = mapaStr.substring(i*126, (i*126)+126);
            aux2 = aux.toCharArray();
            for (int j = 0; j < Constants.PIXELS_WIDTH; j++) {
                mapa[i][j] = aux2[j];
            }
        }
        this.mapa = mapa;
    }
}
