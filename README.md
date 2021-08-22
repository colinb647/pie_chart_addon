# Stats Pie Graph with Distinct 'Learning' and/or 'Relearning' Sections #

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fcd8608d6d9b419f851c231961d60646)](https://www.codacy.com/gh/colinb647/pie_chart_addon/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=colinb647/pie_chart_addon&amp;utm_campaign=Badge_Grade)

**An Anki addon to change the pie chart colors in the stats overview window.**

The stock version of Anki includes a pie chart at the end of the statistics overview screen, with the deck/collection divided into 'New', 'Suspended+Buried', 'Young+Learning', and 'Mature' sections.

Since I use longer intervals while 'learning' compared to the default options, I've felt it may be better to separate 'Young' and 'Learning' cards. However, vanilla Anki doesn't include this option, so I figured I'd make one!

Notably, as of v1.1, this addon is **compatible with both v1 and v2 review scheduler versions!**

## Development ##

### Version history ###

- **v1.1**: Adapted `piegraphs.py` functions (and created `config.md` and `config.json`) to allow user configuration via the addons manager. **_Compatible with both v1 and v2 scheduler versions._**

- **v1.0.1**: minor formatting updates
- **v1.0**: initial release

---

### Examples ###

**Native divisions/colors:**

![picture alt](https://github.com/colinb647/pie_chart_addon/blob/master/example_pics/vanilla_graph.png)

**Graph with 'learning' cards option enabled (alone):**
![picture alt](https://github.com/colinb647/pie_chart_addon/blob/master/example_pics/learning_only.png)

**Graph with 'relearning' cards option enabled (alone):**
![picture alt](https://github.com/colinb647/pie_chart_addon/blob/master/example_pics/relearning_only.png)

**Graph with _both_ 'learning' and 'relearning' card options enabled:**
![picture alt](https://github.com/colinb647/pie_chart_addon/blob/master/example_pics/learning_relearning.png)

---

### Installation ###

#### Via the Addon Manager ####

The addon number for install via the in-program app is **1828603731**. To see the addon page, visit [here](https://ankiweb.net/shared/info/1828603731).

#### Manual Installation ####

Create a folder in your respective addons folder (or clone this one), so that it contains **\_\_init\_\_.py** and piegraphs.py.

**Do not put these in a subfolder**; i.e., it should be `.../addons_folder/newFolder/files.py`. The `meta.json` file should be created automatically by Anki after loading for the first time after install.

**_Conflicts with other addons_**: The only ones I imagine are those that also modify the native `cardGraph` or `_cards` function of `anki/stats.py`, declared as `anki.stats.Collection.cardGraph` or `anki.stats.Collection._cards`. There was a previous conflict with [Progress Graphs and Stats for Learned and Matured Cards](https://ankiweb.net/shared/info/266436365), but this resolved with some debugging of the function wraps used here.
