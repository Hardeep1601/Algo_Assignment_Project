# import p2 from prob2
from prob2 import p2

temp=p2()
pos=temp.getPositive()
neg=temp.getNegative()

totalPositiveCitylink = pos[0] + pos[1] + pos[2]
totalPositivePoslaju = pos[3] + pos[4] + pos[5]
totalPositiveGdex = pos[6] + pos[7] + pos[8]
totalPositiveJnt = pos[9] + pos[10] + pos[11]
totalPositiveDhl = pos[12] + pos[13] + pos[14]

totalNegativeCitylink = neg[0] + neg[1] + neg[2]
totalNegativePoslaju = neg[3] + neg[4] + neg[5]
totalNegativeGdex = neg[6] + neg[7] + neg[8]
totalNegativeJnt = neg[9] + neg[10] + neg[11]
totalNegativeDhl = neg[12] + neg[13] + neg[14]

import plotly.graph_objects as go
couriers=['Citylink', 'Poslaju', 'GDEX', 'JandT', 'DHL']

fig = go.Figure(data=[
    go.Bar(name='Positive words', x=couriers, y=[totalPositiveCitylink, totalPositivePoslaju, totalPositiveGdex, totalPositiveJnt, totalPositiveDhl]),
    go.Bar(name='Negative Words', x=couriers, y=[totalNegativeCitylink, totalNegativePoslaju, totalNegativeGdex, totalNegativeJnt, totalNegativeDhl])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()

ct = totalPositiveCitylink - totalNegativeCitylink
pl = totalPositivePoslaju - totalNegativePoslaju
gd = totalPositiveGdex - totalNegativeGdex
jn = totalPositiveJnt - totalNegativeJnt
dh = totalPositiveDhl - totalNegativeDhl

courierlist = [ct, pl, gd, jn, dh]
# print(courierlist)
def findBestSentiment():
    if ct > pl and ct > gd and ct > jn and ct > dh:
        return print('Citylink has the best sentiment')
    elif pl > ct and pl > gd and pl > jn and pl > dh:
        return print('Poslaju has the best sentiment')
    elif gd > ct and gd > pl and gd > jn and gd > dh:
        return print('GDEX has the best sentiment')
    elif jn > ct and jn > pl and jn > gd and jn > dh:
        return print('JandT has the best sentiment')
    elif dh > ct and dh > pl and dh > gd and dh > jn:
        return print('DHL has the best sentiment')

findBestSentiment()



