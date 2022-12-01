
lista = []




file = open("data.txt", "r")
tec = []
for line in file:
    tec = line.split(",")
for i in file:
    tec.append(file.readlines())
for index, element in enumerate(tec):
    tec[index] = element.upper().strip(" ")

exp_years = 0
counter = 0
unique_tecnologies = []
statistics = []
for index, element in enumerate(tec):
    

    if element.isnumeric():

        
        exp_years += int(tec.pop(index))
        counter += 1

    elif element == "":
        tec.pop(index)
        

    else:

        if element not in unique_tecnologies:

            unique_tecnologies.append(element)



for element in unique_tecnologies:
    
    #print(element)
    statistics.append(tec.count(element))
        


for i in unique_tecnologies:
    print(i)

#print(tec.count(unique_tecnologies[0]))
print(statistics)