import csv

#  So I seem to be able to read in the platcolls just fine
# but inserting it might be a bit trickier.. that will be seen in laoding scripts section

file = 'StarWars.csv'

# Using readlines()
file1 = open(file, 'r')
Lines = file1.readlines()

data = []

i = 0

with open('StarWars.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))

    for row in data:
        # print(len(row))
        # break
        # make question 1 into True and False
        # if row[1] == 'Yes':
        #     row[1] = True
        # elif row[1] == 'No':
        #     row[1] = False

        # # make question 2 into True and False
        # if row[2] == 'Yes':
        #     row[2] = True
        # elif row[2] == 'No':
        #     row[2] = False

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

        if i == 18:
            for j in range(len(row)):
                # if row[j] == '':
                print(row[j])
            # print(len(row))

            # # print(row[0:9], row[19:25], row[25:26], row[53:68], row[79:80], date)
            break
            # data.append([row[0:9], row[19:25], row[25:26],
            #              row[53:68], row[79:80], date])

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
