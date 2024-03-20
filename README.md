# Feature updates

- Update death check to happen more frequent so that reviving happens sooner (no longer goes through full skill rotation before it checks)
- Update to DB orbs image and modified confidence level for more accurate surges  

## Getting started

### 0. Prerequisites:
Install pip:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
python3 -m pip install --upgrade pip
```

### 1.Please change game settings to exactly these numbers:

desktop resolution: 1920x1080\
game resolution: 1920x1080 borderless window, force 21:9 aspect ratio\
HUD size: 110%\
minimap transparency: 100%\
minimap zoom-in: 65%

### 2.Configured character ability settings in /config.py
lots of things can be customized for the best auto clearing experience\
todo.\
Default gameplay settings:
```
    "interact": "g",
    "move": "left",
    "blink": "space",
    "meleeAttack": "c",
    "awakening": "v",
    "healthPot": "f1",
    "healthPotAtPercent": 0.3,
    "selectLevel": True,
    "floor3": False,
    "autoRepair": True,
    "shortcutEnterChaos": True,
    "useHealthPot": True,
```


### 3.Start running script:

```
git clone https://github.com/OracleKen/cheetah-code.git
cd cheetah-code
pip install -r requirements.txt
python3 .\bot.py
```