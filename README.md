# 3city Bus Stops lightweight API for embedded devices 

This simple flask app works as a simple wrapper for (rather heavy) JSON api provided by Gdańsk public transportation operator.

Handling all of this data on an MCU would be pain in the backbone - filtering this
stuff in python is way easier. Also, one day I wish to create HTML frontend too.

The provided API allows user to create their own virtual Bus stop display, J̵̫͖̜̀̀̎͢͡u̷̧̪̗͚͗̊̿͝s҉̢̛̭̱͓̉̀́t̸̨͍̿̍́͝ ḻ̶̾̕͢i̷̡͓͊͠k҉̖̙̑͢͠ę̶̘̠̠̀͌̇͡ t̴̘͒́̉͢͝h̷̢͈҇̽̐i̸̢͈͇҇̎͆̍s҉̧̙̱̞̾̒́͝ ǫ̶͇̲͛͝n̶̢͈͒͂͂͝e҈̨̣̀͞


![HE COMES](https://i.ytimg.com/vi/jEyFTG4uJnQ/maxresdefault.jpg)

(or better!)
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

Please note, right now this project should be considered "work-in-progress".

