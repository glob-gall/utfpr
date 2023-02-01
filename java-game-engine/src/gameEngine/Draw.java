package gameEngine;

import javax.swing.*;
import java.awt.*;

public class Draw {
    private JTextArea asciiDisplay = new JTextArea();
    private int width, height;


    Draw(JFrame frame) {
        this.width = Constants.PIXELS_WIDTH;
        this.height = Constants.PIXELS_HEIGHT;

        this.asciiDisplay.setFont(new java.awt.Font(Constants.fontName, Font.BOLD, 10));
        frame.add(asciiDisplay);
        asciiDisplay.addKeyListener(frame.getKeyListeners()[0]);
    }

    public void drawPixels(Pixels pixels) {
        StringBuilder txt = new StringBuilder();

        for (int i = 0; i < this.height; i++) {
            for (int j = 0; j < this.width; j++) {
                txt.append(pixels.matrix[i][j]);
            }
            txt.append('\n');
        }

        this.asciiDisplay.setText(txt.toString());
    }

    public void clearPixels(Pixels pixels) {
        for (int i = 0; i < this.height; i++)
            for (int j = 0; j < this.width; j++)
                pixels.matrix[i][j] = Constants.BG_CHAR;

    }
    public void clearPixels(Pixels pixels, char[][] mapa) {
        for (int i = 0; i < this.height; i++)
            for (int j = 0; j < this.width; j++)
                pixels.matrix[i][j] = mapa[i][j];

    }

    public void drawRect(Pixels pixels, Rect rect) {
        if (rect.x < 0) return;
        if (rect.y < 0) return;
        if (rect.x + rect.width > this.width) return;
        if (rect.y + rect.height > this.height) return;

        for (int i = rect.y; i < rect.y + rect.height; i++) {
            for (int j = rect.x; j < rect.x + rect.width; j++) {
                pixels.matrix[i][j] = rect.texture;
            }
        }
    }

    public void drawTriangle(Pixels pixels, Triangle triangle) {
        if (triangle.x < 0) return;
        if (triangle.y < 0) return;
        if (triangle.x + triangle.height > this.width) return;
        if (triangle.y + triangle.height > this.height) return;

        int y = triangle.y-1;
        int x = triangle.x;

        int from = x;
        int to = x+triangle.width;

        for (int i = y+triangle.height; i > y; i--) {
            for (int j = from; j < to; j++) {
                pixels.matrix[i][j] = triangle.texture;
            }
            from++;
            to--;
        }

    }

    public void drawCircle(Pixels pixels, Circle circle) {
        if (circle.x < 0) return;
        if (circle.y < 0) return;
        if (circle.x + circle.width > this.width) return;
        if (circle.y + circle.height > this.height) return;

        int r = circle.rad;
        int b = circle.x+circle.rad, a = circle.y+circle.rad;
        // whitespace
        int s = 3;
        // print area
        int xMin = a - r - s, xMax = a + r + s;
        int yMin = b - r - s, yMax = b + r + s;

        // output an ASCII circle and axes
        for (int y = yMax; y >= yMin; y--) {
            for (int x = xMin; x <= xMax; x++) {
                if ((int) Math.sqrt((x - a) * (x - a) + (y - b) * (y - b)) == r) {
                    // circle
                    pixels.matrix[x][y] = circle.texture;
                } else if (x == a && y == b) {
                    // center of the circle
                    pixels.matrix[x][y] = circle.texture;
                }
            }
        }
    }
}
