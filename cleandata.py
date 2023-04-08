import csv

#  So I seem to be able to read in the platcolls just fine
# but inserting it might be a bit trickier.. that will be seen in laoding scripts section

file = 'StarWars.csv'

# Using readlines()
file1 = open(file, 'r')
Lines = file1.readlines()

outdata = []

i = 0

with open('StarWars.csv', mode='r') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))

    for row in data:
        # if len(row) != 38:
        #     print(len(row))

        # turns seen and fan of into True, False
        for k in range(1, 3):
            if row[k] == 'Yes':
                row[k] = True
            elif row[k] == 'No':
                row[k] = False

        # turns seen individual movie into True, False
        for k in range(3, 9):
            if len(row[k]) > 0:
                # print(k)
                row[k] = True
            else:
                row[k] = False

        # shortens likeabilty of character
        for k in range(15, 29):
            if row[k] == "Very favorably":
                row[k] = 'vf'
            elif row[k] == "Somewhat favorably":
                row[k] = 'sf'
            elif row[k] == "Neither favorably nor unfavorably (neutral)":
                row[k] = 'n'
            elif row[k] == "Somewhat unfavorably":
                row[k] = 'su'
            elif row[k] == "Very unfavorably":
                row[k] = 'vu'
            elif row[k] == "Unfamiliar (N/A)":
                row[k] = 'u'

        # shortens who shot first
        if row[29] == "Han":
            row[29] = 'H'
        elif row[29] == "Greedo":
            row[29] = 'G'
        elif row[29] == "I don't understand this question":
            row[29] = 'DU'

        # shortens Income
        if row[35] == "$0 - $24,999":
            row[35] = 'IL1'
        elif row[35] == "$25,000 - $49,999":
            row[35] = 'IL2'
        elif row[35] == "$50,000 - $99,999":
            row[35] = 'IL3'
        elif row[35] == "$100,000 - $149,999":
            row[35] = 'IL4'
        elif row[35] == "$150,000+":
            row[35] = 'IL5'

        # shortens Education
        if row[36] == "Less than high school degree":
            row[36] = 'E1'
        elif row[36] == "High school degree":
            row[36] = 'E2'
        elif row[36] == "Some college or Associate degree":
            row[36] = 'E3'
        elif row[36] == "Bachelor degree":
            row[36] = 'E4'
        elif row[36] == "Graduate degree":
            row[36] = 'E5'

        # if i == 1187:
        #     for j in range(len(row)):
        #         print(row[j])
        #     break
        outdata.append([row])

        i += 1
# # so seems to work would put in a temp table then switch to

# fields = ["cusip", "poolname", "indicator", "faceinplatinum", "active", "date"]

# with open('data/output/platcolls.cvs', 'w', newline='') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(fields)

#     # writing the data rows
#     csvwriter.writerows(data)

print(outdata[-1])
