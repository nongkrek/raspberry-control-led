# raspberry-control-led
This repository provide script for controlling LED through Raspberry Pi based on service oriented.
This article explain about web application using HTML and PHP for control (turn on or turn off) LED that connected through Raspberry Pi 2 Model B. For making this apps, needed some parts :
  1.	Computer/Laptop as a server
  2.	Raspberry Pi 2 Model B
  3.	Mini Breadboard
  4.	LED (3)
  5.	Resistor 270 Ohm (3)
  6.	Jumper Cable (Female-to-Male) 
  7.	Network Cable(UTP) .
  8.	Power Cable for Raspberry 5v 2A.
  9.	Access Point/Router Mikrotik.
Before assemble that parts, we have to understand about pin and GPIO of Raspberry Pi 2 Model B. 
Sebelum merangkai komponen tersebut, harus dipahami arsitektur pin dari GPIO Raspberry Pi 2 Model B. Here is the architecture of pin and GPIO of Raspberry Pi 2 Model B.

![image](http://yaddarabullah.net/raspberry-control-led/Pin-GPIO-Raspberry.png)

Layout Scheme

Next step we will assemble the parts, stared with put LED, resistor and jumper cable to breadboard. For your information, LED consist of two leg, first is positive (anode) and the second one is negative (cathode). To distinguish both of positive and negative, you can see from height of leg. For longer leg, it is positive and the second one is negative. For the first LED, the postitive leg connected with resistor (270 ohm) and the another leg of resistor connected to ground (see the figure 2,3 and 4). Next connected jumper cable (male-to-female), for male connected to positive leg and the female of jumper cable connected to pin 7 raspberry pi (GPIO 4). For the second LED has the same step, but for female of jumper cable (that connected to second LED) will connected to pin 11 raspberry pi (GPIO 17), and then for the third LED connected to pin 12 raspberry (GPIO 18). For more detail, see this figure : 

![image](http://yaddarabullah.net/raspberry-control-led/figure1.png)

Figure 2. Layout Scheme -1

![image](http://yaddarabullah.net/raspberry-control-led/figure2.png)

Figure 3. Layout Scheme -2

![image](http://yaddarabullah.net/raspberry-control-led/figure3.png)

Figure 3. Layout Scheme -3

System Architecture

The system architecture that used is based on Service Oriented Architecture (SOA) approach.

![image](http://yaddarabullah.net/raspberry-control-led/figure4.png)

With that architecture, you can make a raspberry as a node that will run script for request and respond data from service(server). Server provide service that used for giving information about state of LED, that info was gotten from storage (teks file). Web apps (html) used as interface for controlling LED.

Source Code

source code consist of some file : file raspberry-script-led.py for run at raspberry, file service-led.php locate at server web, file ui-control.html locate at server web, 3 teks file. For simulation you can set IP Address of server is IP 10.10.10.111 and raspberry has same network with server.

Hope this script helpful

Thank You

by : Yaddarabullah

