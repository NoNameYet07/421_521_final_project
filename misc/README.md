BioE 421/521 Final Project
==========================

#BioE 521 Final Project (BEERduino): Brainstorm
####Authors: Karl Gerhardt, Samantha Paulsen


For our project we would implement a solenoid valve and a user identification system to regulate beer dispensing from a team member’s personal kegerator 

Two systems:
	*Regulation/beer flow
	*Solenoid valve ($20 on Amazon)
	*Identification
	*Card swipe/login ($25 on Amazon)

Our first goal will be implementing a system to regulate beer dispensing. We would also implement an Arduino-regulated valve system to turn beer flow on or off depending on the user’s permissions. Permissions could stem from whether the user has an account, the user’s age, or the amount of money/credit the user has towards beer. 

We plan to use either the Pi Camera or a Barcode Scanner ($25 from Amazon) to read a driver’s license and determine the user’s name and age. This information would then be used to link each individual user with a pre-made user account for the kegerator system.

We could easily adjust the scope of this project by altering the identification system: If license ID doesn’t work users could enter login codes/snap pictures of individually printed QR codes. We can also alter the number of permissions tied with the valve system. 


##BEERduino

#BioE 521 Final Project Abstract
#Authors: Karl Gerhardt, Samantha Paulsen


When a resource is shared within a population, tracking the consumption rate and who is doing the consuming is of interest to the individuals sharing the resource. The shared resource in the context of a domicile cohabited by a population of college roommates is often beer. Here, we propose an automated beer tracking and allocating system which can be implemented on a refrigerated draft beer dispensing device known as a “kegerator”. User tracking operations are achieved through a card scanner (or camera)-Raspberry pi device which captures a user’s driver’s license barcode and decides whether the user qualifies for access to beer. Criteria for this decision will be based on whether the user has an account in good standing located on the Raspberry pi. An admin is responsible for maintaining accounts. The flow of beer is physically and electronically regulated by an in-line DC solenoid valve which is controlled with an Arduino Uno taking input from the Raspberry pi. If a user with a BEERduino account in good standing scans their driver’s license, the valve will open and beer can be dispensed for a period of time needed to pour approximately one pint of beer. The admin can alternatively put the BEERduino system into “party mode”, in which case any driver’s license which establishes a date of birth > 21 years will qualify for unlimited access to beer. Once a beer keg has been exhausted, the admin can assign balances to user’s accounts in proportion to the number of times the user accessed beer. BEERduino, therefore, is a simple yet effective tool which maintains fairness in the sharing of a costly resource: beer. 

