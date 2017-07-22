#include <DmxSimple.h>
char receivedChar;
int n = 1;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  DmxSimple.usePin(3);
  DmxSimple.maxChannel(21);  //Three times the amount of lights
}


void loop() {
  delay(1000);
  while(Serial.available() > 0){
    receivedChar = Serial.read();
    int PWM = atoi(receivedChar);
    Serial.println(receivedChar);
    if(receivedChar != ','){
      if(n == 1){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 2){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 3){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 4){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 5){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 6){
        DmxSimple.write(n, PWM);
        n ++;
      }
      if(n == 7){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 8){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 9){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 10){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 11){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 12){
        DmxSimple.write(n, PWM);
        n ++;
      }
      if(n == 13){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 14){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 15){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 16){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 17){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 18){
        DmxSimple.write(n, PWM);
        n ++;
      }
      if(n == 19){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 120){
        DmxSimple.write(n, PWM);
        n++;
      }
      if(n == 21){
        DmxSimple.write(n, PWM);
        n = 1;
      }
    }
  }
}

