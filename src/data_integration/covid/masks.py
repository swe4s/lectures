from operator import itemgetter
import rates
import sys
sys.path.insert(1, '../../hash_tables/')
import hash_table



def main() :
    covid_data='covid-19-data/us-counties.csv'
    cencus_data='co-est2019-alldata.csv'
    mask_data='covid-19-data/mask-use/mask-use-by-county.csv'


    state = sys.argv[1]

    co_county_pop = rates.get_columns(cencus_data, [5], [state], [6,7])

    pop_hash_table = hash_table.ChainHashTable(10000, hash_table.hash_functions.h_python)
    for co in co_county_pop:
        county  = co[0][:-7]
        pop  = int(co[1])
        pop_hash_table.insert(county, pop)

    county_masks = rates.get_columns(mask_data, None, None, (0,4,5))

    mask_hash_table = hash_table.ChainHashTable(10000, hash_table.hash_functions.h_python)
    for county_masks in county_masks:
        county_fp = county_masks[0]
        mask_rate = float(county_masks[1]) + float(county_masks[2])
        mask_hash_table.insert(county_fp, mask_rate)

    co_county_cases = rates.get_columns(covid_data, [2,0], [state,'2020-10-28'], [1,3,4])

    county_cases_mask_rate = []
    for co_county_case in co_county_cases:
        name = co_county_case[0]

        if name == 'Unknown':
            continue

        fp = co_county_case[1]
        cases = int(co_county_case[2])

        pop = pop_hash_table.find(name)
        mask_rate = mask_hash_table.find(fp)

        county_cases_mask_rate.append((name,cases/pop,mask_rate))

    for co in county_cases_mask_rate:
        print(co[0],co[1],co[2])

if __name__ == '__main__':
    main()
