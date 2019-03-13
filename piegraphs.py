# -*- coding: utf-8 -*-
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

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


OLDcardGraph = anki.stats.CollectionStats.cardGraph

def cardGraph_alt(self):
    # pie graph data
    div = self._cards()
    d = []
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

anki.stats.CollectionStats.cardGraph = wrap(anki.stats.CollectionStats.cardGraph, cardGraph_alt, pos="after")

###############################################################################

OLD_cards = anki.stats.CollectionStats._cards

def _cards_alt(self, _old):
    return self.col.db.first("""
        select
        sum(case when queue=2 and ivl >= 21 then 1 else 0 end), -- mtr
        sum(case when queue=2 and ivl < 21 then 1 else 0 end), -- yng
        sum(case when queue in (1,3) then 1 else 0 end), --lrn
        sum(case when queue=0 then 1 else 0 end), -- new
        sum(case when queue<0 then 1 else 0 end) -- susp
        from cards where did in %s""" % self._limit())


anki.stats.CollectionStats._cards = wrap(anki.stats.CollectionStats._cards, _cards_alt, pos="around")
