// Libraries
#include <mbed.h>

// Serial microcontroller
Serial pc(USBTX, USBRX);

// Timers
Timer timerAccuPercentage;

// Main loop
int main() {
    // Baud rate
    pc.baud(9600);

    // CAN-bus accu:
    float voltage = 40;
    float current = 20;
    float accuPercentage = 100;
    float temperature = 25; // kamertemperatuur

    // CAN-bus accu cel level:
    float celNumber1 = 1, celNumber2 = 2, celNumber3 = 3, celNumber4 = 4, celNumber = 5, celNumber6 = 6, celNumber7 = 7, celNumber8 = 8, celNumber9 = 9, celNumber10 = 10, celNumber11 = 11, celNumber12 = 12; 
    float celVoltage1 = 10, celVoltage2 = 20, celVoltage3 = 30, celVoltage4 = 40, celVoltage5 = 50, celVoltage6 = 60, celVoltage7 = 70, celVoltage8 = 80, celVoltage9 = 90, celVoltage10 = 100, celVoltage11 = 110, celVoltage12 = 120;
    float celTemperature1 = 100, celTemperature2 = 200, celTemperature3 = 300, celTemperature4 = 400, celTemperature5 = 500, celTemperature6 = 600, celTemperature7 = 700, celTemperature8 = 800, celTemperature9 = 900, celTemperature10 = 1000, celTemperature11 = 1100, celTemperature12 = 1200;

    // CAN-bus accu while charging:
    float voltageIn = 45;
    float currentIn = 3;

    // CAN-bus motorcontrollers:
    float RPS = 200; 
    float angleAccelerationPaddle = 45;
    
  while(1) {
    // Timer counts till 6 then the accu accuPercentage drops with 0.1%. 
    // After this loop the timer resets its self. 
    timerAccuPercentage.start(); 
    if(timerAccuPercentage > 6){
      accuPercentage = accuPercentage - 0.1;
      timerAccuPercentage.reset();
    }
    // Sends data
    pc.printf("%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n", voltage, current, accuPercentage, temperature, celNumber1, celNumber2, celNumber3, celNumber4, celNumber, celNumber6, celNumber7, celNumber8, celNumber9, celNumber10, celNumber11, celNumber12, celVoltage1, celVoltage2, celVoltage3, celVoltage4, celVoltage5, celVoltage6, celVoltage7, celVoltage8, celVoltage9, celVoltage10, celVoltage11, celVoltage12, celTemperature1, celTemperature2, celTemperature3, celTemperature4, celTemperature5, celTemperature6, celTemperature7, celTemperature8, celTemperature9, celTemperature10, celTemperature11, celTemperature12, voltageIn, currentIn, RPS, angleAccelerationPaddle);
    wait(1); 
  }
}





