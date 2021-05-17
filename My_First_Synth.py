#'''
#Clock.bpm = 100
#ch = var([0,5,2,3],[8,4,2,2])
#b = PlayerKey('bass',ch)
#b.update('bass',ch,dur=(5,4))

#values = [1, 2, 3]

# Use a loop
#my_list = []
#for i in values:
#    my_list.append(i * 2)
#print(my_list)

# List comprehension
#print([i*2 for i in values])
#'''
Clock.bpm = 110

import random

baselist = var([5,1],[8,8])
#duration = P[1,.5].stretch([8])
duration = var([.5,1,.5,1,.5,1,.5,1,.5,1,.5,1,.5,1,.5])


octrand = random.randint(3,7)
klankrand = random.randint(1,9)

b1 >> bass(baselist, dur=duration)

p1 >> pluck([(0, 5, 9), (0, 3, 5)],oct = [4,5,octrand,octrand], dur=[0.25,1/2,1.5])
p2 >> swell([(0, 5, 9), (0, 3, 5)],oct = [4,5,octrand,octrand], dur=[0.25,1/2,1.5])

p3 >> klank([klankrand,(2,4,6)])

p2.stop()

p3.stop()

d1 >> play("x-o{-[--]}")

d1.stop()
#p2 >> pluck([(0, 2, 4), (0, 3, 5)], dur=0.25)

#p1.stop()
#p2.stop()
#CMajor = [C,D,E,F,G,A,B]

#p1 >> pluck([0, 2, 4], dur=[1, 1/2, 1/2], amp=0.75)

print(SynthDefs)

#p3 >> rave.()

#p3.stop()
