PImage img;
int Ax = 0;
int Bx = 85;


void setup () {
  size(500, 500); 
  img = loadImage("city.jpg");
}  


void draw () {
  
  image(img, 0, 0);

  //carro
 
  rect(Ax, 435, 90, 45);
  //roda
 
  ellipse(Ax, 480, 30, 30);
  //roda
  
  ellipse(Bx, 480, 30, 30);
  
  //botao1
  fill(#0815FC);
  rect(0, 0, 70, 70);
  //botao2
  fill(#08FC2E);
  rect(width-70, 0, 70, 70);  
  
if(Ax>width) Ax = -55;
if(Bx>width) Bx = -55;
  fill(255);
  if(var==1) fill(#0815FC);
  if(var==2) fill(#08FC2E);
  
  
  
  
  
  Bx = Bx + 1;
  Ax = Ax + 1;
}

int var = 0;

void mousePressed(){
  if(mouseButton == LEFT){
    if((mouseX<70) && (mouseY<70)) var = 1;
    if((mouseX>(width-70) && (mouseY<70))) var = 2;}
}