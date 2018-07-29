# fetchGoogleImage

This script fetchs the images from google image search.   


## Prerequisite
You need install the programs mentioned below.
- python3
- selenium
- webdriver for chrome

and I tested this script only on debian9, so on other os this script may not work

## Usage
At first you need set the environmental varialbe for "WEBDRIVER_PATH".
If you put the webdriver in the same folder as this script, you should execute this command.
```
export WEBDRIVER_PATH=`pwd`/chromedriver
```

And then you can execute the command
```
./fetchGoogleImage.py  <query> <output folder>
```


