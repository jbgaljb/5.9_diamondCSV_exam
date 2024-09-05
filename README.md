# Diamond Data Analysis

This Python script analyzes diamond data using the Pandas library. It provides various insights such as the most expensive diamond, the average price, counts of specific cuts, and more.

## Features

- **Most Expensive Diamond**: Find the price of the most expensive diamond in the dataset.
- **Average Price**: Calculate the average price of diamonds.
- **Ideal Cut Count**: Count the number of diamonds with an "Ideal" cut.
- **Different Colors**: List all the distinct diamond colors in the dataset.
- **Premium Cut Carat Median**: Calculate the median carat size for diamonds with a "Premium" cut.
- **Average Carat Per Cut**: Calculate the average carat size for each type of diamond cut.
- **Average Price Per Color**: Calculate the average price for diamonds of each color.

## Requirements

- Python 3.x
- Pandas library

## Setup

1. Clone this repository or download the script.
2. Make sure you have `data.csv` in the same directory as the script. The CSV file should contain at least the following columns:
    - `price`: The price of the diamond.
    - `cut`: The cut of the diamond (e.g., "Ideal", "Premium").
    - `color`: The color grade of the diamond.
    - `carat`: The carat weight of the diamond.
3. Install the required dependencies by running:
    ```bash
    pip install pandas
    ```

## Usage

Run the script using Python:

```bash
python <script_name>.py
