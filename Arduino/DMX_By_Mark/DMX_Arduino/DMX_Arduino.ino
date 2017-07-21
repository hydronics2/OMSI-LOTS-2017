#include <DmxSimple.h>
char receivedChar;
int n = 1;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  DmxSimple.usePin(3);
  DmxSimple.maxChannel(9);
}


void loop() {
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
        n = 1;
      }
    }
  }
}

