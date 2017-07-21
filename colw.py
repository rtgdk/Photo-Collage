"""

    Copyright (c) 2017 Yrals
    @author Rohit Lodha, BITS
    
    Portrait Photo Collage Algorithm.
    Default 7 templates are used. More can be added easily in makeframe().
    Photos are arranged into templates and resized. Then templates are arranges in canvas and resized accordingly.
    Then finally pasted into a new image.

"""
from __future__ import print_function
from PIL import Image,ImageFilter,ImageEnhance,ImageColor
import os
import traceback
from time import sleep
import random
import sys
#print(im.format, im.size, im.mode)
#f,e = os.path.splitext('a.png')
#outfile = f + '.thumbnail'
argv = sys.argv[1:]         # list of images
print (argv)
rw,rh,cw,ch,maxh,c0,c1,c2 = 0,0,0,0,0,0,0,0

d = dict()
d["0"] = list()
d["1"] = list()
d["2"] = list()

e = dict()
e["0"] = list()     # 2 square
e["1"] = list()     # 1 verti 2 square
e["2"] = list()     # 1 verti 1 square
e["3"] = list()     # only hori
e["4"] = list()     # only 2 verti
e["5"] = list()     # only 1 verti
e["6"] = list()     # only 1 square
e["7"] = list()     # 1 square 1 verti 1 hori
final = list()

# Divide photos in 7 templates. While loop can be rearranged to create collages randomly or divided into separate function
# and then called randomly.
def makeframe():
    c0 = len(d["0"])
    c1 = len(d["1"])
    c2 = len(d["2"])
    while (c1>=2):
        l = list()
        pop1 = d["1"].pop()
        pop2 = d["1"].pop()
        l.append(pop1)
        l.append(pop2)
        l.append("4")
        final.append(l)
        c1 = c1 - 2
    while (c0>=2):
        l = list()
        pop1 = d["0"].pop()
        pop2 = d["0"].pop()
        l.append(pop1)
        l.append(pop2)
        l.append("0")
        c0 = c0-2
        if (c1>=1):
            pop3 = d["1"].pop()
            l.pop()
            l.append(pop3)
            l.append("1")
            c1 = c1 -1
        final.append(l)
    while (c0>0):
        l = list()
        try:
            pop1 = d["0"].pop()
            l.append(pop1)
            l.append("6")
            if (c1==1):
                pop3 = d["1"].pop()
                l.pop()
                l.append(pop3)
                l.append("2")
                c1 = c1 -1
                if (c2>=1):
                    pop3 = d["2"].pop()
                    l.pop()
                    l.append(pop3)
                    l.append("7")
                    c2 = c2 -1
            final.append(l)
            c0 = c0 -1
        except:
            pass
    while (c2>0):
        l = list()
        try:
            pop1 = d["2"].pop()
            l.append(pop1)
            l.append("3")
            final.append(l)
            c2 = c2 -1
        except:
            pass
    while (c1>0):
        l = list()
        try:
            pop1 = d["1"].pop()
            l.append(pop1)
            l.append("5")
            final.append(l)
            c1 = c1 -1
        except:
            pass
            

# Resizing all types of templates.
def type0(i):
    w1,h1 = i[0][0],i[0][1]
    w2,h2 = i[1][0],i[1][1]
    if (h1 > h2):
        w2 = ((w2*h1)/h2)
        h2 = h1
    else :
        w1 = ((w1*h2)/h1)
        h1 = h2
    i[0][0],i[0][1] = w1,h1
    i[1][0],i[1][1] = w2,h2

def type1(i):
    w1,h1 = i[0][0],i[0][1]
    w2,h2 = i[1][0],i[1][1]
    w3,h3 = i[2][0],i[2][1]
    if (w1 > w2) :
        h2 = ((h2*w1)/w2)
        w2 = w1
    else :
        h1 = ((h1*w2)/w1)
        w1 = w2
    w3 = ((w3*(h1+h2))/h3)
    h3 = h1+h2
    i[0][0],i[0][1] = w1,h1
    i[1][0],i[1][1] = w2,h2
    i[2][0],i[2][1] = w3,h3
def type2(i):
    w1,h1 = i[0][0],i[0][1]
    w2,h2 = i[1][0],i[1][1]
    if (h1 > h2):
        w2 = ((w2*h1)/h2)
        h2 = h1
    else :
        w1 = ((w1*h2)/h1)
        h1 = h2
    i[0][0],i[0][1] = w1,h1
    i[1][0],i[1][1] = w2,h2
def type3(i):
    pass
def type4(i):
    w1,h1 = i[0][0],i[0][1]
    w2,h2 = i[1][0],i[1][1]
    if (h1 > h2):
        w2 = ((w2*h1)/h2)
        h2 = h1
    else :
        w1 = ((w1*h2)/h1)
        h1 = h2
    i[0][0],i[0][1] = w1,h1
    i[1][0],i[1][1] = w2,h2
def type5(i):
    pass
def type6(i):
    pass
def type7(i):
    w1,h1 = i[0][0],i[0][1]  # square
    w2,h2 = i[2][0],i[2][1]  # hori
    w3,h3 = i[1][0],i[1][1]  # verti
    if (w1 > w2) :
        h2 = ((h2*w1)/w2)
        w2 = w1
    else :
        h1 = ((h1*w2)/w1)
        w1 = w2
    w3 = ((w3*(h1+h2))/h3)
    h3 = h1+h2
    print (h1,h2,h3)
    i[0][0],i[0][1] = w1,h1
    i[2][0],i[2][1] = w2,h2
    i[1][0],i[1][1] = w3,h3

# Fix width of templates according to the canvas size
def fixwidth(i,maxw):
    if (i[len(i)-1]=="1"):
        if (i[0][0]+i[2][0] == maxw):
            return
        else :
            w1 = ((maxw * i[0][0])/(i[0][0]+i[2][0]))
            w2 = w1
            w3 = ((maxw * i[2][0])/(i[0][0]+i[2][0]))
            h1 = ((i[0][1]*w1)/i[0][0])
            h2 = ((i[1][1]*w2)/i[1][0])
            h3 = ((i[2][1]*w3)/i[2][0])
            i[0][0],i[0][1] = w1,h1
            i[1][0],i[1][1] = w2,h2
            i[2][0],i[2][1] = w3,h3
            return
    elif (i[len(i)-1]=="7"):
        if (i[0][0]+i[1][0] == maxw):
            return
        else :
            w1 = ((maxw * i[0][0])/(i[0][0]+i[1][0]))
            w2 = w1
            w3 = ((maxw * i[1][0])/(i[0][0]+i[1][0]))
            h1 = ((i[0][1]*w1)/i[0][0])
            h2 = ((i[2][1]*w2)/i[2][0])
            h3 = ((i[1][1]*w3)/i[1][0])
            i[0][0],i[0][1] = w1,h1
            i[2][0],i[2][1] = w2,h2
            i[1][0],i[1][1] = w3,h3
            return
    elif ((i[len(i)-1]=="3") or (i[len(i)-1]=="5") or (i[len(i)-1]=="6")):
        if (i[0][0] == maxw):
            return
        else :
            i[0][1] = ((i[0][1]*maxw)/i[0][0])
            i[0][0] = maxw
            return
    else:
        if (i[0][0]+i[1][0] == maxw):
            return
        else :
            w1 = ((maxw * i[0][0])/(i[0][0]+i[1][0]))
            w2 = ((maxw * i[1][0])/(i[0][0]+i[1][0]))
            h1 = ((i[0][1]*w1)/i[0][0])
            h2 = ((i[1][1]*w2)/i[1][0])
            i[0][0],i[0][1] = w1,h1
            i[1][0],i[1][1] = w2,h2
            return
"""
def fixheight(i,maxh): 
    if (i[len(i)-1]=="1"):
        if (i[2][1] == maxh):
            return
        else :
            w3 = ((maxh * i[2][0])/(i[2][1]))
            h3 = maxh
            h1 = ((maxh * i[0][1])/(i[0][1]+i[1][1]))
            w1 = ((i[0][0]*h1)/(i[0][1]))
            h2 = ((maxh * i[1][1])/(i[0][1]+i[1][1]))
            w2 = ((i[1][0]*h2)/(i[1][1]))
            i[0][0],i[0][1] = w1,h1
            i[1][0],i[1][1] = w2,h2
            i[2][0],i[2][1] = w3,h3
            return
    elif (i[len(i)-1]=="7"):
        if (i[1][1] == maxh):
            return
        else :
            w3 = ((maxh * i[1][0])/(i[1][1]))
            h3 = maxh
            h1 = ((maxh * i[0][1])/(i[0][1]+i[2][1]))
            w1 = ((i[0][0]*h1)/(i[0][1]))
            h2 = ((maxh * i[2][1])/(i[0][1]+i[2][1]))
            w2 = ((i[2][0]*h2)/(i[2][1]))
            i[0][0],i[0][1] = w1,h1
            i[2][0],i[2][1] = w2,h2
            i[1][0],i[1][1] = w3,h3
            return
    elif ((i[len(i)-1]=="3") or (i[len(i)-1]=="5") or (i[len(i)-1]=="6")):
        if (i[0][0] == maxh):
            return
        else :
            i[0][0] = ((i[0][0]*maxh)/i[0][1])
            i[0][1] = maxh
            return
    else:
        if (i[0][1] == maxh):
            return
        else :
            h1 = maxh
            h2 = maxh
            w1 = ((i[0][0]*h1)/(i[0][1]))
            w2 = ((i[1][0]*h2)/(i[1][1]))
            i[0][0],i[0][1] = w1,h1
            i[1][0],i[1][1] = w2,h2
            return
            
"""    

# Divide photos into groups using ratio of width and height.        
def mod(rw,rh,b):
    ratio = float(rw)/float(rh)
    print("ration = " + str(ratio))
    if (ratio>1.5): # hori 
        d["2"].append([rw,rh,b])
        e["3"].append([rw,rh,b])
        return 2
    elif (ratio<0.66): # verti
        d["1"].append([rw,rh,b])
        e["1"].append([rw,rh,b])
        e["4"].append([rw,rh,b])
        e["2"].append([rw,rh,b])
        return 1
    else:           #square
        d["0"].append([rw,rh,b])
        e["0"].append([rw,rh,b])
        e["1"].append([rw,rh,b])
        e["2"].append([rw,rh,b])
        return 0

try:
    #a = Image.open('a.png')
    #a.show()
    #print (a.size)
    #w,h = a.size
    #box = (0,0,w,h)
    lis = list()
    for i in argv:
        #rw = random.randrange(w/10,w/2)
        #rh = random.randrange(h/10,h/2)
        b = Image.open(i)
        rw ,rh= b.size
        print (b.size)
        lis.append([rw,rh,mod(rw,rh,Image.open(i))])
    makeframe()
    for i in lis:
        print (i)
    print("-------")
    for i in final:
        print (i) 
        if (i[len(i)-1]=="0"):
            type0(i)
            print ("simple 2 square")
        elif (i[len(i)-1]=="1"):
            type1(i)
            print ("2 square 1 verti")
        elif (i[len(i)-1]=="2"):
            type2(i)
            print ("1 square 1 verti")
        elif (i[len(i)-1]=="3"):
            type3(i)
            print ("only hori")
        elif (i[len(i)-1]=="4"):
            type4(i)
            print ("only 2 verti")
        elif (i[len(i)-1]=="5"):
            type5(i)
            print ("only 1 verti")
        elif(i[len(i)-1]=="6"):
            type6(i)
            print ("only 1 sqaure")
        elif(i[len(i)-1]=="7"):
            type7(i)
            print ("1 square 1 verti 1 hori")
    maxh = 0
    ch = 0
    maxw = 0
    totalw = 0
    for i in final:
        cw = 0
        for j in range(0,len(i)-1):
            #maxh = i[j][1] if i[j][1] > maxh else maxh
            cw = cw + i[j][0]
        #ch = ch + maxh
        totalw = totalw + cw
        maxw = cw if cw> maxw else maxw
    #print ("here maxw maxh")
    #print (maxw,maxh)
    for i in final:
        fixwidth(i,maxw)
    for i in final:
        maxh = 0
        for j in range(0,len(i)-1):
            maxh = i[j][1] if i[j][1] > maxh else maxh
        ch = ch + maxh
        #ch = maxh if maxh>ch else ch
    #for i in final:
        #fixheight(i,ch)
    print ("MAXW = " + str(maxw) + " Maxh ="+ str(ch))
    b = Image.new("RGBA",(maxw,ch),"#ff0000")
    maxh = 0
    ch = 0
    countim = 0
    for i in final:
        cw=0
        #ch = 0
        maxh = 0
        if (i[len(i)-1]=="1"):
            print("here")
            out = i[0][2].resize((i[0][0],i[0][1]))
            out1 = i[1][2].resize((i[1][0],i[1][1]))
            out3 = i[2][2].resize((i[2][0],i[2][1]))
            print ("Placing at1 " + str(cw) + "," + str(ch))
            b.paste(out,(cw,ch))
            b.paste(out1,(cw,ch+i[0][1]))
            b.paste(out3,(cw+i[0][0],ch))
            maxh = i[2][1]
            cw = cw + i[0][0]+i[2][0]
        if (i[len(i)-1]=="7"):
            print("here")
            print ("Placing at7 " + str(cw) + "," + str(ch))
            out = i[0][2].resize((i[0][0],i[0][1]))
            out1 = i[1][2].resize((i[1][0],i[1][1]))
            out3 = i[2][2].resize((i[2][0],i[2][1]))
            b.paste(out,(cw,ch))
            b.paste(out3,(cw,ch+i[0][1]))
            b.paste(out1,(cw+i[0][0],ch))
            maxh = i[1][1]
            cw = cw + i[0][0]+i[1][0]
        else:
            for j in range(0,len(i)-1):
                out = i[j][2].resize((i[j][0],i[j][1]))
                print ("Placing at " + str(cw) + "," + str(ch))
                maxh = i[j][1] if i[j][1] > maxh else maxh
                b.paste(out,(cw,ch))
                cw = cw + i[j][0]
        ch = ch + maxh
        countim = countim+1
    print (b.size)
    b.show()
    b.save("out.jpg")
    #b.show()   
    # out = a.resize((rw,rh))
    # print (rw,rh)
    # maxh = rh if rh > maxh else maxh
    # if (cw + rw > 1280):
    #     cw = 0
    #     ch = maxh
    # if (ch + rh>720):
    #     pass
    #     #break
    # print ("Placing at " + str(cw) + "," + str(ch))
    # b.paste(out,(cw,ch))
    # cw = cw + rw        
    
    #out2 = a.resize((w/3,h/3))
    
    #b.paste(out2,(0,0))
    #b.paste(out,(w/3,0))
    #b.show()
    #print(b.size)
    #r,g,b,A = (a.split())
    #a = Image.merge("RGBA",(b,g,A,r))
    #out2 = a.filter(ImageFilter.DETAIL)
    #out = out2.resize((w/2,h/2))
    #out3 = a.point(lambda i: i * 0.5)
    #enh = ImageEnhance.Contrast(a)
    #enh.enhance(1.3).show("30 %")
    #r = a.crop(box)
    #r = r.transpose(Image.ROTATE_90)
    #print (out3.size)
    #out3.show()
    #a.paste(r,(0,0,h,w))
    #print (out.size)
    #print (out2.size)
    #out = out.filter(ImageFilter.DETAIL)
    #out.show()
    #out2.show()
    #a.save(outfile)
except:
    traceback.print_exc()
    print ("Cannot convert")
"""
try :
    im = Image.open("giphy.gif")
    im.duration()
    im.show()
    im.seek(1)
    while 1:
        im.seek(im.tell()+1)
        #im.show()
        print("here")
        #sleep(1)
except EOFError:
    traceback.print_exc()
    pass
"""
#im.show()
