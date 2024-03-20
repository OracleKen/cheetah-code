"""
    IMPORTANT #1:
    Please change game settings to EXACTLY these numbers:
    desktop resolution: 1920x1080
    In-game Video settings:
    Resolution: 1920x1080
    Screen: Borderless
    Force 21:9 Aspect Ratio checked
    In-game Gameplay -> Controls and Display -> HUD size: 110%
    minimap transparency (at top right corner): 100%
    minimap zoom-in (at top right corner): 65%
    IMPORTANT #2: 
    config must be set up correctly in order for the bot to work properly on your machine.
    Refer to the inline comments below:
    For Lopang enjoyers: https://github.com/any-other-guy/LostArk-Endless-Chaos/issues/15
    Set your first bifrost point to be at lopang island.
    Exact location to be right in front of the NPC machine which stands farthest to the entrance.
    Then set your 2/4/5 (because i dont have no3 unlocked) bifrost location to be right in front of those three lopang quest hand-in NPCs.
"""
config = {
    "mainCharacter": 0,  # must be in number 0 to 5 (0 is the first character)ii
    "GFN": False,  # set True for Geforce Now users
    "enableMultiCharacterMode": False,  # this is lit
    "enableUnaTasks": True, 
    "forceAorMode": False,
    "enableGuildDonation": True,  # please make sure all your characters have a guild
    "enableRapport": False,  # NOTE: you need to setup bifrost no3 infront of a rapport NPC
    "floor3Mode": False,  # only enable if you ONLY want to run infinite floor3 clearing Setup your characters below:aaaaaaaaa
    # can setup UP TO 9 characters for daily chaos/lopang/guild stuff however your main must be in character 0 to 5 (
    # just for re-connect back after disconnection happens) ilvl-endless is the dungeon which you want to run
    # infinitely ilvl-aor is the daily aura of resonance dungeon you only want to run TWICE per day IMPORTANT:
    # dungeon ilvl choices are only limited to 1475, 1445, 1370, 1110 for now. I will add more later when brel comes
    # out
    "characters": [
{
            "index": 0,
            "class": "sorceress",
            "chaos": True,
            "ilvl-endless": 1540,
            "ilvl-aor": 1540,
            "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 4}, {"leap": "voldis", "bifrost": 1}],
            "lopang": False,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },
        {
            "index": 1,
            "class": "deathblade",
            "chaos": True,
            "ilvl-endless": 1540,
            "ilvl-aor": 1540,
            "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 4}, {"leap": "voldis", "bifrost": 1}],
            "lopang": False,
            "guildDonation": True,
            "rapport": False,
            "goHome": True
        },

        {
            "index": 2,
            "class": "souleater",
            "chaos": True,
            "ilvl-endless": 1445,
            "ilvl-aor": 1445,
            "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 4}, {"leap": "moko", "bifrost": 1}],
            "lopang": False,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },
        {
            "index": 3,
            "class": "bard",
            "chaos": True,
            "ilvl-endless": 1475,
            "ilvl-aor": 1475,
            "lopang": True,
            # "leapUnas": [{ "leap": "hestera", "bifrost": 0},{"leap": "ghost", "bifrost": 2}, {"leap": "voldis", "bifrost": 1}],
            "guildDonation": True,
            "rapport": False,
            "goHome": True
        },    
        {
            "index": 4,
            "class": "artist",
            "chaos": False,
            "ilvl-endless": 1445,
            "ilvl-aor": 1445,
            # "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 2}, {"leap": "voldis", "bifrost": 4}],
            "lopang": True,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },          
        {
            "index": 5,
            "class": "spear",
            "chaos": True,
            "ilvl-endless": 1340,
            "ilvl-aor": 1340,
            # "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 2}, {"leap": "voldis", "bifrost": 4}],
            "lopang": True,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },
        {
            "index": 6,
            "class": "deathblade",
            "chaos": True,
            "ilvl-endless": 1415,
            "ilvl-aor": 1415,
            # "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 2}, {"leap": "voldis", "bifrost": 4}],
            "lopang": True,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },
        {
            "index": 7,
            "class": "deathblade",
            "chaos": True,
            "ilvl-endless": 1370,
            "ilvl-aor": 1370,
            # "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 2}, {"leap": "voldis", "bifrost": 4}],
            "lopang": True,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },
        {
            "index": 8,
            "class": "summoner",
            "chaos": True,
            "ilvl-endless": 1445,
            "ilvl-aor": 1445,
            # "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 2}, {"leap": "voldis", "bifrost": 4}],
            "lopang": True,
            "guildDonation": False,
            "rapport": False,
            "goHome": True
        },
        # {
        #     "index": 9,
        #     "class": "spear",
        #     "chaos": False,
        #     "ilvl-endless": 1580,
        #     "ilvl-aor": 1580,
        #     "lopang": False,
        #     "leapUnas": [{ "leap": "hestera", "bifrost": 3},{"leap": "ghost", "bifrost": 2}, {"leap": "moko", "bifrost": 4}],
        #     "guildDonation": True,
        #     "rapport": False,
        #     "goHome": True
        # },
        # {
        #     "index": 10,
        #     "class": "scouter",
        #     "chaos": False,
        #     "ilvl-endless": 1540,
        #     "ilvl-aor": 1540,
        #     "leapUnas": [{ "leap": "hestera", "bifrost": 3}, { "leap": "ghost", "bifrost": 2}, { "leap": "moko", "bifrost": 4}],
        #     "lopang": False,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
        # {
        #     "index": 11,
        #     "class": "deathblade",
        #     "chaos": True,
        #     "ilvl-endless": 1560,
        #     "ilvl-aor": 1560,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
        # {
        #     "index": 12,
        #     "class": "gunlancer",
        #     "chaos": True,
        #     "ilvl-endless": 1540,
        #     "ilvl-aor": 1540,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
        # {
        #     "index": 13,
        #     "class": "slayer",
        #     "chaos": True,
        #     "ilvl-endless": 1540,
        #     "ilvl-aor": 1540,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
        # {
        #     "index": 14,
        #     "class": "gunslinger",
        #     "chaos": False,
        #     "ilvl-endless": 1540,
        #     "ilvl-aor": 1540,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
        # {
        #     "index": 15,
        #     "class": "reaper",
        #     "chaos": False,
        #     "ilvl-endless": 1490,
        #     "ilvl-aor": 1490,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
        # {
        #     "index": 16,
        #     "class": "sorceress",
        #     "chaos": False,
        #     "hestera": False,
        #     "ilvl-endless": 1490,
        #     "ilvl-aor": 1490,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },



        # {
        #     "index": 12,
        #     "class": "arty",
        #     "chaos": False,
        #     "ilvl-endless": 1445,
        #     "ilvl-aor": 1445,
        #     "lopang": True,
        #     "guildDonation": True,
        #     "rapport": False,
        # },
 

        
    ],
    "performance": False,  # set True for lower-end PCs
    "interact": "g",  # change this if you have binded it to something else eg.mouse button
    "move": "left",  # or "right"
    "blink": "space",
    "meleeAttack": "c",
    "awakening": "v",
    "healthPot": "f1",  # important to put your regen potion on this buttonG
    "healthPotAtPercent": 0.35,  # health threshold to trigger potion
    # "useAwakening": True, # not checking this for now
    # "useSpeciality1": True, # not checking this for now
    # "useSpeciality2": True, # not checking this for now
    "auraRepair": True,  # True if you have aura, if not then for non-aura users: MUST have your character parked near a repairer in city before starting the script
    "shortcutEnterChaos": True,  # you want to use True
    "useHealthPot": False,  # you want to use True
    "useHealthPotAor": True,
    # You might not want to touch anything below, because I assume you have your game setup same as mine :) otherwise something might not work properly!
    "confidenceForGFN": 0.9,
    "regions": {
        "minimap": (1655, 170, 260, 200),  # (1700, 200, 125, 120)
        "abilities": (625, 779, 300, 155),
        "awakening": (680, 875, 50, 150),
        "leaveMenu": (0, 154, 250, 300),
        "buffs": (625, 779, 300, 60),
        "center": (685, 280, 550, 420),
        "portal": (228, 230, 1370, 570),
        "specials": (885, 825, 1030, 935)
    },
    "screenResolutionX": 1920,
    "screenResolutionY": 1080,
    "clickableAreaX": 500,
    "clickableAreaY": 250,
    "screenCenterX": 960,
    "screenCenterY": 540,
    "minimapCenterX": 1772,
    "minimapCenterY": 272,
    "timeLimit": 420000,  # to prevent unexpected amount of time spent in a chaos dungeon, a tiem limit is set here, will quit after this amount of seconds
    "timeLimitAor": 600000,  # to prevent unexpected amount of time spent in a chaos dungeon, a tiem limit is set here, will quit after this amount of seconds
    "blackScreenTimeLimit": 90000,  # if stuck in nothing for this amount of time, alt f4 game, restart and resume.
    "delayedStart": 1000,
    "portalPause": 700,
    "healthCheckX": 690,
    "healthCheckY": 854,
    "charSwitchX": 540,
    "charSwitchY": 683,
    "charSwitchDownArrowX": 1260,
    "charSwitchDownArrowY": 640,
    "charSwitchUpArrowX": 1260,
    "charSwitchUpArrowY": 392,

    "charPositionsAtCharSelect": [
        [500, 827],
        [681, 827],
        [874, 827],
        [1050, 827],
        [1237, 827],
        [1425, 827],
    ],
    "charPositions": [
        [760, 440],
        [960, 440],
        [1160, 440],
        [760, 530],
        [960, 530],
        [1160, 530],
        [760, 620],
        [960, 620],
        [1160, 620],
        [760, 620],
        [960, 620],
        [1160, 620],
        [760, 620],
        [960, 620],
        [1160, 620],
        [760, 620],
        [960, 620],
        [1160, 620],
        [760, 620],
        [960, 620],
        [1160, 620],
        [760, 620],
        [960, 620],
        [1160, 620]       
    ],
    "offlinePositions": [
        [1826, 905],
        [1834, 868],
        [1872, 385],
        [1810, 444]
    ],
    "charSelectConnectX": 1030,
    "charSelectConnectY": 684,
    "charSelectOkX": 920,
    "charSelectOkY": 590,
}