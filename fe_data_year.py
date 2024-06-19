import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    data = np.loadtxt(filename, skiprows=25)
    return data

def calculate_fp_doy(fp_year):
    year = np.floor(fp_year)
    fp_doy = (fp_year - year) * 365.25
    return fp_doy

def plot_fe_data(filename_fe, energy_levels, data_type):
    data_fe = read_data(filename_fe)

    fp_year_fe = data_fe[:, 0]
    data_fe_values = data_fe[:, 1:9]  # Assuming 8 columns of data
    fp_doy_fe = calculate_fp_doy(fp_year_fe)

    plt.figure(figsize=(24, 6))

    for level in energy_levels:
        if level < 1 or level > 8:
            continue 
        
        if data_type == 'flux':
            plt.plot(fp_doy_fe, data_fe_values[:, level-1], label=f'Energy level {level}')
            plt.ylabel('Iron Flux (particles/(cm² Sr sec MeV/nucleon))')
            plt.title('Iron Flux at Specified Energy Levels Throughout the Year 2024')
        elif data_type == 'counts':
            plt.plot(fp_doy_fe, data_fe_values[:, level-1], label=f'Energy level {level}')
            plt.ylabel('Iron Counts')
            plt.title('Iron Counts at Specified Energy Levels Throughout the Year 2024')

    plt.xlabel('Fractional Day of Year')
    plt.legend()
    plt.grid(True)
    plt.ylim(0, np.max(data_fe_values) * 1.05) 
    plt.show()

filename_fe_flux = 'data/fp_year_vs_fe_flux.txt'
filename_fe_counts = 'data/fe_count.txt'

energy_levels = [1, 3, 5, 7]  # Define the energy levels to plot

plot_fe_data(filename_fe_flux, energy_levels, 'flux')
plot_fe_data(filename_fe_counts, energy_levels, 'counts')
