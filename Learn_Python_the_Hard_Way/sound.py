import winsound
for j in [1,2,3,4,5]:
    for i in [262,294,330,349,392,440,493,523]:
        winsound.Beep(i*j,500)