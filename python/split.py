x = '914750 914250 924750 909750 905750 927250 913250 913750 922750 918250 920250 926750 916750 917250 909250 907750 908750 917750 910250 915750 903750 920750 911750 902750 922250 906250 921250 919250 904250 903250 925750 912250 925250 926250 905250 912750 915250 921750 918750 911250 923250 916250 906750 924250 904750 907250 919750 908250 910750 923750'
import re
ss = re.split('\s+', x)
ii = list(map(int, ss))
ii = [I / 1000 for I in ii]

with open('d:\\Atom\\test.txt', 'w') as f:
    for i in ii:
        f.write('%s, ' % i)