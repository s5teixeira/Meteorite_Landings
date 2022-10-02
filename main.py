from meteor_data_class import MeteorDataEntry


def main():
    # opening the file for reading
    file_obj = open('meteorite_landings_data.txt', 'r')

    # read file each at a time
    line = file_obj.readline()

    # create dict for meteor objects
    objs = {'mass': list(), 'year': list()}
    # keep reading while there are more lines to read
    while line:
        # replace the \n character with empty string character
        line = line.replace('\n', "")
        # split line by tab to get array of strings
        line = line.split('\t')
        # create new meteor object
        obj = MeteorDataEntry()

        # set all the member fields
        obj.name = line[0]
        obj.id = line[1]
        obj.nametype = line[2]
        obj.recclass = line[3]
        obj.mass = line[4]
        obj.fall = line[5]
        obj.year = line[6]
        obj.reclat = line[7]
        obj.reclong = line[8]
        obj.geolocation = line[9]
        obj.states = line[10]
        obj.fall = line[11]

        # check to see if object qualifies filtering
        try:
            if float(obj.mass) > 2900000:
                objs['mass'].append(obj)
            if int(obj.year) >= 2013:
                objs['year'].append(obj)
        # exception handling bc of converting str to float
        except ValueError:
            pass

        line = file_obj.readline()

    # print tables
    name_label = 'NAME'
    mass_label = 'MASS (g)'
    print(f'{name_label:<24}{mass_label:<20}')
    print('====================================')
    for obj in objs['mass']:
        print(f'{obj.name:<24}{obj.mass:<20}')

    # print objects filtered by year
    year_label = 'YEAR'
    print('\n')
    print(f'{name_label:<24}{year_label:<20}')
    print('====================================')
    for obj in objs['year']:
        print(f'{obj.name:<24}{obj.year:<20}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
