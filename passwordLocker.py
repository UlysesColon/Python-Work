#! python3
# passwrodLocker.py - An insecure password locker program.

 
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             'Wallyworld': 'cagujkihcgbqikhgvbbdfqcioygoiyuwq1giouydfo1g89076564eiyuucgbqkhlc1g89d67gvbikhcjvqbvg1q986g1iuy c1bc98i ycgf-980opoihfc09uqtgc971h90ucqg9u1 qcgh10987chba09iuahcx09811ygth08gfh1p9iuvc g1097rfdh19-087gdhfc-9781vfcyg`-801rfygh89-012'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name\

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
