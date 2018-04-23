import ddf.minim.*;
import processing.sound.*;


Minim minim;
AudioPlayer music_player;
PImage play;
PImage pause;


void setup() {
  pause = loadImage("pause.jpg");
  play = loadImage("play.jpg");
  size(1000, 700);
  minim = new Minim(this);
  music_player = minim.loadFile("music.mp3");
}

void draw() {
  background(#FFFFFF);
  image(play, 475, 500, 70, 70);
  image(pause, 390, 500, 70, 70);
   
   for(int i = 0; i < music_player.bufferSize() - 1; i++){
     float x1 = map(i, 0, music_player.bufferSize(), 0, width);
     float x2 = map(i+1, 0, music_player.bufferSize(), 0, width);
     line( x1, 50 + music_player.left.get(i)*50, x2, 50 + music_player.left.get(i + 1)*50);
     line( x1, 150 + music_player.right.get(i)*50, x2, 150 + music_player.right.get(i+1)*50);
     
     
   }
}

void mousePressed() {
  if (mouseX > 475 && mouseX < 545 && mouseY > 500 && mouseY < 570){
    music_player.rewind();
    music_player.play();
  }
  if(mouseX > 390 && mouseX < 460 && mouseY > 500 && mouseY < 570) {
    music_player.pause(); 
  }
}
