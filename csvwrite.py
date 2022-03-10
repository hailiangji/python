import csv
def write_csv():
    path  = "bb.csv"
    with open(path,'a+') as f:
        csv_write = csv.writer(f)
        data_row = ["1","2","哈哈"]
        csv_write.writerow(data_row)
    f.close()

write_csv()