from collections import Counter
import csv
f = open('assets/absentee11xx08xx2016.csv')




reader = csv.reader(f)
county_prec_desc = []
#http://stackoverflow.com/questions/16108526/count-how-many-lines-are-in-a-csv-python
num_of_votes = sum(1 for row in reader)
print(num_of_votes)

#combine county_desc and cong_dist_desc
for row in reader:
    county_prec_desc.append(row[22] + ' ' + row[23])
    print(row)

# print(county_prec_desc)
# print(Counter(county_prec_desc).keys())
# print(Counter(county_prec_desc).values())

# print(county_prec_desc)

#http://stackoverflow.com/questions/3428532/how-to-import-a-csv-file-using-python-with-headers-intact-where-first-column-is
# headers = reader.next()
# print(headers)
# column = {}
# for h,idx in headers:
#     column[h].append(idx)
# print(column)

f.close()
