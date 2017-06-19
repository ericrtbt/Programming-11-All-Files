from earsketch import *

init()
setTempo(100)


#sounds

#A


for measure in range(1,32):
  fitMedia(Y26_PERCUSSION_2,1,measure,measure+1)
for measure in range(1,32):
  fitMedia(Y26_PERCUSSION_1,2,measure,measure+1)
fitMedia(YG_NEW_HIP_HOP_CHOIR_1,3,8,34)
fitMedia(YG_NEW_HIP_HOP_CHOIR_2,4,6,8)
fitMedia(RD_UK_HOUSE__AIRYPAD_1,14,1,5)
fitMedia(YG_EDM_LOW_NOTE_1,9,1,17)
  
#B

fitMedia(HIPHOP_BASSSUB_001,5,12,31)
fitMedia(HIPHOP_DUSTYMOOG_001,6,16,27)
fitMedia(HIPHOP_DUSTYSTRINGS_001,7,18,31)
fitMedia(HIPHOP_FUNKBASS_001,8,20,31)

#C
for measure in range(32,50):
  fitMedia(Y26_PERCUSSION_2,1,measure,measure+1)
for measure in range(32,50,2):
  fitMedia(Y26_PERCUSSION_1,2,measure,measure+1)
fitMedia(YG_TRAP_SYNTH_CHOIR_1,14,29,45)
fitMedia(HIPHOP_SOLOMOOGLEAD_001,10,49,50)

#effect
setEffect(3,DELAY,DELAY_TIME,40)
setEffect(3,CHORUS,CHORUS_LENGTH,17)
setEffect(3,CHORUS,CHORUS_NUMVOICES,3)
setEffect(3,CHORUS,CHORUS_RATE,4)
setEffect(3,CHORUS,CHORUS_MOD,0.3)
setEffect(14,CHORUS,CHORUS_NUMVOICES,3)
setEffect(14,VOLUME,GAIN,-15,29,-16,45)

#beat
dubBass1 = "0+++++++------0+"
dubBass2 = "0++0++0+---0++0+"
dubBass3 = "0++0++0+------0+"
dubBass4 = "00+00+0+--------"

bass = DUBSTEP_BASS_WOBBLE_014

for measure in range (4, 40, 6):
 makeBeat(bass, 11, measure, dubBass1)
 makeBeat(bass, 11, measure+1, dubBass2)
 makeBeat(bass, 11, measure+2, dubBass3)
 makeBeat(bass, 11, measure+3, dubBass4)

finish()
