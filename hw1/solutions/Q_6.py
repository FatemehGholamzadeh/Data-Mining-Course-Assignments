from cubes import Workspace, Cell, PointCut
import math
import numpy as np
from decimal import *

# workspace
workspace = Workspace()
workspace.register_default_store("sql", url="mysql://root@localhost:3306/olapdb")
workspace.import_model("model.json")

#browser
browser = workspace.browser("london12")

QA = {"init": 0.0}
QB = {"init": 0.0}
QC = {"init": 0.0}
QD = {"init": 0.0}

sports = ["Archery", "Athletics", "Badminton", "Basketball", "Beach Volleyball", "Canoe Slalom", "Canoe Sprint", "Cycling - BMX","Cycling - Mountain Bike", "Cycling - Road", "Cycling - Track", "Diving", "Equestrian", "Fencing", "Football",
          "Handball","Hockey", "Judo", "Modern Pentathlon", "Rowing", "Sailing", "Shooting", "Swimming", "Table Tennis", "Tennis","Triathlon","Volleyball", "Water Polo", "Weightlifting", "Wrestling"]
continents = ["Africa", "Asia", "Europe", "North America", "Oceania", "Other", "South America"]
genders = ['M', 'F']
age = ['A', 'B', 'C', 'D']

def STD(m_sum, avg):
    me = 0
    for y in m_sum:
        me += abs(float(y) - avg) ** 2

    std = math.sqrt(me / len(m_sum))
    return std

############################## part a ##########################################

def part_A(ans, QString):
    max_CV = list(QA.values())
    ms= 0
    sumOfMedals = []
    counts = 0
    for row in ans:
        sumOfMedals.append(row["Medals_sum"])
        ms+= row["Medals_sum"]
        counts += 1

    if counts >= 100 and ms>= 20:
        avg = float(ms/ counts)
        std = STD(sumOfMedals, avg)
        cv = std / avg

        if cv >= max_CV[0]:
            QA.clear()
            QA[QString] = cv
############################## part b ##########################################

def part_B(ans, QString):
    max_b = list(QB.values())
    ms= 0
    counts = 0
    for row in ans:
        ms+= row["Medals_sum"]
        counts += 1

    if counts >= 10:
        ssi = ms/ counts
        if ssi >= max_b[0]:
            QB.clear()
            QB[QString] = ssi

############################## part c ##########################################

def part_C(ans, QString):
    max_medal = list(QC.values())
    ms= 0
    b = 0
    silver = 0
    for row in ans:
        ms+= row["Medals_sum"]
        b += row["bronze_sum"]
        silver += row["silver_sum"]

    if silver + b >= (9 / 10) * my_sum:
        if ms>= max_medal[0]:
            QC.clear()
            QC[QString] = my_sum

############################## part d ##########################################

def part_D(ans, QString):
    max_medal_d = list(QD.values())
    my_s = 0
    gold = 0
    for row in ans:
        my_s += row["Medals_sum"]
        gold += row["gold_sum"]

    if gold >= (1 / 2) * my_s:
        if my_s >= max_medal_d[0]:
            QD.clear()
            QD[QString] = my_s


def final_Q(ans, QString):
    part_A(ans, QString)
    part_B(ans, QString)
    part_C(ans, QString)
    part_D(ans, QString)




##################################################### drill down #####################################################

print("we are drilling down here : ")


answer = browser.aggregate(drilldown=[])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = []')
answer = browser.aggregate(drilldown=["continent"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent')
answer = browser.aggregate(drilldown=["gender", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = gender,sport')
answer = browser.aggregate(drilldown=["continent", "agegroup", "gender"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent,agegroup,gender')
answer = browser.aggregate(drilldown=["agegroup"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = agegroup')
answer = browser.aggregate(drilldown=["gender"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = gender')
answer = browser.aggregate(drilldown=["sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = sport')
answer = browser.aggregate(drilldown=["continent", "agegroup", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent,agegroup,sport')
answer = browser.aggregate(drilldown=["agegroup", "gender", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = agegroup,gender,sport')
answer = browser.aggregate(drilldown=["continent", "gender", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent,gender,sport')
answer = browser.aggregate(drilldown=["continent", "agegroup", "gender", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down =continent,gender,sport,agegroup ')
answer = browser.aggregate(drilldown=["continent", "agegroup"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent,agegroup')
answer = browser.aggregate(drilldown=["continent", "gender"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent,gender')
answer = browser.aggregate(drilldown=["continent", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = continent,sport')
answer = browser.aggregate(drilldown=["agegroup", "gender"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = agegroup,gender')
answer = browser.aggregate(drilldown=["agegroup", "sport"])
final_Q(answer, 'cut = [] ' + '\n' + 'drill down = agegroup,sport')

print("we are doing slice here : ")
##################################################### slice #####################################################
################ slice on age
for a in age:
    cut = PointCut("agegroup", [a])
    cell = Cell(browser.cube, cuts=[cut])
    answer = browser.aggregate(cell, drilldown=["gender"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = gender')
    answer = browser.aggregate(cell, drilldown=["sport"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = sport')
    answer = browser.aggregate(cell, drilldown=["gender", "sport", "continent"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = gender,continent,sport')
    answer = browser.aggregate(cell, drilldown=[])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down =[]')
    answer = browser.aggregate(cell, drilldown=["gender", "continent"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = gender,continent')
    answer = browser.aggregate(cell, drilldown=["gender", "sport"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = gender,sport')
    answer = browser.aggregate(cell, drilldown=["continent", "sport"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = continent,sport')
    answer = browser.aggregate(cell, drilldown=["continent"])
    final_Q(answer, 'cut =' + a + '\n' + 'drill down = continent')


########################################## slice on continents
for c in continents:
    cut = PointCut("continent", [c])
    cell = Cell(browser.cube, cuts=[cut])
    answer = browser.aggregate(cell, drilldown=["gender", "agegroup"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = gender,agegroup')
    answer = browser.aggregate(cell, drilldown=["agegroup", "sport"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = agegroup,sport')
    answer = browser.aggregate(cell, drilldown=["agegroup"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = agegroup')
    answer = browser.aggregate(cell, drilldown=["gender"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = gender')
    answer = browser.aggregate(cell, drilldown=["gender", "sport"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = gender,sport')
    answer = browser.aggregate(cell, drilldown=["sport"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = sport')
    answer = browser.aggregate(cell, drilldown=["gender", "sport", "agegroup"])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = gender,sport,agegroup')
    answer = browser.aggregate(cell, drilldown=[])
    final_Q(answer, 'cut =' + c + '\n' + 'drill down = []')

# ################################### # slice on sports
for s in sports:
    cut = PointCut("sport", [s])
    cell = Cell(browser.cube, cuts=[cut])
    answer = browser.aggregate(cell, drilldown=["gender", "agegroup"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = gender,agegroup')
    answer = browser.aggregate(cell, drilldown=["gender", "continent"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = gender,continent')
    answer = browser.aggregate(cell, drilldown=["continent"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = continent')
    answer = browser.aggregate(cell, drilldown=["gender", "continent", "agegroup"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = gender,continent,agegroup')
    answer = browser.aggregate(cell, drilldown=["agegroup", "continent"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = agegroup,continent')
    answer = browser.aggregate(cell, drilldown=["agegroup"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = agegroup')
    answer = browser.aggregate(cell, drilldown=["gender"])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = gender,continent')
    answer = browser.aggregate(cell, drilldown=[])
    final_Q(answer, 'cut =' + s + '\n' + 'drill down = []')

################################### slice on genders
for g in genders:
    cut = PointCut("gender", [g])
    cell = Cell(browser.cube, cuts=[cut])
    answer = browser.aggregate(cell, drilldown=["agegroup", "continent"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = agegroup,continent')
    answer = browser.aggregate(cell, drilldown=["agegroup"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = agegroup')
    answer = browser.aggregate(cell, drilldown=["sport"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = sport')
    answer = browser.aggregate(cell, drilldown=["continent"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = continent')
    answer = browser.aggregate(cell, drilldown=["sport", "agegroup"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = sport,agegroup')
    answer = browser.aggregate(cell, drilldown=["sport", "continent"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = sport,continent')
    answer = browser.aggregate(cell, drilldown=["sport", "continent", "agegroup"])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = sport,continent,agegroup')
    answer = browser.aggregate(cell, drilldown=[])
    final_Q(answer, 'cut =' + g + '\n' + 'drill down = []')


############################################ dicing with 2 attributes #############################################
print("we are dicing with 2 attributes here : ")

################ dice on genders and sports
for item11 in age:
    for item12 in sports:
        cut1 = PointCut("agegroup", [item11])
        cut2 = PointCut("sport", [item12])
        cell = Cell(browser.cube, cuts=[cut1, cut2])
        answer = browser.aggregate(cell, drilldown=["continent"])
        final_Q(answer, 'cut = agegroup,sport' + '\n' + 'drill down = continent')
        answer = browser.aggregate(cell, drilldown=["gender"])
        final_Q(answer, 'cut = agegroup,sport' + '\n' + 'drill down = gender')
        answer = browser.aggregate(cell, drilldown=["gender", "continent"])
        final_Q(answer, 'cut = agegroup,sport' + '\n' + 'drill down = gender,continent')
        answer = browser.aggregate(cell, drilldown=[])
        final_Q(answer, 'cut = agegroup,sport' + '\n' + 'drill down = []')


#########################dice on genders and age
for item7 in genders:
    for item8 in age:
        cut1 = PointCut("gender", [item7])
        cut2 = PointCut("agegroup", [item8])
        cell = Cell(browser.cube, cuts=[cut1, cut2])
        answer = browser.aggregate(cell, drilldown=["continent"])
        final_Q(answer, 'cut = gender,agegroup' + '\n' + 'drill down = continent')
        answer = browser.aggregate(cell, drilldown=["sport"])
        final_Q(answer, 'cut = gender,agegroup' + '\n' + 'drill down = sport')
        answer = browser.aggregate(cell, drilldown=["sport", "continent"])
        final_Q(answer, 'cut = gender,agegroup' + '\n' + 'drill down = sport,continent')
        answer = browser.aggregate(cell, drilldown=[])
        final_Q(answer, 'cut = gender,agegroup' + '\n' + 'drill down = []')

################# dice on continents and sports
for item3 in continents:
    for item4 in sports:
        cut1 = PointCut("continent", [item3])
        cut2 = PointCut("sport", [item4])
        cell = Cell(browser.cube, cuts=[cut1, cut2])
        answer = browser.aggregate(cell, drilldown=["gender"])
        final_Q(answer, 'cut = continent,sport' + '\n' + 'drill down = gender')
        answer = browser.aggregate(cell, drilldown=["agegroup"])
        final_Q(answer, 'cut = continent,sport' + '\n' + 'drill down = agegroup')
        answer = browser.aggregate(cell, drilldown=["agegroup", "gender"])
        final_Q(answer, 'cut = continent,sport' + '\n' + 'drill down = agegroup,gender')
        answer = browser.aggregate(cell, drilldown=[])
        final_Q(answer, 'cut = continent,sport' + '\n' + 'drill down = []')

############### dice on continents and age
for item5 in continents:
    for item6 in age:
        cut1 = PointCut("continent", [item5])
        cut2 = PointCut("agegroup", [item6])
        cell = Cell(browser.cube, cuts=[cut1, cut2])
        answer = browser.aggregate(cell, drilldown=["gender"])
        final_Q(answer, 'cut = continent,agegroup' + '\n' + 'drill down = gender')
        answer = browser.aggregate(cell, drilldown=["sport"])
        final_Q(answer, 'cut = continent,agegroup' + '\n' + 'drill down = sport')
        answer = browser.aggregate(cell, drilldown=["sport", "gender"])
        final_Q(answer, 'cut = continent,sport' + '\n' + 'drill down = agegroup,gender')
        answer = browser.aggregate(cell, drilldown=[])
        final_Q(answer, 'cut = continent,agegroup' + '\n' + 'drill down = []')




#################### dice on continent and gender
for item1 in continents:
    for item2 in genders:
        cut1 = PointCut("continent", [item1])
        cut2 = PointCut("gender", [item2])
        cell = Cell(browser.cube, cuts=[cut1, cut2])
        answer = browser.aggregate(cell, drilldown=["sport"])
        final_Q(answer, 'cut = continent,gender' + '\n' + 'drill down = sport')
        answer = browser.aggregate(cell, drilldown=["agegroup"])
        final_Q(answer, 'cut = continent,gender' + '\n' + 'drill down = agegroup')
        answer = browser.aggregate(cell, drilldown=["agegroup", "sport"])
        final_Q(answer, 'cut = continent,gender' + '\n' + 'drill down = agegroup, sport')
        answer = browser.aggregate(cell, drilldown=[])
        final_Q(answer, 'cut = continent,gender' + '\n' + 'drill down = []')


###############dice on genders and sports
for item9 in genders:
    for item10 in sports:
        cut1 = PointCut("gender", [item9])
        cut2 = PointCut("sport", [item10])
        cell = Cell(browser.cube, cuts=[cut1, cut2])
        answer = browser.aggregate(cell, drilldown=["continent"])
        final_Q(answer, 'cut = gender,sport' + '\n' + 'drill down = continent')
        answer = browser.aggregate(cell, drilldown=["agegroup"])
        final_Q(answer, 'cut = gender,sport' + '\n' + 'drill down = agegroup')
        answer = browser.aggregate(cell, drilldown=["agegroup", "continent"])
        final_Q(answer, 'cut = gender,sport' + '\n' + 'drill down = agegroup,continent')
        answer = browser.aggregate(cell, drilldown=[])
        final_Q(answer, 'cut = gender,sport' + '\n' + 'drill down = []')


################################################ dicing with 3 attributes##################################################
print("we are dicing with 3 attributes here : ")

for u in sports:
    for o in genders:
        for t in continents:
            cut = PointCut("sport", [u])
            cut1 = PointCut("gender", [o])
            cut2 = PointCut("continent", [t])
            cell = Cell(browser.cube, cuts=[cut, cut1, cut2])
            answer = browser.aggregate(cell, drilldown=["agegroup"])
            final_Q(answer, 'cut = continent,gender,sport' + '\n' + 'drill down = agegroup')
            answer = browser.aggregate(cell)
            final_Q(answer, 'cut = continent,gender,sport' + '\n' + 'drill down = []')


for k in age:
    for l in continents:
        for x in genders:
            cut = PointCut("agegroup", [k])
            cut1 = PointCut("continent", [l])
            cut2 = PointCut("gender", [x])
            cell = Cell(browser.cube, cuts=[cut, cut1, cut2])
            answer = browser.aggregate(cell, drilldown=["sport"])
            final_Q(answer, 'cut = agegroup,gender,continent' + '\n' + 'drill down = sport')
            answer = browser.aggregate(cell)
            final_Q(answer, 'cut = agegroup,gender,continent' + '\n' + 'drill down = []')

for q in genders:
    for e in age:
        for r in sports:
            cut = PointCut("sport", [r])
            cut1 = PointCut("agegroup", [e])
            cut2 = PointCut("gender", [q])
            cell = Cell(browser.cube, cuts=[cut, cut1, cut2])
            answer = browser.aggregate(cell, drilldown=["continent"])
            final_Q(answer, 'cut = agegroup,gender,sport' + '\n' + 'drill down = continent')
            answer = browser.aggregate(cell)
            final_Q(answer, 'cut = agegroup,gender,sport' + '\n' + 'drill down = []')




for ss in sports:
    for aa in age:
        for cc in continents:
            cut = PointCut("sport", [ss])
            cut1 = PointCut("agegroup", aa)
            cut2 = PointCut("continent", [cc])
            cell = Cell(browser.cube, cuts=[cut, cut1, cut2])
            answer = browser.aggregate(cell, drilldown=["gender"])
            final_Q(answer, 'cut = agegroup,sport,continent' + '\n' + 'drill down = gender')
            answer = browser.aggregate(cell, drilldown=[])
            final_Q(answer, 'cut = agegroup,sport,continent' + '\n' + 'drill down = []')

print("we are dicing with 4 attributes here : ")
for si in sports:
    for gi in genders:
        for ci in continents:
            for ai in age:
                cut = PointCut("sport", [si])
                cut1 = PointCut("gender", [gi])
                cut2 = PointCut("continent", [ci])
                cut3 = PointCut("agegroup", [ai])
                cell = Cell(browser.cube, cuts=[cut, cut1, cut2, cut3])
                answer = browser.aggregate(cell)
                final_Q(answer, 'cut = continent,gender,sport,agegroup' + '\n' + 'drill down = []')
                if ci == 'North America' and ai == 'C' and si == 'Swimming' and gi == 'M':
                    print(QB.values())



print(QA.keys())
print(QB.keys())
print(QC.keys())
print(QD.keys())
