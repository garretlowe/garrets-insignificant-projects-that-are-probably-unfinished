# MH: Rise Fextralife Scraper | March 2022 | Completed

I made this tool to ease the data entry for my steam guide: [A Hunter's Bestiary - Low/High Rank Monster Stats](https://steamcommunity.com/sharedfiles/filedetails/?id=2732708878). The idea of the guide was to provide the important information from the wiki without the ads/embeds which lag the Steam Overlay Web Browser.

The script first scrapes the names and addresses for every large monster posted on the Fextralife Wiki. It then iterates through the entries and sacrapes detailed data from each page.

### Ideas To Improve

Split the Master rank monsters into separate files from the High/Low rank monsters.

### How To Use

Run the program via CLI: `py ./main.py`.

BBCode formatted output will be saved to a folders: `./Large Monsters/` and `./Apex Monsters/`.

### Learning Outcomes

Python, Web Scraping, XPaths, BB Code