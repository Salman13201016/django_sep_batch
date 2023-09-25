cake1 = "bf"
cake2 = "vc"
cake3 = "cc"

#material cost, #transportation #utility #staff #space  
mc1 = 160 
mc2 = 170
mc3 = 180

t_c = 50

tc_mc1 = mc1+ t_c
tc_mc2 = mc2+ t_c
tc_mc3 = mc3+ t_c


uc1 = (tc_mc1 * 5)/100
uc2 = (tc_mc2 * 5)/100
uc3 = (tc_mc3 * 5)/100

st_c = 60

s_c = 50

total_c1 = tc_mc1 + uc1 + s_c + st_c
total_c2 = tc_mc2 + uc2 + s_c + st_c
total_c3 = tc_mc3 + uc3 + s_c + st_c

print(total_c1,total_c2,total_c3)