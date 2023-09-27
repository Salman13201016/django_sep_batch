b1 = int(input("Enter your number for bangla1: "))
b2 = int(input("Enter your number for bangla2: "))
e1 = int(input("Enter your number for english1: "))
e2 = int(input("Enter your number for english2: "))
gm = int(input("Enter your number for gm: "))
r = int(input("Enter your number for religion: "))
ss = int(input("Enter your number for ss: "))
ict = int(input("Enter your number for ict: "))
phy_s = int(input("Enter your number for phy_s: "))
phy_p = int(input("Enter your number for phy_p: "))
chem_s = int(input("Enter your number for chem_s: "))
chem_p = int(input("Enter your number for chem_p: "))
hm_s = int(input("Enter your number for hm_s: "))
hm_p = int(input("Enter your number for hm_p: "))
bio_s = int(input("Enter your number for bio_s: "))
bio_p = int(input("Enter your number for bio_p: "))

b = (b1+b2)/2
e = (e1+e2)/2
phy = phy_s+phy_p
chem = chem_s+chem_p
hm = hm_s+hm_p
bio = bio_s+bio_p

f1 = 33
f2_s = 24
f2_p = 8

in1 = 0
in2 = 100
in3 = 75
in4 = 25

b_g = 0
e_g = 0
gm_g = 0
hm_g = 0
phy_g = 0
chem_g = 0
bio_g = 0
ss_g = 0
ict_g = 0
r_g = 0


if((b<in1 or b>in2) or (e<in1 or e>in2) or (gm<in1 or gm>in2) or (r<in1 or r>in2) or (ss<in1 or ss>in2) or (ict<in1 or ict>in2) or (phy<in1 or phy>in2) or (chem<in1 or chem>in2) or (hm<in1 or hm>in2) or (bio<in1 or bio>in2) or (phy_s<in1 or phy_s>in3) or (phy_p<in1 or phy_p>in4) or (chem_p<in1 or chem_p>in4) or (chem_s<in1 or chem_s>in3) or (hm_p<in1 or hm_p>in4) or (hm_s<in1 or hm_s>in3) or (bio_p<in1 or bio_p>in4) or (bio_s<in1 or bio_s>in3)):
    print("The number is a invalid number")

# elif(b1<f1 or b2<f1 or e1<f1 or e2<f1 or gm<f1 or religion<f1 or ss<f1 or ict<f1 or hm_s<f2_s or hm_p<f2_p or phy_s<f2_s or phy_p<f2_p or chem_s<f2_s or chem_p<f2_p or bio_s<f2_s or bio_p<f2_p):
#     print("F")
else:
    #bangla
    if(b>0 and b < 33 ):
        print("F")
        b_g = 0.0
    elif(b>32 and b < 40):
        print("D")
        b_g = 1.0
    elif(b>39 and b < 50 ):
        print("C")
        b_g = 2.0
    elif(b>49 and b < 60):
        print("B")
        b_g = 3.0

    elif(b>59 and b < 70 ):
        print("A-")
        b_g = 3.5
    elif(b>69 and b < 80):
        print("A")
        b_g = 4.0
    else:
        print("A+")
        b_g = 5.0

    #english
    if(e>0 and e < 33 ):
        print("F")
        e_g = 0.0
    elif(e>32 and e < 40):
        print("D")
        e_g = 1.0
    elif(e>39 and e < 50 ):
        print("C")
        e_g = 2.0
    elif(e>49 and e < 60):
        print("B")
        e_g = 3.0

    elif(e>59 and e < 70 ):
        print("A-")
        e_g = 3.5
    elif(e>69 and e < 80):
        print("A")
        e_g = 4.0
    else:
        print("A+")
        e_g = 5.0
    
    #general Math
    if(gm>0 and gm < 33 ):
        print("F")
        gm_g = 0.0
    elif(gm>32 and gm < 40):
        print("D")
        gm_g = 1.0
    elif(gm>39 and gm < 50 ):
        print("C")
        gm_g = 2.0
    elif(gm>49 and gm < 60):
        print("B")
        gm_g = 3.0

    elif(gm>59 and gm < 70 ):
        print("A-")
        gm_g = 3.5
    elif(gm>69 and gm < 80):
        print("A")
        gm_g = 4.0
    else:
        print("A+")
        gm_g = 5.0
    
    #hm
    if(hm>0 and hm < 33 ):
        print("F")
        hm_g = 0.0
    elif(hm>32 and hm < 40):
        print("D")
        hm_g = 1.0
    elif(hm>39 and hm < 50 ):
        print("C")
        gm_g = 2.0
    elif(hm>49 and hm < 60):
        print("B")
        hm_g = 3.0

    elif(hm>59 and hm < 70 ):
        print("A-")
        hm_g = 3.5
    elif(hm>69 and hm < 80):
        print("A")
        hm_g = 4.0
    else:
        print("A+")
        hm_g = 5.0

    #phy
    if(phy>0 and phy < 33 ):
        print("F")
        phy_g = 0.0
    elif(phy>32 and phy < 40):
        print("D")
        phy_g = 1.0
    elif(phy>39 and phy < 50 ):
        print("C")
        phy_g = 2.0
    elif(phy>49 and phy < 60):
        print("B")
        phy_g = 3.0

    elif(phy>59 and phy < 70 ):
        print("A-")
        phy_g = 3.5
    elif(phy>69 and phy < 80):
        print("A")
        phy_g = 4.0
    else:
        print("A+")
        phy_g = 5.0



    #Chemistry
    if(chem>0 and chem < 33 ):
        print("F")
        chem_g = 0.0
    elif(chem>32 and chem < 40):
        print("D")
        chem_g = 1.0
    elif(chem>39 and chem < 50 ):
        print("C")
        chem_g = 2.0
    elif(chem>49 and chem < 60):
        print("B")
        chem_g = 3.0

    elif(chem>59 and chem < 70 ):
        print("A-")
        chem_g = 3.5
    elif(chem>69 and chem < 80):
        print("A")
        chem_g = 4.0
    else:
        print("A+")
        chem_g = 5.0

    

    if(ss>0 and ss < 33 ):
        print("F")
        ss_g = 0.0
    elif(ss>32 and ss < 40):
        print("D")
        ss_g = 1.0
    elif(ss>39 and ss < 50 ):
        print("C")
        ss_g = 2.0
    elif(ss>49 and ss < 60):
        print("B")
        ss_g = 3.0

    elif(ss>59 and ss < 70 ):
        print("A-")
        ss_g = 3.5
    elif(ss>69 and ss < 80):
        print("A")
        ss_g = 4.0
    else:
        print("A+")
        ss_g = 5.0

    if(bio>0 and bio < 33 ):
        print("F")
        bio_g = 0.0
    elif(bio>32 and bio < 40):
        print("D")
        bio_g = 1.0
    elif(bio>39 and bio < 50 ):
        print("C")
        bio_g = 2.0
    elif(bio>49 and bio < 60):
        print("B")
        bio_g = 3.0

    elif(bio>59 and bio < 70 ):
        print("A-")
        bio_g = 3.5
    elif(bio>69 and bio < 80):
        print("A")
        bio_g = 4.0
    else:
        print("A+")
        bio_g = 5.0

    

    if(r >0 and r  < 33 ):
        print("F")
        r_g = 0.0
    elif(r >32 and r  < 40):
        print("D")
        r_g = 1.0
    elif(r >39 and r  < 50 ):
        print("C")
        r_g = 2.0
    elif(r >49 and r  < 60):
        print("B")
        r_g = 3.0

    elif(r >59 and r  < 70 ):
        print("A-")
        r_g = 3.5
    elif(r >69 and r  < 80):
        print("A")
        r_g = 4.0
    else:
        print("A+")
        r_g = 5.0

    
    if(ict>0 and ict < 33 ):
        print("F")
        ict_g = 0.0
    elif(ict>32 and ict < 40):
        print("D")
        ict_g = 1.0
    elif(ict>39 and ict < 50 ):
        print("C")
        ict_g = 2.0
    elif(ict>49 and ict < 60):
        print("B")
        ict_g = 3.0

    elif(ict>59 and ict < 70 ):
        print("A-")
        ict_g = 3.5
    elif(ict>69 and ict < 80):
        print("A")
        ict_g = 4.0
    else:
        print("A+")
        ict_g = 5.0


avg_g = (b_g + e_g +gm_g +hm_g+phy_g+chem_g+bio_g+r_g+ss_g+ict_g)/10

print(avg_g)
if(avg_g>=0 and avg_g < 1 ):
    print("F")
elif(avg_g>=1 and avg_g < 2):
    print("D")
elif(avg_g>=2 and avg_g < 3 ):
    print("C")
elif(avg_g>=3 and avg_g < 3.5):
    print("B")
elif(avg_g>=3.5 and avg_g < 4 ):
    print("A-")
elif(avg_g>=4 and avg_g < 5):
    print("A")
else:
    print("A+")

# elif(score>0 and score < 33 ):
#     print("F")
# elif(score>32 and score < 40):
#     print("D")
# elif(score>39 and score < 50 ):
#     print("C")
# elif(score>49 and score < 60):
#     print("B")

# elif(score>59 and score < 70 ):
#     print("A-")
# elif(score>69 and score < 80):
#     print("A")
# else:
#     print("A+")