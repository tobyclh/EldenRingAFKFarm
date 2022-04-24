# Elden Ring AFK Farm on Ubuntu
Farm Elden ring runes shamelessly. 
This requires the end game weapon and the site of grace.  
But if you are here I am guessing that you already got that figured out. 

## Install 
The only dependency is pyautogui, which you can install with pip.  
`pip install pyautogui`

### Ubuntu
This repository is tested on Ubuntu 20.04. 

### PS Remote play  
It might work for PS Remote play if you setup the key bindings properly. 
I can't test it for PS because scalpers.  

### Windows
Haven't tested it myself but probably will work, but you have a lot other options anyway (didn't test any of these).  
1. https://github.com/AdamBissonnette/elden-ring-bot  
2. https://www.reddit.com/r/Eldenring/comments/u8ynx1/a_nontoxic_way_to_afk_farm/


## Usage
1. Equip the appropriate weapon (wave of gold)  
2. Set 'b' to use the ash of war in the control menu  
3. Wrap to the palace bonfire
3. `python main.py` in your terminal
4. switch active window to Elden ring within 3 seconds  
5. Profit 
6. Terminate the script by just terminating ctrl+c as usual

## Optimize
The current timing is set based on my personal rig (Ryzen 5700, Rtx 2080Ti), and it is rather tight to speed up the farming.   
You should adjust the timing if the script isn't working on your system.  
For example the load time might be shorter if you have better SSD than I do. The easiest way to do that is to edit the variables at the top of `main.py` (START_DELAY, LOAD_TIME). 

## Note
I was also trying AutoKey for better trigger/terminate support, but I just couldn't get it working for some reason. Feel free to make PR to make this AutoKey competiable. 