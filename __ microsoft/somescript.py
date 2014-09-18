
f = open('samplein.txt','rU')
contents = f.read()
thing = []

items = filter(None,contents.split('\n'))
newitems = []
newitems2 = []

for thing in items:
        newitems.append(thing.split(','))

for thing in newitems:
    newitems2.append([thing[0].replace('"','').replace(' ',''),
                      thing[1].replace('"','').replace(' ',''))


