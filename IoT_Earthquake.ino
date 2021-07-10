int Xout=A0;
int Yout=A1;
int Zout=A2;
int SWOUT=4;

void setup() {
  // put your setup code here, to run once:
pinMode(Xout,INPUT);
pinMode(Yout,INPUT);
pinMode(Zout,INPUT);
pinMode(SWOUT,INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int Xval = analogRead(Xout);
int Yval = analogRead(Yout);
int Zval = analogRead(Zout);

Serial.print("A_X = "+ String(Xval)+ ", A_Y= " + String(Yval)+  ", A_Z = " +String(Zval));

  if (Xval>200 and Yval>200 and Zval>200)
  {
  Serial.print(", Vibration ON");
 
}
else
{
 Serial.print(", Vibration OFF"); 
}
Serial.println("");
delay(200);
}
