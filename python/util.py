# decimal to hexadecimal
def epc_dtoh(raw):
    nums = raw['data']
    epc = ''
    for num in nums:
        epc = epc + ' ' + '%04x' % num
    return epc


color_names = ['aqua', 'azure', 'beige', 'black', 'blue', 'brown',
               'cyan', 'darkblue', 'darkcyan', 'darkgrey', 'darkgreen',
               'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
               'darkorchid', 'darkred', 'darksalmon', 'darkviolet', 'fuchsia',
               'gold', 'green', 'indigo', 'khaki', 'lightblue', 'lightcyan',
               'lightgreen', 'lightgrey', 'lightpink', 'lightyellow', 'lime',
               'magenta', 'maroon', 'navy', 'olive', 'orange', 'pink', 'purple',
               'violet', 'red', 'silver', 'white', 'yellow']
