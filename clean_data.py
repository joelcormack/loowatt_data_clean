"""
CSV format
id,ts,event,unit,man_fwd,man_back,main_flush,main_bag_used,second_flush,
second_bag_used,bag_used,bag_left,blockages,resets,fault

"""
import csv
import re
import arrow #great time and date module
import sys
from datetime import datetime
from pytz import timezone

in_file = sys.argv[1]
out_file = sys.argv[2]
regex = re.compile(r'\+\d*')


with open(in_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    successful_rows = 0
    duplicates = 0

    for row in readCSV:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            with open(out_file, 'w') as output_file:
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
                timestamp_tz = row[1]
                if re.search(regex, timestamp_tz):
                    ts = arrow.get(timestamp_tz)
                    ts = ts.shift(hours=+1)
                    row[1] = ts.format('YYYY-MM-DD HH:mm:ss')
                #print line to file if it's not a repeat of the previous line
                with open(out_file, 'a') as output_file:
                    output_writer = csv.writer(
                        output_file,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
                    output_writer.writerow(row)
                successful_rows += 1
            else:
                duplicates += 1

            line_count += 1
            previous_row = row
    print(f'Processed {line_count} lines.')
    print(f'New file contains {successful_rows} lines.')
    print(f'There were {duplicates} duplicates.')
