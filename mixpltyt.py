age_data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 
            25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
## Mencari Mean (rata-rata)
length_data = len(age_data)
sum_data = sum(age_data)/length_data
print("Rata-rata umur adalah : " +str(round(sum_data))+"\n")

## Mencari Modus (paling sering muncul)
def mode(i):
    angkaterbanyak = 0
    modes = []
    for x in i:
        if x in modes:
            continue
        count = i.count(x)
        if count > angkaterbanyak:
            del modes[:]
            modes.append(x)
            angkaterbanyak = count
        elif count == angkaterbanyak:
            modes.append(x)
    return modes
print("Modus dari data umur adalah : "+str(mode(age_data))+"\n")
## Mencari nilai maksimum dan minimum
def maks_min (x):
    minimum = maksimum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maksimum:
                maksimum = i
    return (minimum, maksimum)
print("Nilai maksimum dan minimum adalah : "+str(maks_min(age_data))+"\n")

## Mencari Quartil 1, Quartil 2, dan Quartil 3
def rata_rata(x):
    urut = sorted(x)
    mid = len(x)//2
    if len(x) % 2:
        return urut[mid]
    else:
        med = (urut[mid]+urut[mid-1])/2
        return med
print("Rata-rata dari data umur (Q2) adalah : "+str(rata_rata(age_data)))

def quartile_1(x):
    return sorted(x)[int(len(x) * .25)]
print("Kuartil 1 dari data umur adalah : "+ str(quartile_1(age_data)))

def quartile_3(x):
    return sorted(x)[int(len(x) * .75)]
print("Kuartil 3 dari data umur adalah : "+ str(quartile_3(age_data))+"\n")


## Mencari Interquartile Range (IQR)
iqr_age = quartile_3(age_data) - quartile_1(age_data)
print ("Interquartile Range : " +str(iqr_age)+"\n")
low_bound = quartile_1(age_data) - (1.5 * iqr_age)
high_bound = quartile_3(age_data) + (1.5 * iqr_age)

print("Batas bawah dan atas :"+str(low_bound)+",",(high_bound))


    