# CSTR Profit vs. Volume Simulation

This project simulates and visualizes the profit as a function of reactor volume in a Continuous Stirred Tank Reactor (CSTR) system. The graphical interface allows users to adjust parameters dynamically and observe the resulting profit behavior.

## Features

- **Interactive GUI**: Built with `Tkinter`, the application provides an intuitive interface for parameter adjustment.
- **Dynamic Plotting**: Uses `Matplotlib` to dynamically plot the profit as a function of reactor volume.
- **Optimal Profit Calculation**: Automatically determines the reactor volume that maximizes profit and displays it on the graph.

## Dependencies

This project relies on the following Python libraries:

- `numpy`
- `matplotlib`
- `tkinter` (bundled with Python; no need to install via `pip`)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Ensure all dependencies are installed.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Adjust parameters in the GUI to observe changes in the profit curve.

## Usage Instructions

- **Input Fixed Parameters**: Enter the values for the feed concentration, reaction rate constant, flow rate, and maximum reactor volume in the input fields.
- **Adjust Sliders**: Use the sliders to adjust adjustable parameters such as costs, prices, and exponents.
- **View Results**: The application calculates and displays the optimal reactor volume and maximum profit directly above the plot.

## File Structure

- `main.py`: The main script containing the application logic.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: Documentation for the repository.

## Example Output

- Optimal Reactor Volume: **X.XX m³**
- Maximum Profit: **Y.YY €/s**

The profit curve is displayed, with a red dashed line indicating the optimal reactor volume.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

