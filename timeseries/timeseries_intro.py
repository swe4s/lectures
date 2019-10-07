import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime


class ImportData:
    def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._roundtime = []
        self._roundtimeStr = []
        with open(data_csv, "r") as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                try:
                    self._time.append(dateutil.parser.parse(row['time']))
                except ValueError:
                    print('Bad input format for time')
                    print(row['time'])
                self._value.append(row['value'])
            fhandle.close()

        self.roundTime(5)

    def linear_search_value(self, key_time):
        for i in range(len(self._roundtimeStr)):
            curr =  self._roundtimeStr[i]
            if key_time == curr:
                return self._value[i]
        print('invalid time')
        return -1

    def roundTime(self, resolution):
        for times in self._time:
            minminus = datetime.timedelta(minutes = (times.minute % resolution))
            minplus = datetime.timedelta(minutes=resolution) - minminus
            if (times.minute % resolution) <= resolution/2:
                newtime = times - minminus
            else:
                newtime=times + minplus
            self._roundtime.append(newtime)
            self._roundtimeStr.append(newtime.strftime("%m/%d/%Y %H:%M"))

def printLargeArray(data_list, annotation_list, base_name, key_file):
    #find index with data you want
    base_data = []
    key_idx = 0
    for i in range(len(annotation_list)):
        if annotation_list[i] == key_file:
            base_data = zip(data_list[i]._roundtimeStr, data_list[i]._value)
            print('base data is: '+annotation_list[i])
            key_idx = i
            break
        if i == len(annotation_list):
            print('Key not found')

    file=open(base_name+'.csv','w')
    file.write('time,')

    file.write(annotation_list[key_idx][0:-4]+', ')

    non_key = list(range(len(annotation_list)))
    non_key.remove(key_idx)

    for idx in non_key:
        file.write(annotation_list[idx][0:-4]+', ')
    file.write('\n')


    for time, value in base_data:
        file.write(time+', '+value+', ')
        for n in non_key:
            if time in data_list[n]._roundtimeStr:
                file.write(str(data_list[n].linear_search_value(time))+', ')
            else:
                file.write('0, ')
        file.write('\n')
    file.close()

if __name__ == '__main__':

    #adding arguments
    parser = argparse.ArgumentParser(description= 'Import and combine data.',
    prog= 'dataImport')

    parser.add_argument('folder_name', type = str, help = 'Name of the folder')

    parser.add_argument('output_file', type=str, help = 'Name of Output file')

    parser.add_argument('--number_of_files', type = int,
    help = "Number of Files", required = False)

    args = parser.parse_args()

    folder_path = args.folder_name

    #pull all the folders in the file
    files_lst = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

    #import all the files into a list of ImportData objects
    data_lst = []
    for files in files_lst:
        data_lst.append(ImportData(folder_path+files))

    #print to a csv file
    printLargeArray(data_lst,files_lst,args.output_file,'cgm_small.csv')
