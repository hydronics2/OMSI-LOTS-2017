/* Welcome to DmxSimple. This library allows you to control DMX stage and
** architectural lighting and visual effects easily from Arduino. DmxSimple
** is compatible with the Tinker.it! DMX shield and all known DIY Arduino
** DMX control circuits.
**
** DmxSimple is available from: http://code.google.com/p/tinkerit/
** Help and support: http://groups.google.com/group/dmxsimple       */

/* To use DmxSimple, you will need the following line. Arduino will
** auto-insert it if you select Sketch > Import Library > DmxSimple. */

#include <DmxSimple.h>

void setup() {
  /* The most common pin for DMX output is pin 3, which DmxSimple
  ** uses by default. If you need to change that, do it here. */
  DmxSimple.usePin(3);

  /* DMX devices typically need to receive a complete set of channels
  ** even if you only need to adjust the first channel. You can
  ** easily change the number of channels sent here. If you don't
  ** do this, DmxSimple will set the maximum channel number to the
  ** highest channel you DmxSimple.write() to. */
  DmxSimple.maxChannel(511);
}

void loop() {
  int brightness;
  /* Simple loop to ramp up brightness */
  for (brightness = 0; brightness <= 255; brightness++) {
    brightness++;
    /* Update DMX channel 1 to new brightness */
    DmxSimple.write(1, 8);
    DmxSimple.write(2, brightness);
    DmxSimple.write(4, 8);
    DmxSimple.write(5, 55);
    DmxSimple.write(7, 8);
    DmxSimple.write(8, 105);
    DmxSimple.write(10, 8);
    DmxSimple.write(11, brightness);
    DmxSimple.write(13, 8);
    DmxSimple.write(14,brightness);
    DmxSimple.write(16, 8);
    DmxSimple.write(17,10);
    DmxSimple.write(19, 8);
    DmxSimple.write(20,30);
    
    

    
    /* Small delay to slow down the ramping */
    delay(10);
  }

}
