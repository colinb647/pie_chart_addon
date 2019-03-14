### Popup Dictionary Configuration

Changes in these settings require a restart to apply:

- `showLearning` (true/false): Whether or not to enable results drawn from the dictionary note type. Default: `true`.
- `showRelearning` (true/false): Whether or not to enable results drawn from the dictionary note type. Default: `false`.
- `ignoreSuspended` (true/false): Whether or not to enable results drawn from the dictionary note type. Default: `false`.


v2:
# card types: 0=new, 1=lrn, 2=rev, 3=relrn
# queue types: 0=new, 1=(re)lrn, 2=rev, 3=day (re)lrn,
#   4=preview, -1=suspended, -2=sibling buried, -3=manually buried
# revlog types: 0=lrn, 1=rev, 2=relrn, 3=early review
# positive revlog intervals are in days (rev), negative in seconds (lrn)
# odue/odid store original due/did when cards moved to filtered deck

v1:
# queue types: 0=new/cram, 1=lrn, 2=rev, 3=day lrn, -1=suspended, -2=buried
# revlog types: 0=lrn, 1=rev, 2=relrn, 3=cram
# positive revlog intervals are in days (rev), negative in seconds (lrn)
