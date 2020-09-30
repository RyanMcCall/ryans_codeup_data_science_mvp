# {{ cookiecutter.project_name }}

### Author: {{ cookiecutter.author }}

## Description: 
{{ cookiecutter.description }}

## Project Organization

Generated with [ryans_codeup_data_science_mvp](https://github.com/RyanMcCall/ryans_codeup_data_science_mvp)

Modified from [datasciencemvp](https://github.com/cliffclive/datasciencemvp/)

```
├── README.md               <- The top-level README for developers using this project.
│
├── data                    <- All of the data for the project
│   ├── modeling            <- The prepared, processed and split datasets for modeling.
│   ├── prepared            <- The prepared datasets for exploration
│   └── raw                 <- The original, immutable data
│
├── main.py                 <- The main python script that calls all src scripts
│
├── mvp.ipynb               <- The main notebook for the project
│
├── src                     <- The source code for use in this project
│   ├── __init__.py         <- Makes src a Python module
│   ├── acquire.py          <- The script to download or generate data and store it in
│   │                          data/raw/
│   ├── explore.py          <- The script for creating any visuals that need to be stored
│   │                          in visuals/generated_graphics/
│   ├── model.py            <- The script for preprocessing, modeling, and interpreting
│   └── prepare.py          <- The script for preparing the raw data and storing it in
│                              data/prepared/
│
└── visuals                 <- All project visuals
    ├── external_visuals    <- Visuals brought from outside the project
    ├── generated_graphics  <- Visuals generated from the project
    └── presentation        <- A copy of your presentation
```

## Data Dictionary

| Feature | Definition |
| --- | --- |
| Feature 1 | Definition 1 |
| Feature 2 | Definition 2 |

| Target | Definition |
| --- | --- |
| Target 1 | Definition 1 |