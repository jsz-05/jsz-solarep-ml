# Solar Energetic Particles:

### 1. Dataset:
High Priority elements:
- Fe (Iron): Iron is a key element in SEP due to wide range of charge states, and a high Q(Fe) correlation with the Fe/O ratio is significant.
- O (Oxygen): Oxygen is another abundant element and serves as a good reference point when analyzing charge state ratios (like Fe/O).
- Si (Silicon): Silicon, while less abundant than Fe or O, also exhibits a range of charge states

6 Elements are included in the flux data, including C, Fe, He, N, O, and Si across 6 energies and from 2017 to Q1 of 2024

Time-intensity profiles of SEPs:
- These show how the flux of SEPs changes over time. The exponential decay is a characteristic pattern observed in  flux profiles.
- Load info from SIS into dataframe (Fe, O, Si flux from 2017 to Q1 2024)
- Compute statistics (mean, STD, determine cutoff for noise)
- Examine the flux data for sudden, significant increases in particle flux (SEP events)
- Zoom in on the periods after the initial peak, where the flux gradually decreases. These are the decay phases.

### 2. Identifying Decays:
Analysis and identification of decay phases is done in solardecay.ipynb. The code identifies periods of exponential decay in a given time series of flux data.

A sliding window approach is used, where a fixed-size window (specified by `window_size`) is moved across the y-axis log scaled flux data. For each position of the window, linear regression is performed on the data within the window. 

The regression line's slope is computed, and if this slope is less than a predefined threshold (`slope_threshold`), it indicates a significant downward trend, characteristic of an exponential decay. The start and end times of the window are recorded as a decay segment if the slope condition is met.

After identifying all potential decay segments, it proceeds to merge overlapping or adjacent segments. This step ensures that a continuous decay period is not fragmented into multiple segments. 

All the decay phase start/stop times are loaded into a Pandas dataframe, and a plotting function plots all of them on a grid.


### 2. Identifying General SEP Events:
Analysis and identification of general SEP events is done in solarflare.ipynb. The code identifies all SEP events based on certain criteria.

First, the first quartile (Q1) values for each element are precomputed, excluding invalid data points (-999.9 and 0). Multipliers are applied to the elements Helium (He) and Oxygen (O) to account for their abundance. This marks the lower threshold for SEP events.

Next, a `identify_events` detects significant flux events using a smoothed version of the flux data. Slopes are calculated using a specified window size to identify upward trends, which mark the beginning of an event. 

Events are defined by periods where the flux exceeds the Q1 threshold and maintains an upward trend towards a peak. Events are cut off when the flux level decays to a level similar to the flux at the start of the event, following the peak.

All the event start/stop times are loaded into a Pandas dataframe, and a plotting function plots all of them on a grid, with each element being separated and color coded.


