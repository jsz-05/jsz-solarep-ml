import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    data = np.loadtxt(filename, skiprows=25)
    return data

def calculate_fp_doy(fp_year):
    year = np.floor(fp_year)
    fp_doy = (fp_year - year) * 365.25
    return fp_doy

def plot_fe_o_ratio(filename_fe, filename_o, energy_levels):
    data_fe = read_data(filename_fe)
    data_o = read_data(filename_o)

    fp_year_fe = data_fe[:, 0]
    flux_fe = data_fe[:, 1:9]  

    fp_year_o = data_o[:, 0]
    flux_o = data_o[:, 1:9] 

    fp_doy_fe = calculate_fp_doy(fp_year_fe) # same for o

    if flux_o.any() == 0:
        ratio_fe_o = None
    else:
        ratio_fe_o = flux_fe / flux_o

    plt.figure(figsize=(12, 8))

    for level in energy_levels:
        if level < 1 or level > 8:
            continue 
        plt.plot(fp_doy_fe, ratio_fe_o[:, level-1], label=f'Energy level {level}')

    plt.xlabel('Fractional Day of Year')
    plt.ylabel('Fe/O Flux Ratio')
    plt.title('Fe/O Flux Ratio at Specified Energy Levels Throughout the Year 2024')
    plt.legend()
    plt.grid(True)
    #plt.yscale('log') 
    plt.show()

filename_fe = 'data/fe_count.txt'
filename_o = 'data/o_count.txt'
energy_levels = [1, 3, 5, 7]

plot_fe_o_ratio(filename_fe, filename_o, energy_levels)
