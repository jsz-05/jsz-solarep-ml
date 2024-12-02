
# Solar Energetic Particles (SEP) Analysis

This repository contains code and data for analyzing solar energetic particles (SEPs) using novel machine learning approaches. The project involves processing flux data of various elements, identifying significant events, and visualizing the results.

This research will be presented at the American Geophysical Union Conference, held in Washington, D.C., from December 9–13, 2024. For more details, please refer to the [AGU24 program](https://agu.confex.com/agu/agu24/meetingapp.cgi/Paper/1696330).

---

Solar Energetic Particles (SEPs) are a significant phenomenon in space weather research, as they are not only capable of disrupting infrastructure on Earth, but also provide insights into solar phenomena through their ionic charge states. All flux data collected by the Solar Isotope Spectrometer aboard NASA's ACE orbiter, courtesy of the ACE Science Center at Caltech.

Although instruments like NASA’s Solar Isotope Spectrometer (SIS) aboard the Advanced Composition Explorer (ACE) do not directly measure ionic charge states, these states can be inferred if an energy-dependence exists within the time decay constants of SEP event profiles. These profiles can also yield info on the types of particle accelerations present. (Sollitt et al. (2008)).

Current methods for extracting decay profiles for charge state inference involve manual and semi-automated algorithms that are time-consuming and prone to implicit bias. To solve this, we leverage machine learning techniques, specifically Multilayer Perceptrons (MLP) combined with time-series analysis methods, as well as time-series imaging techniques, such as DMDT or Gramian Angular Fields, for use with training Convolutional Neural Networks (CNNs) for classification.

This repository contains code and data for this project.

## Repository Structure

- **flux**: Contains raw flux data files from 2017-2024 
- **flux_1998**: Contains flux data from 1998-2014 
- **flux_2014**: Contains flux data from 2014-2024
- **mlp_model**: Location to store trained MLP models for decay event classification

- **old_analyses**: Archive of previous analyses, not used anymore.
  - **data**: Raw flux data for Fe and O with ratios. Used for early visualization, not used anymore.
  - **graphing**: Old scripts for graphing and visualizing flux data, not used anymore.
  - **out_grid**: Old Output files from grid-based analyses, not used anymore.
  - **trim_txt**: Text files with trimming instructions used in old analyses, not used anymore.
  - **Notebooks**:
    - **decay_training.ipynb**: Initial test for training decay identification models.
    - **solardecay.ipynb**: Initial test for analyzing and identifying decay phases in SEP data.
    - **solarflare.ipynb**: Initial test for identifying general SEP events.

- **out_csv**: Output CSV files from the old analyses, not used anymore.

- **randomforest_model**: Location to store trained Random Forest models for decay event classification


- **transformed_data**: Transformed data files used in the current analyses.
  - **decay_input_features_2014.csv**: Transformed features for input to ML training. Features are calculated from 57 total events extracted from 2014-2024
  - **decay_test_features_1998.csv**: Transformed test features for input to ML analysis. Features are calculated from 113 total events extracted from 1998-2014
  - **decay_test_predictions.csv**: Features from 1998-2014 analysis with an added column with predicted labels made by the ML model.
  - **filtered_decay_events.csv**: Filtered list of 27 decay events with more than 4 elements decaying from 2014-2024
  - **uncleaned_decay_events_14.csv**: Unfiltered list of 186 decay events from 2014-2024

## Scripts

- **features.py**: Scripts for extracting features from SEP data.
- **graph.py**: Scripts for graphing and visualizing SEP data.
- **identification.py**: Scripts for identifying decay phases in SEP data.
- **load.py**: Scripts for loading SEP data into data structures for analysis.

## Jupyter Notebooks


- **decay_identification.ipynb**: Notebook for classifying different types of decays (Exponential, Power-Law, Irregular)

- **test_mlp_1998-2014.ipynb**: Notebook for testing the trained MLP model with 1998-2014 data.
- **test_randomforest_1998-2014.ipynb**: Notebook for testing the trained MLP model with 1998-2014 data.
- **train_data_2014.ipynb**: Notebook for analyzing, preparing, and extracting training data from 2014-2024, used to train MLP in `train_mlp_2014.ipynb`.
- **train_mlp_2014.ipynb**: Notebook for training the MLP model with 2014-2024 data. 
- **train_randomforest_2014.ipynb**: Notebook for training the Random Forest classifier with 2014-2024 data.

## HTML

- **web_plot.html**: HTML file for web-based plotting of SEP data with general event detection start/stop flags.

<!-- ## Dataset

### High Priority Elements

- **Fe (Iron)**: Key element in SEP analysis due to a wide range of charge states and significant correlation with the Fe/O ratio.
- **O (Oxygen)**: Abundant element serving as a reference point when analyzing charge state ratios.
- **Si (Silicon)**: Exhibits a range of charge states, though less abundant than Fe or O.

The dataset includes flux data for six elements: Carbon (C), Iron (Fe), Helium (He), Nitrogen (N), Oxygen (O), and Silicon (Si) across six energies from 2017 to Q1 2024.

### Time-Intensity Profiles of SEPs

- Show how the flux of SEPs changes over time.
- Exponential decay is a characteristic pattern observed in flux profiles.

Steps:

1. Load data from SIS into a dataframe (Fe, O, Si flux from 2017 to Q1 2024).
2. Compute statistics (mean, standard deviation, determine cutoff for noise).
3. Examine flux data for sudden, significant increases in particle flux (SEP events).
4. Zoom in on periods after the initial peak, where the flux gradually decreases (decay phases).

## Analysis and Identification

### Identifying Decays

Conducted in `solardecay.ipynb`. The code identifies periods of exponential decay in the time series of flux data using a sliding window approach.

- Linear regression is performed within a fixed-size window.
- The slope of the regression line indicates a significant downward trend (exponential decay) if below a threshold.
- Decay segments are merged to ensure continuous decay periods are not fragmented.
- Results are loaded into a Pandas dataframe and plotted.

### Identifying General SEP Events

Conducted in `solarflare.ipynb`. The code identifies SEP events based on predefined criteria.

- Precompute first quartile (Q1) values for each element, excluding invalid data points.
- Apply multipliers to He and O to account for abundance.
- `identify_events` detects significant flux events using smoothed flux data and slope calculations.
- Events are defined by periods exceeding the Q1 threshold and maintaining upward trends toward a peak.
- Results are loaded into a Pandas dataframe and plotted.
 -->
