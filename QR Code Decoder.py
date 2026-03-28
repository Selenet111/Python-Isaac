QR1 = (["110011", 
           "110011", 
           "000000", 
           "000000", 
           "110000", 
           "110001"])
QR2 = (["100011", 
           "000011", 
           "000000", 
           "000000", 
           "110011", 
           "110011"])
QR3 = (["110011", 
           "111111", 
           "010000", 
           "110000", 
           "110011", 
           "110100"])
QR4 = (["011011", 
           "101011", 
           "101000", 
           "100010", 
           "110011", 
           "111011"])
QR5 = (["111100", 
           "110001", 
           "100011", 
           "001101", 
           "110011", 
           "110011"])

def check_QR(QR):
    corners = []
    corners.append(QR[0][0])
    corners.append(QR[0][1])
    corners.append(QR[1][0])
    corners.append(QR[1][1])
    corners.append(QR[0][4])
    corners.append(QR[0][5])
    corners.append(QR[1][4])
    corners.append(QR[1][5])
    corners.append(QR[4][0])
    corners.append(QR[4][1])
    corners.append(QR[5][0])
    corners.append(QR[5][1])

    if corners.count('1') == 12:
        return True
    return False

def rotate_QR(QR):
    # NEWQR = [[QR[0].split], [QR[1].split], [QR[2].split], [QR[3].split], [QR[4].split], [QR[5].split]]



    for x in NEWQR:
        for y in x:
             if QR.index(y) == 5:
                 NEWQR[1].append(y)
    print(NEWQR[0])



rotate_QR(QR1)