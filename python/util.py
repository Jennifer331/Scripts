# decimal to hexadecimal
def epc_dtoh(raw):
    nums = raw['data']
    epc = ''
    for num in nums:
        epc = epc + ' ' + '%04x' % num
    return epc
