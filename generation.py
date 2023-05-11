
import json
 
data = {"combinations": [],
        "combinations_name_range":{}}
combinations_name_range ={}
combinations = []
#Para
combinations_name_range["Пара"] = [len(combinations)]
for i in range(1,7):
    combinations.append((i,i))
combinations_name_range["Пара"].append(len(combinations))


#Dve pari
combinations_name_range["Дві пари"] = [len(combinations)]
for i in range(1,7):
    for j in range(1,7):
        if i < j : combinations.append((i,i,j,j))
combinations_name_range["Дві пари"].append(len(combinations))


#Set
combinations_name_range["Сет"] = [len(combinations)]
for i in range(1,7):
    combinations.append((i,i,i))
combinations_name_range["Сет"].append(len(combinations))


#Maliy strit
combinations_name_range["Малий стрейт"] = [len(combinations)]
combinations.append((1,2,3,4,5))


#Bolshoi strit
combinations_name_range["Великий стрейт"] = [len(combinations)]
combinations.append((2,3,4,5,6))



#Full house
combinations_name_range["Фулхаус"] = [len(combinations)]
for i in range(1,7):
    for j in range(1,7):
        if i != j : combinations.append(sorted((i,i,i,j,j)))
combinations_name_range["Фулхаус"].append(len(combinations))

#Kare
combinations_name_range["Каре"] = [len(combinations)]
for i in range(1,7):
    combinations.append((i,i,i,i))
combinations_name_range["Каре"].append(len(combinations))

#Poker
combinations_name_range["Покер"] = [len(combinations)]
for i in range(1,7):
    combinations.append((i,i,i,i,i))
combinations_name_range["Покер"].append(len(combinations))

data["combinations_name_range"]=combinations_name_range
data['combinations'] = combinations
with open('data.json', 'w') as f:
    json.dump(data, f, indent='\t')