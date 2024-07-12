import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_all_decay_events(decay_events_df, data_3d, datetime_values, element_mapping, energy_level, extend_days, useLogScale):
    """
    Args:
        decay_events_df (pd.DataFrame): DataFrame containing decay event details.
        data_3d (numpy.ndarray): The 3D data cube (energy, time, element).
        datetime_values (numpy.ndarray): Array of datetime objects for the time axis.
        element_mapping (dict): Dictionary mapping element names to array indices.
        energy_level (int): The energy level to analyze.
        extend_days (int): Number of days to extend the time range before and after the event.
    """

    num_events = len(decay_events_df)
    if num_events == 0:
        print("No decay events found to plot.")
        return

    num_cols = 5
    num_rows = int(np.ceil(num_events / num_cols))

    #add key at top
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 4 * num_rows), sharey=True)
    fig.subplots_adjust(hspace=0.5, top=0.95)  

    lines = []
    labels = []

    for i, row in decay_events_df.iterrows():
        ax = axes[i // num_cols, i % num_cols]

        start_time = pd.to_datetime(
            f"{int(row['Start Year'])}-{row['Start Fractional Day']:.5f}", format="%Y-%j.%f"
        )
        end_time = pd.to_datetime(
            f"{int(row['End Year'])}-{row['End Fractional Day']:.5f}", format="%Y-%j.%f"
        )

        # Extend time range by extend_days before and after
        extended_start_time = start_time - pd.Timedelta(days=extend_days)
        extended_end_time = end_time + pd.Timedelta(days=extend_days)

        time_mask = (datetime_values >= extended_start_time) & (
            datetime_values <= extended_end_time
        )

        for element_name, element_index in element_mapping.items():
            element_flux = data_3d[energy_level - 1, time_mask, element_index]

            valid_data_mask = element_flux != -999.9
            element_flux = element_flux[valid_data_mask]
            element_time = datetime_values[time_mask][valid_data_mask]

            line, = ax.plot(element_time, element_flux, label=f"{element_name}")
            if element_name not in labels:
                lines.append(line)
                labels.append(element_name)

        if useLogScale == True:
            ax.set_yscale("log")

        ax.set_xlabel("Day of Year")
        if i % num_cols == 0:
            ax.set_ylabel("Log Flux (particles/(cm² Sr sec MeV/nucleon))")
        ax.set_title(f"Event {i+1} ({start_time.year})")
        ax.grid(True)

        # Set major ticks to daily
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%j"))

        # Set minor ticks to half-daily
        ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=12))

        # Rotate x-axis labels for better readability
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

        # Lines to separate out extra days added before and after each event on plot
        ax.axvline(start_time, color="black", linestyle="--", linewidth=1)
        ax.axvline(end_time, color="black", linestyle="--", linewidth=1)

    # Hide any unused subplots in the grid, not really needed but its nice to have
    for j in range(i+1, num_rows * num_cols):
        axes[j // num_cols, j % num_cols].axis('off')


    #add key at top
    fig.legend(lines, labels, loc='upper center', ncol=len(labels), bbox_to_anchor=(0.5, 1.01))

    plt.tight_layout()
    plt.show()



