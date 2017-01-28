import csv

FILENAME = "sales.csv"
OUTFILE = "sales_output.csv"
# file_pointer = open(FILENAME, "r")
# data = file_pointer.readlines()
# print(data)
# file_pointer.close()

#*************************
class House:
    def __init__(self, br=0, sqft=0, price=0.0):
        self.br = br
        self.sqft = sqft
        self.price = price

    def __str__(self):
        return "{} bedroom, {} sqft, ${}".format(self.br, self.sqft, self.price)

out_pointer = open(OUTFILE, "w")
with open(FILENAME, "r") as my_file:
    csv_pointer = csv.reader(my_file)
    header = ""
    count = 0
    three_br_total_price = 0.0
    three_br_total_area = 0
    #for row in my_file:
    for row in csv_pointer:
        if count != 0:
            #print(row)
            house = House(int(row[4]), int(row[6]), float(row[9]))
            if house.br == 3:
                three_br_total_area += house.sqft
                three_br_total_price += house.price
            print(house)
        if count == 0:
            header = row
        count += 1
    print("3 bedder psf = ${:.2f}".format(float(three_br_total_price/three_br_total_area)))
    print("Total record = {}".format(count-1), file=out_pointer)
    print(header)
out_pointer.close()