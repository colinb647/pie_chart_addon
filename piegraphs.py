# Copyright 2016 Matthew Hayes

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import datetime
import json
import math
import anki.stats
import anki.collection
from anki.hooks import wrap


defaultColor = "#0F0"
colYoung = "#7c7"
colMature = "#070"
colCum = "rgba(0,0,0,0.9)"
colLearn = "#00F"
colRelearn = "#c00"
colCram = "#ff0"
colIvl = "#077"
colHour = "#ccc"
colTime = "#770"
colUnseen = "#000"
colSusp = "#ff0"

OLD_cards = anki.stats.CollectionStats._cards

def _cards_alt(self):
    if self.col.schedVer() == 2:
        return self.col.db.first("""
            select
            sum(case when type=2 and ivl >= 21 then 1 else 0 end), -- mtr
            sum(case when type=2 and ivl < 21 then 1 else 0 end), -- yng
            sum(case when type in (1,3) then 1 else 0 end), -- lrn
            sum(case when type=0 then 1 else 0 end), -- new
            sum(case when queue<0 then 1 else 0 end) -- susp
            from cards where did in %s""" % self._limit())
    else:
        return self.col.db.first("""
            select
            sum(case when queue=2 and ivl >= 21 then 1 else 0 end), -- mtr
            sum(case when queue=2 and ivl < 21 then 1 else 0 end), -- yng
            sum(case when queue in (1,3) then 1 else 0 end), --lrn
            sum(case when queue=0 then 1 else 0 end), -- new
            sum(case when queue<0 then 1 else 0 end) -- susp
            from cards where did in %s""" % self._limit())


anki.stats.CollectionStats._cards = wrap(anki.stats.CollectionStats._cards, _cards_alt, pos="after")

###############################################################################

OLDcardGraph = anki.stats.CollectionStats.cardGraph

def cardGraph_alt(self):
    # pie graph data
    div = self._cards()
    d = []
    if self.col.schedVer() == 2:
        for c, (t, col) in enumerate((
            (_("Mature"), colMature),
            (_("Young"), colYoung),
            (_("Learn"), colLearn),
            (_("Unseen"), colUnseen),
            (_("Suspended+Buried"), colSusp))):
            d.append(dict(data=div[c], label="%s: %s" % (t, div[c]), color=col))
        # text data
        i = []
        (c, f) = self.col.db.first("""
            select count(id), count(distinct nid) from cards
            where did in %s """ % self._limit())
        self._line(i, _("Total cards"), c)
        self._line(i, _("Total notes"), f)
        (low, avg, high) = self._factors()
        if low:
            self._line(i, _("Lowest ease"), "%d%%" % low)
            self._line(i, _("Average ease"), "%d%%" % avg)
            self._line(i, _("Highest ease"), "%d%%" % high)
        info = "<table width=100%>" + "".join(i) + "</table><p>"
        info += _('''\
            A card's <i>ease</i> is the size of the next interval \
            when you answer "good" on a review.''')
        txt = self._title(_("Card Types"),
                          _("The division of cards in your deck(s)."))
        txt += "<table width=%d><tr><td>%s</td><td>%s</td></table>" % (
            self.width,
            self._graph(id="cards", data=d, type="pie"),
            info)
        return txt
    else:
        return OLDcardGraph(self)

anki.stats.CollectionStats.cardGraph = wrap(anki.stats.CollectionStats.cardGraph, cardGraph_alt, pos="after")
