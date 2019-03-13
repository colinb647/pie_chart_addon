# Stats Pie Chart with Distinct 'Learning' Section #
**An Anki addon to alter pie chart color in the stats overview screen.**


The stock version of Anki includes a pie chart at the end of the statistics overview screen, with the deck/collection divided into 'New', 'Suspended+Buried', 'Young+Learning', and 'Mature' sections.

As I use longer intervals while 'learning' compared to the default options, I've felt it may be better to separate 'Young' and 'Learning' cards. However, stock anki doesn't include that option, so I figured I'd make one!

___
### Compare the graph with this addon enabled:

![picture alt](https://github.com/colinb647/pie_chart_addon/blob/working_branch/pic%20with%20addon.png)

### Same info with the native divisions/colors:

![picture alt](https://github.com/colinb647/pie_chart_addon/blob/working_branch/pic%20without%20addon.png)

___

## Installation

#### Via the Addon Manager:
Addon number for install via the in-program app is **1828603731**. To see the addon page, visit [here](https://ankiweb.net/shared/info/1828603731).

#### Manual Installation 
Create a folder in your respective addons folder (or clone this one), so that it contains __init__.py and piegraphs.py. **Do not put these in a subfolder**; i.e., it should be `.../addons_folder/newFolder/files.py`. The `meta.json` file should be created automatically by Anki after loading for the first time after install.


**_Conflicts with other addons_**: The only ones I've encountered are those that also modify the native `cardGraph` function of `anki/stats.py`, declared as `anki.stats.Collection.cardGraph`.
