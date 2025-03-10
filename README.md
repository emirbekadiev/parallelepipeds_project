Parallelepiped Statistics Project
This project is designed to process and analyze the characteristics of parallelepipeds. It calculates various geometric properties such as diagonals, volumes, surface areas, angles, and properties of the described spheres. The results are then summarized in a statistical report and presented in an HTML format.

Table of Contents
Project Overview

Installation

Usage

File Structure

Functions and Modules

Output

Contributing

License

Project Overview
The project consists of several Python scripts that work together to process data about parallelepipeds, calculate their geometric properties, and generate a summary report in HTML format. The main components include:

main.py: The main script that orchestrates the processing of parallelepiped data and generates the final output files.

utils/functions.py: Contains utility functions for calculating geometric properties of parallelepipeds.

utils/statistics.py: Computes the average values of the calculated properties.

html.py: Generates an HTML file that displays the statistical summary.

parallelepipeds.json: Input data containing the dimensions of parallelepipeds.

outputs/characteristics.json: Output data containing the calculated properties of each parallelepiped.

outputs/statistics.json: Output data containing the average values of the calculated properties.

outputs/data_summary.html: The final HTML report summarizing the statistics.

Installation
To set up the project, follow these steps:

Clone the Repository:

bash
Copy
git clone https://github.com/yourusername/parallelepiped-statistics.git
cd parallelepiped-statistics
Install Python:
Ensure you have Python 3.7 or higher installed. You can download it from python.org.

Install Dependencies:
The project uses the standard Python libraries, so no additional dependencies are required.

Usage
Prepare Input Data:
Ensure that the parallelepipeds.json file contains the dimensions of the parallelepipeds you want to analyze. The file should follow the format:

json
Copy
{
    "figure_1": {
        "a": "2",
        "b": "1",
        "c": "6"
    },
    "figure_2": {
        "a": "16",
        "b": "10",
        "c": "14"
    },
    ...
}
Run the Main Script:
Execute the main.py script to process the data and generate the output files:

bash
Copy
python main.py
View the Results:

The calculated properties for each parallelepiped will be saved in outputs/characteristics.json.

The statistical summary will be saved in outputs/statistics.json.

The HTML report will be generated as outputs/data_summary.html. Open this file in a web browser to view the summary.

File Structure
Copy
parallelepiped-statistics/
│
├── main.py                  # Main script to process data and generate outputs
├── utils/                   # Directory containing utility modules
│   ├── functions.py         # Utility functions for geometric calculations
│   └── statistics.py        # Script to compute average values
├── html.py                  # Script to generate HTML report
├── parallelepipeds.json     # Input data with parallelepiped dimensions
├── outputs/                 # Directory containing output files
│   ├── characteristics.json # Output data with calculated properties
│   ├── statistics.json      # Output data with average values
│   └── data_summary.html    # HTML report summarizing the statistics
└── README.md                # Project documentation
Functions and Modules
utils/functions.py
This module contains functions to calculate various geometric properties of parallelepipeds:

get_diag(a, b, c): Calculates the diagonal of the parallelepiped.

get_volume(a, b, c): Calculates the volume of the parallelepiped.

get_surface(a, b, c): Calculates the surface area of the parallelepiped.

get_alpha(a, b, c), get_beta(a, b, c), get_gamma(a, b, c): Calculate the angles between the diagonals and the axes.

get_sphr_radius(a, b, c): Calculates the radius of the described sphere.

get_sphr_volume(a, b, c): Calculates the volume of the described sphere.

process(a, b, c): Returns a dictionary with all calculated properties.

utils/statistics.py
This module computes the average values of the calculated properties:

get_stat_dict(characteristics): Takes a dictionary of parallelepiped characteristics and returns a dictionary of average values.

html.py
This module generates an HTML file that displays the statistical summary:

generate_html(): Reads the statistics from statistics.json and generates an HTML file.

Output
The project generates the following output files:

outputs/characteristics.json: Contains the calculated properties for each parallelepiped.

outputs/statistics.json: Contains the average values of the calculated properties.

outputs/data_summary.html: An HTML file that presents the statistical summary in a user-friendly format.

Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes and push to the branch.

Submit a pull request.

Thank you for using the Parallelepiped Statistics Project! If you have any questions or need further assistance, please feel free to contact the project maintainers.
