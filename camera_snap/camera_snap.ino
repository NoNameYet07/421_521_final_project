
// Shift register bit values to display 0-9 on the seven-segment display
const byte ledCharSet[10] = {
  B00111111, 
  B00000110, 
  B01011011, 
  B01001111, 
  B01100110, 
  B01101101, 
  B01111101, 
  B00000111, 
  B01111111, 
  B01101111
};

// set the total number of rounds to be played and the number of allowed errors
int num_errors=3;
int num_rounds=10;

//initalizing variables in game
int rand_sounds[10];
int turn=0;
int score=0;
int num[10]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0,};
int count=0;
int numToDisplay=0;
int errors=0;

// three possible tones
int butt1Sound = 1000;
int butt2Sound = 1500;
int butt3Sound = 2000;
int possible_sounds[3] = {butt1Sound, butt2Sound, butt3Sound};
// Pin definitions
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#define SLIDER1  A2 //Matches button 1
#define SLIDER2  A1 
#define SLIDER3  A0 //Matches button 3
#define LIGHT    A3
#define TEMP     A4

#define BUZZER   3
#define DATA     4
#define LED1     5
#define LED2     6
#define LATCH    7
#define CLOCK    8
#define BUTTON1  10
#define BUTTON2  11
#define BUTTON3  12
//v1.7 uses CapSense
//This relies on the Capactive Sensor library here: http://playground.arduino.cc/Main/CapacitiveSensor
#include <CapacitiveSensor.h>

CapacitiveSensor capPadOn92 = CapacitiveSensor(9, 2);   //Use digital pins 2 and 9,
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

void setup() {

  Serial.begin(9600);
  randomSeed(analogRead(0));


  //Initialize inputs and outputs
  pinMode(SLIDER1, INPUT);
  pinMode(SLIDER2, INPUT);
  pinMode(SLIDER3, INPUT);
  pinMode(LIGHT, INPUT);
  pinMode(TEMP, INPUT);

  //Enable internal pullups
  pinMode(BUTTON1, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);

  pinMode(BUZZER, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  pinMode(LATCH, OUTPUT);
  pinMode(CLOCK, OUTPUT);
  pinMode(DATA, OUTPUT);

  //Initialize the capsense
  capPadOn92.set_CS_AutocaL_Millis(0xFFFFFFFF); // Turn off autocalibrate on channel 1 - From Capacitive Sensor example sketch

  Serial.println("Danger Shield Component Test");  

  //Set up the set of random tones
  for(int j=0; j<num_rounds-1; j++) {
     rand_sounds[j]=possible_sounds[random(0,3)];     
  }

  }


void loop()
{
 
 //Use value 2 (Slider position) to adjust playback speed 
 int val2 = analogRead(SLIDER2);     


  // When the turn = 0 the computer plays a set of randomly generated tones
  if (turn==0) {
    //Display the score on 7-segment display
    numToDisplay=score;
    digitalWrite(LATCH, LOW);
    shiftOut(DATA, CLOCK, MSBFIRST, ~(ledCharSet[numToDisplay]));
    digitalWrite(LATCH, HIGH);
     
    //Adjust playback speed with slider #2  
    int set_speed = map(val2, 0, 1020, 1,10);
  
    for (int k=0; k<=score; k++) {
      tone(BUZZER, rand_sounds[k]); //Set sound value for 1s
      delay(1000/set_speed);
      noTone(BUZZER);
      delay(250/set_speed);
      turn=1;
    }   
  }  

//When turn=1 the player presses the buttons to match the computer
  if (turn==1){
    for(int k=0; k<=score;){
      if (digitalRead(BUTTON1) == LOW){
          tone(BUZZER, butt1Sound);
          delay(500);
          noTone(BUZZER);
          num[k]={butt1Sound};
          k++;
      }
         
      if(digitalRead(BUTTON2) == LOW){
          tone(BUZZER, butt2Sound);
          delay(500);
          noTone(BUZZER);
          num[k]={butt2Sound};
          k++;
       }
         
      if (digitalRead(BUTTON3) == LOW){
          tone(BUZZER, butt3Sound);
          delay(500);
          noTone(BUZZER);
          num[k]={butt3Sound};
          k++;
       }
    }  
    delay(250);
    turn=2;
  }

//Turn=2 calculates score
 if (turn==2){
     count=0;
            for(int k=0; k<=score; k++){
                if (num[k]==rand_sounds[k]){
                     count=count+1;
                }
                
                else{
                  break;
                }
            }
            
            if (count>score){
               delay(500); 
               noTone(BUZZER);    
               score=score+1;
               turn=0;
            }
            
            else {
                  score=0;
                  tone(BUZZER, 250);
                  delay(250);
                  noTone(BUZZER);
                  delay(250);
                  turn=0;
                  errors=errors+1;
            }
            
            //Play 'you lost' noise
            if (errors>=num_errors){                
              delay(100); 
              tone(BUZZER, 5000);
              delay(100);
              tone(BUZZER, 4000);
              delay(100);
              tone(BUZZER, 3000);
              delay(100);
              tone(BUZZER, 2000);
              delay(100);
              tone(BUZZER, 1000);
              delay(100);
              tone(BUZZER, 500);
              delay(500);
              noTone(BUZZER);
              turn=3;
                
             }
              ////CHANGE THE SCORE
              if (score>=num_rounds){
                delay(100); 
                tone(BUZZER, 500);
                delay(100);
                tone(BUZZER, 1000);
                delay(100);
                tone(BUZZER, 2000);
                delay(100);
                tone(BUZZER, 3000);
                delay(100);
                tone(BUZZER, 4000);
                delay(100);
                tone(BUZZER, 5000);
                delay(100); 
                tone(BUZZER, 500);
                delay(100);
                tone(BUZZER, 1000);
                delay(100);
                tone(BUZZER, 2000);
                delay(100);
                tone(BUZZER, 3000);
                delay(100);
                tone(BUZZER, 4000);
                delay(100);
                tone(BUZZER, 5000);
                delay(500);
                noTone(BUZZER);
                turn=3;
            }

  }
}

