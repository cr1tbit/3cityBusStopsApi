# 3city Bus Stops lightweight API for embedded devices 

This simple flask app works as a simple wrapper for (rather heavy) JSON api provided by Gdańsk public transportation operator.

Handling all of this data on an MCU would be pain in the backbone - filtering this
stuff in python is way easier. Also, one day I wish to create HTML frontend too.

The provided API allows user to create their own virtual Bus stop display, J̵̫͖̜̀̀̎͢͡u̷̧̪̗͚͗̊̿͝s҉̢̛̭̱͓̉̀́t̸̨͍̿̍́͝ ḻ̶̾̕͢i̷̡͓͊͠k҉̖̙̑͢͠ę̶̘̠̠̀͌̇͡ t̴̘͒́̉͢͝h̷̢͈҇̽̐i̸̢͈͇҇̎͆̍s҉̧̙̱̞̾̒́͝ ǫ̶͇̲͛͝n̶̢͈͒͂͂͝e҈̨̣̀͞


![HE COMES](https://i.ytimg.com/vi/jEyFTG4uJnQ/maxresdefault.jpg)

(or [better one](https://ztm.gda.pl/rozklady/rozklad-199_20190518-11-1.html)!)
## API description

The app provides following endpoints:<br>


API with filtered JSON content - providing 'dh' filters the result for most recent arrivals
```
/json?id=stopId&dh=2
/json?id=stopId
```


API for raw text output - dw/dh parameters are target alphanumeric display size
```
/disp?id=stopId&dw=16&dh=2
```
(dw parameter is not handled atm.)

## Where do I get my bus stop's stopId?
This info could be extracted from the API too, but I've found it way easier to just go into ZTM's official website and find info for the interesting stop manually.

1. Go to https://ztm.gda.pl/ 
2. Click on any bus that tends to visit your bus stop
3. Click on the bus stop which you're interested in - please keep in mind that bus stop in each direction has its' own unique ID. In some cases, there might also exist separate entities for night bus stops. 
4. The bus stop's ID may be located to the left of the bus stop's name.

Example: https://ztm.gda.pl/rozklady/rozklad-199_20190518-11-1.html  
This bus stop's ID is '1339'.

## Please note, right now this project should be considered "work-in-progress".
Important TODOs:

- Caching API requests
- Creating endpoint for multiple bus stops to be squashed into a single response

