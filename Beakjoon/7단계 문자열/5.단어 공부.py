words = input().upper()
wlist = list(set(words))

nwlist = []
for i in wlist:
    cnt = words.count(i)
    nwlist.append(cnt)

if nwlist.count(max(nwlist)) > 1:
    print("?")
else:
    print(wlist[nwlist.index(max(nwlist))])