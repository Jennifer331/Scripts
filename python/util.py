# decimal to hexadecimal
def epc_dtoh(raw):
    nums = raw['data']
    epc = ''
    for num in nums:
        epc = epc + ' ' + '%04x' % num
    return epc.strip()


color_names = ['aqua', 'black', 'blue', 'brown', 'fuchsia', 'darkgrey', 'darkgreen',
               'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
               'darkorchid', 'darkred', 'darksalmon', 'darkviolet',
               'gold', 'green', 'indigo', 'khaki', 'lightblue',
               'lightgreen', 'lightgrey', 'lightpink', 'lime',
               'magenta', 'maroon', 'navy', 'olive', 'orange', 'pink', 'purple',
               'violet', 'red', 'silver', 'yellow', 'cyan', 'darkblue', 'darkcyan']
