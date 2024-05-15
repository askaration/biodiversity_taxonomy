# Inclusion in Biodiversity Metadata: Vascular Plant Collection in The Chrysler Herbarium and Mycological Collections

## Project Overview
This project focuses on enhancing the integrity and usability of the vascular plant collection data from the Chrysler Herbarium and Mycological Collections at Rutgers University. The research aims to align the dataset with Darwin Core standards, reduce missing data, and analyze the dataset to uncover key insights about collectors, species distribution, and geographic trends.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **Data Cleaning and Preparation**: Standardized inconsistent entries and performed comprehensive data cleaning.
- **Missing Data Analysis**: Calculated and reduced the percentage of missing geospatial data.
- **Darwin Core Alignment**: Compared dataset columns with Darwin Core terms to ensure standardization.
- **Geospatial Data Integration**: Merged the dataset with external geospatial data to enhance completeness.
- **Exploratory Data Analysis**: Visualized key insights about top species, collectors, and geographic distributions.

## Data Sources
- **Primary Dataset**: [Rutgers Chrysler Herbarium and Mycological Collections](https://herbarium.rutgers.edu/)
- **External Geospatial Data**: Dataset used in a project by Santiago Nunez-Corrales, University of Illinois Urbana-Champaign

## Methodology
1. **Data Collection**: Downloaded dataset from the Rutgers Herbarium portal.
2. **Data Cleaning**: Used OpenRefine for initial cleaning and clustering of inconsistent entries.
3. **Missing Data Analysis**: Calculated the amount and percentage of missing data for each column.
4. **Darwin Core Comparison**: Matched dataset columns with Darwin Core terms.
5. **Geospatial Data Integration**: Merged with external geospatial data and updated missing coordinates.
6. **Exploratory Data Analysis**: Conducted analysis to identify top species, collectors, and geographic distributions.

## Results
- **Data Enhancement**: Reduced missing geospatial data from 94.78% to 28.55%.
- **Darwin Core Compliance**: Achieved 78% alignment with Darwin Core terms.
- **Key Insights**: Identified top collectors (e.g., M.A. Chrysler), states (e.g., New Jersey), and species (e.g., Dryopteris Carthusiana).

## Installation
To run the analysis, clone this repository and install the required packages:

```bash
git clone https://github.com/yourusername/biodiversity-metadata-analysis.git
cd biodiversity-metadata-analysis
pip install -r requirements.txt
