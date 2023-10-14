#define ir1 A0
#define ir2 A1
#define ir3 A2
#define ir4 A3
#define ir5 A4
#define m1 4  //Right Motor MA1  // backward
#define m2 8  //Right Motor MA2 // foraward
#define m3 2  //Left Motor MB1  // forward 
#define m4 7 //Left Motor MB2 // backward
#define e1 9  //Right Motor Enable Pin EA
#define e2 10 //Left Motor Enable Pin EB
#define s 155  // max speed 

void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(m3, OUTPUT);
  pinMode(m4, OUTPUT);
  pinMode(e1, OUTPUT);
  pinMode(e2, OUTPUT);
  pinMode(ir1, INPUT);
  pinMode(ir2, INPUT);
  pinMode(ir3, INPUT);
  pinMode(ir4, INPUT);
  pinMode(ir5, INPUT);

  Serial.begin(9600);
}

void loop() {
  int s1= digitalRead(ir1);
  int s2= digitalRead(ir2);
  int s3= digitalRead(ir3);
  int s4= digitalRead(ir4);
  int s5= digitalRead(ir5);
  Serial.println(s1);
  Serial.println(s1);
  Serial.println(s2);
  Serial.println(s3);
  Serial.println(s4);
  Serial.println(s5);
  

// put your main code here, to run repeatedly:
// forward 
//  bool ultra=(d1<=200 && d2 <=200);
   
if(((s1 == 0) && (s2 == 0) && (s3 == 1) && (s4 == 0) && (s5 == 0))){
  nalogWrite(e1, s-20); 
  analogWrite(e2, s-20);
  digitalWrite(m1, LOW);
  digitalWrite(m2, HIGH);
  digitalWrite(m3, HIGH);
  digitalWrite(m4,LOW);
    
  delay(10);
}
   
// right turn 
if(((s1 == 1) && (s2 == 1) && (s3 == 1) && (s4 == 0) && (s5 == 0))){
  delay(250);
//      if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 0)){
       analogWrite(e1, s-20); //you can adjust the speed of the motors from 0-255
     digitalWrite(m1, LOW);
      digitalWrite(m2, HIGH);
      digitalWrite(m3, LOW);
      digitalWrite(m4, LOW);
      
      delay(600);
//    }
    }
    
    // left turn
     if((s1 == 0) && (s2 == 0) && (s3 == 1) && (s4 == 1) && (s5 == 1)){
       analogWrite(e2, s-20); 
    digitalWrite(m1, LOW);
    digitalWrite(m2, LOW);
    digitalWrite(m3, HIGH);
    digitalWrite(m4, LOW);
    
      delay(600);
     }
     
     // when all ir in white dead end we reverse bot 
      if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 0)){
        delay(200);
        if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 0)){
         analogWrite(e1, s-40); 
   analogWrite(e2, s-40);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, LOW);
    digitalWrite(m4,HIGH);
      delay(300);
        }
     }
     
     // when all sensor in black line 
      if((s1 == 1) && (s2 == 1) && (s3 == 1) && (s4 == 1) && (s5 == 1)){
       analogWrite(e2, s-40); 
    digitalWrite(m1, LOW);
    digitalWrite(m2, LOW);
    digitalWrite(m3, HIGH);
    digitalWrite(m4, LOW);
      delay(600);
      // left function ko call karna jab T or cross junction aaye toh 
     }
     
     // when right curve occur low curvature 
      if((s1 == 0) && (s2 == 1) && (s3 == 1) && (s4 == 0) && (s5 == 0))
       {
  analogWrite(e1, s-40); 
   analogWrite(e2, s-60);
   
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
  
      delay(50);
     }
     
     // when right curve normal curvature occur  
     if((s1 == 0) && (s2 == 1) && (s3 == 0) && (s4 == 0) && (s5 == 0)){
       analogWrite(e1, s-40); 
   analogWrite(e2, s-65);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
 delay(50);
     }
     
     // when right curve  high curvature occur 
     if((s1 == 1) && (s2 == 1) && (s3 == 0) && (s4 == 0) && (s5 == 0)){
      analogWrite(e1, s-40); 
   analogWrite(e2, s-75);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
    delay(50);
     }
       if((s1 == 1) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 0)){
      analogWrite(e1, s-40); 
   analogWrite(e2, s-100);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
    delay(100);
     }
     
     
     // when left curve occur low curvature 
      if((s1 == 0) && (s2 == 0) && (s3 == 1) && (s4 == 1) && (s5 == 0)){
       analogWrite(e1, s-60); 
   analogWrite(e2, s-40);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
      delay(50);
     }
     
     // when left curve normal curvature occur  
     if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 1) && (s5 == 0)){
      analogWrite(e1, s-65); 
   analogWrite(e2, s-40);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
   delay(50);
     }
     
     // when left curve  high curvature occur 
     if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 1) && (s5 == 1))
       {
       analogWrite(e1, s-70); 
   analogWrite(e2, s-40);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
    delay(50);
     }
       if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 1))
       {
       analogWrite(e1, s-100); 
   analogWrite(e2, s-40);
    digitalWrite(m1, LOW);
    digitalWrite(m2, HIGH);
    digitalWrite(m3, HIGH);
    digitalWrite(m4,LOW);
    delay(100);
     }
}
