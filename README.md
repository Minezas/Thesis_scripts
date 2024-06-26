## Scripts for Data Extraction

**Introduction**

This repository contains a collection of scripts designed to facilitate the extraction and analysis from documents generated by tools such as OpenControl (Aguiar, Mendonca et al. 2007) and Bonsai (Lopes, Bonacchi et al. 2015).

**Features**

### Latency Learning Curve

- **`latencies_learning.py`**: This script calculates the average latency.

- ### Latency Probe Sessions

- **`latencies_probe.py`**: This script calculates the average latency, latency of rewarded / no rewarded trials and latency of delayed / instant trials.

### Variation and Shifting

- **`variation_&_shifting.py`**: This script calculates the variation and shifting between levers of the animal.

### Animal Tracking

- **`coordinates.py`**: This script assists in reading a .txt document generated by Bonsai for tracking the animal's position vector.

### Distance and Average Speed

- **`distance_and_speed.m`**: Matlab script for additional analysis of tracking data. It allows calculating distance (in pixels) and average speed (pixels/second) based on animal tracking data.

**Usage**

To use the scripts:

1. Clone this repository to your local environment.
2. Run the scripts corresponding to the data you want to analyze.
3. Follow the instructions provided in the scripts themselves to provide the correct paths to the input files.

**Requirements**

- Python 3.x
- MATLAB

**Contributions**

Contributions are welcome! If you have suggestions for improvements or encounter issues, feel free to open an issue or submit a pull request.

---

This project is maintained by Minezas (Gonçalo Araújo). If you encounter any problems or have any questions, please feel free to contact me by goncaloaraujo1070@gmail.com

### Bibliography

- Aguiar, P., L. Mendonca, & V. Galhardo. (2007). "OpenControl: a free opensource software for video tracking and automated control of behavioral mazes." *J Neurosci Methods, 166*(1), 66-72.
  
- Lopes, G., N. Bonacchi, J. Frazao, J. P. Neto, B. V. Atallah, S. Soares, L. Moreira, S. Matias, P. M. Itskov, P. A. Correia, R. E. Medina, L. Calcaterra, E. Dreosti, J. J. Paton, & A. R. Kampff. (2015). "Bonsai: an event-based framework for processing and controlling data streams." *Front Neuroinform, 9*, 7.


