import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis
from scipy.signal import find_peaks

def calculate_features(flux_values):
    """Calculates features from a list of flux values."""
    duration = len(flux_values)  # Assuming flux values are hourly
    max_flux = np.nanmax(flux_values)
    
    if (duration >= 25):
        initial_decay_rate = (flux_values[0] - flux_values[24]) / 24
        average_decay_rate = (flux_values[0] - flux_values[-1]) / duration
    else:
        initial_decay_rate = np.nan
        average_decay_rate = np.nan

    time_to_peak = np.argmax(flux_values)
    
    peaks, _ = find_peaks(flux_values)
    peak_prominence = (
        np.nanmax(flux_values[peaks]) - np.nanmin(flux_values) if peaks.size > 0 else 0
    )
    
    num_peaks = len(peaks)
    auc = np.trapz(flux_values)
    skewness = skew(flux_values, nan_policy="omit")
    kurt = kurtosis(flux_values, nan_policy="omit")

    std_flux = np.nanstd(flux_values)
    median_flux = np.nanmedian(flux_values)
    max_median_ratio = max_flux / median_flux if median_flux != 0 else np.nan
    normalized_time_to_peak = time_to_peak / duration if duration > 0 else np.nan

    decay_25_percent = (
        (flux_values[0] - flux_values[int(0.25 * duration)]) / (0.25 * duration)
        if duration >= 4
        else np.nan
    )
    decay_50_percent = (
        (flux_values[0] - flux_values[int(0.50 * duration)]) / (0.50 * duration)
        if duration >= 2
        else np.nan
    )
    decay_75_percent = (
        (flux_values[0] - flux_values[int(0.75 * duration)]) / (0.75 * duration)
        if duration >= 4
        else np.nan
    )
    avg_decay_percentages = np.nanmean(
        [decay_25_percent, decay_50_percent, decay_75_percent]
    )

    return (
        duration,
        max_flux,
        initial_decay_rate,
        average_decay_rate,
        time_to_peak,
        peak_prominence,
        num_peaks,
        auc,
        skewness,
        kurt,
        std_flux,
        median_flux,
        max_median_ratio,
        normalized_time_to_peak,
        decay_25_percent,
        decay_50_percent,
        decay_75_percent,
        avg_decay_percentages,
    )

def create_dataframe(filtered_df, datetime_values, all_flux_data, element_mapping, target_label):
    """Creates a dataframe from the given filtered dataframe and other data."""
    ml_data = []
    for i, row in filtered_df.iterrows():
        event_id = row["Event Number"]
        start_time = pd.to_datetime(
            f"{int(row['Start Year'])}-{row['Start Fractional Day']:.5f}", format="%Y-%j.%f"
        )
        end_time = pd.to_datetime(
            f"{int(row['End Year'])}-{row['End Fractional Day']:.5f}", format="%Y-%j.%f"
        )
        time_mask = (datetime_values >= start_time) & (datetime_values <= end_time)

        data_3d = np.where(all_flux_data == -999.9, np.nan, all_flux_data)

        for element_name, element_index in element_mapping.items():
            if element_name in row["Non-Decaying Elements"] and target_label == 1:
                # print(element_name)
                continue
            
            for energy_level in range(4):
                flux_values = data_3d[energy_level, time_mask, element_index]

                (
                    duration,
                    max_flux,
                    initial_decay_rate,
                    average_decay_rate,
                    time_to_peak,
                    peak_prominence,
                    num_peaks,
                    auc,
                    skewness,
                    kurt,
                    std_flux,
                    median_flux,
                    max_median_ratio,
                    normalized_time_to_peak,
                    decay_25_percent,
                    decay_50_percent,
                    decay_75_percent,
                    avg_decay_percentages,
                ) = calculate_features(flux_values)

                ml_data.append(
                    {
                        "Event ID": event_id,
                        "Element": element_mapping[element_name],
                        # "Energy Level": energy_level + 1,
                        "Duration": duration,
                        "Max Flux": max_flux,
                        "Initial Decay Rate": initial_decay_rate,
                        "Average Decay Rate": average_decay_rate,
                        "Time to Peak": time_to_peak,
                        "Peak Prominence": peak_prominence,
                        "Number of Peaks": num_peaks,
                        # "AUC": auc,
                        "Skewness": skewness,
                        "Kurtosis": kurt,
                        "Std Flux": std_flux,
                        "Median Flux": median_flux,
                        # "Max/Median Ratio": max_median_ratio,
                        "Normalized Time to Peak": normalized_time_to_peak,
                        "Decay Rate 25%": decay_25_percent,
                        "Decay Rate 50%": decay_50_percent,
                        "Decay Rate 75%": decay_75_percent,
                        "Avg Decay Percentages": avg_decay_percentages,
                        'Target Label': target_label
                    }
                )

    return pd.DataFrame(ml_data)