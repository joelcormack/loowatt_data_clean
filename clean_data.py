"""
CSV format
id,ts,event,unit,man_fwd,man_back,main_flush,main_bag_used,second_flush,
second_bag_used,bag_used,bag_left,blockages,resets,fault

"""
import csv


with open('test2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0

    for row in readCSV:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            with open('output.csv', 'a') as output_file:
                output_writer = csv.writer(
                    output_file,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                output_writer.writerow(row)
            line_count += 1
        elif line_count == 1:
            previous_row = next(readCSV)
            line_count += 1
        else:
            if row[9] != previous_row[9]:
                
                #print line to file if it's not a repeat of the previous line
                with open('output.csv', 'a') as output_file:
                    output_writer = csv.writer(
                        output_file,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
                    output_writer.writerow(row)

            line_count += 1
            previous_row = row
    print(f'Processed {line_count} lines.')
