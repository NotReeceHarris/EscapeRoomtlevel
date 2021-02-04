
<p align=center>

  <img src="https://i.imgur.com/pZQRQ9k.png" alt="Escape ROOM" />

  <br>
  <br>
  <span>Terminal based random escape room game <br></span>
  <br>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.8-green.svg"></a>
</p>

<p align="center">
  <a href="#Contributors">Contributors</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Run">Run</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Features">Features</a>
</p>

## Run
[![Run on Repl.it](https://user-images.githubusercontent.com/27065646/92304596-bf719b00-ef7f-11ea-987f-2c1f3c323088.png)](https://repl.it/github/NotReeceHarris/EscapeRoomtlevel)

## Debugging options
```json
// Within "jsonFiles/data.json" there is a atribute names "Debug" change this to "true"

{
  "inventorySpace": 5,
  "Debug": false
}
```
This just displays that data is that run as it will be diffrent every run
```console
-------Debugging Panel-------

Main Character       : [Runs Main character]
Side Character       : [Runs Side character]
Antagonist Character : [Runs Antagonist character]

Scene: [Runs Scene]

Room1: [Runs Room1]
Room2: [Runs Room2]
Room3: [Runs Room3]
Room4: [Runs Room4]
Room5: [Runs Room5]

Inventory Space : [Games set inventory size]
Special Item    : [Runs Special item]
Special Room    : [Runs Special room]
EscapeRoom      : [Runs EscapeDoor location]

-----------------------------
```

## Edit characters
```json
// Within the "jsonFiles/BaseData.json" there are blocks of characters and items, all are editable
// Customize it to your liking make the game personal to you

{
"Themes": "Mystery",
"Scene": [],
"antagonistNames": [],
"sideCharacterNames": [],
"mainCharacterNames": [],

"Space StationSpecialItem": [],
"Abandoned HospitalSpecialItem": [],
"PrisonSpecialItem": [],
"CastleSpecialItem": []
}
```

## Features
* <strong>Randomization</strong>
* <strong>Puzzles</strong>
* <strong>Game saving features</strong>


## How and why
<span>With all education your set to make projects well this is our project just overcomplicated with 1mil+ possible runs</span>
<span>This project heavily depends on randomness its a simple script for python but a over engineered script for an escaperoom</span>

## Contributors
* [Reece Harris](https://www.linkedin.com/in/reece-harris-3215b91bb/) 
* [Deven Briers](https://www.linkedin.com/in/deven-briers-5b62541bb/)
* [Elijah McVey](https://www.linkedin.com/in/elijah-mcvey-97a5b81bb/)
* [Kyle Willets](https://www.linkedin.com/in/kyle-willets-2315b81bb/)


