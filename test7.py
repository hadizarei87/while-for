d = [2,4,5,12,8,73]
summatiom = 0
for i in d:
    summatiom = summatiom + i
numberofnumbers = len(d)
avg = summatiom/numberofnumbers
output = {"sum":summatiom,"number of numbers":numberofnumbers,"avarage":avg}
print(output)