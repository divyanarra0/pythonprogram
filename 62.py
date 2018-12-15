p11=raw_input()
"""if all(c in '01' for a in p11):
    print "yes"
else:
    print "No"
    """
if not(p11.translate(None,'01')):
    print "yes"
else:
    print "No"
