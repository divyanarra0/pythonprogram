p11=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(p11):
    print "yes"
else:
    print "no"
