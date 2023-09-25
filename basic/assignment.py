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

f1 = 32
f2_s = 24
f2_p = 8

in1 = 0
in2 = 100
in3 = 75
in4 = 25


if((b<in1 or b>in2) or (e<in1 or e>in2) or (gm<in1 or gm>in2) or (r<in1 or r>in2) or (ss<in1 or ss>in2) or (ict<in1 or ict>in2) or (phy<in1 or phy>in2) or (chem<in1 or chem>in2) or (h_m<in1 or h_m>in2) or (bio<in1 or bio>in2) or (phy_s<in1 or phy_s>in3) or (phy_p<in1 or phy_p>in4) or (chem_p<in1 or chem_p>in4) or (chem_s<in1 or chem_s>in3) or (hm_p<in1 or hm_p>in4) or (hm_s<in1 or hm_s>in3) or (bio_p<in1 or bio_p>in4) or (bio_s<in1 or bio_s>in3)):
    print("The number is a invalid number")
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