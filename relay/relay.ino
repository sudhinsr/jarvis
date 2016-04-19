#include <dht.h> 
dht DHT; 
#define DHT11_PIN 5                       
#define RELAY1  7 
#define RELAY2  6 

int l=1;
int s=1;
int input=0;
void light()
{
  if(l==0)
  digitalWrite(RELAY1,0);
  else
  digitalWrite(RELAY1,1);
}
void switc()
{
  if(s==0)
  digitalWrite(RELAY2,0);
  else
  digitalWrite(RELAY2,1);
}
void setup(){
  Serial.begin(9600);
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);  
}

void loop(){
  delay(200);
  int h,t;
  int chk = DHT.read11(DHT11_PIN); 
  
  input=Serial.read();
  if(input=='\n')
  input=0;
  if(input=='1')
  l=1;
  else if(input=='2')
  l=0;
  else if(input=='3')
  s=1;
  else if(input=='4')
  s=0;
  light();
  switc();
  h=DHT.humidity;
  t=DHT.temperature;
 
  if(h > 10 && t > 10 && h < 100 && t < 100)
  {
  Serial.print(h, 1); 
  Serial.print("\t");   
  Serial.println(t, 1); 
  }

}
 
