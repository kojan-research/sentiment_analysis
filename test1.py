from konlpy.tag import Kkma
kkma = Kkma()
sent = []
x = kkma.pos("음식이 맛도 없고 딱딱해서 짜증나고 끔찍했어요.")

for i in range(len(x)):
    if x[i][1] == "VA":
        sent.append(x[i][0]+"다")
    if x[i][1] == "VV":
        sent.append(x[i][0]+"다")
    if x[i][1] == "XR" and x[i + 1][1] == "XSV":
        sent.append(x[i][0]+x[i + 1][0]+"다")
print(x)
for i in sent: print(i)