# 📦 Parallelepiped Statistics Project

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

A project to analyze geometric properties of parallelepipeds and generate statistical reports. Calculates diagonals, volumes, surface areas, angles, and sphere properties. Results are exported to JSON and HTML formats.

## 📚 Table of Contents

| Section            | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| [Project Overview](#-project-overview) | Overview of project objectives and components.                  |
| [Installation](#-installation) | Steps to install the project.                                   |
| [Usage](#-usage) | Instructions for using the project.                               |
| [File Structure](#-file-structure) | Directory structure of the project.                             |
| [Modules & Functions](#-modules--functions) | Functions provided in the project and their descriptions.       |
| [Output](#-output) | Sample output of the project in JSON and HTML formats.            |
| [Contributing](#-contributing) | Guidelines for contributing to the project.                    |
| [License](#-license) | License information.                                              |

---

## 🚀 Project Overview

This project processes parallelepiped data to calculate:
- **Geometric properties**: Diagonals, volume, surface area
- **Angles**: Between space diagonals and axes
- **Sphere properties**: Radius and volume of the circumscribed sphere

**Components**:
- `main.py` - Orchestrates data processing and output generation
- `utils/functions.py` - Core geometric calculations
- `utils/statistics.py` - Statistical analysis
- `html.py` - HTML report generator
- `parallelepipeds.json` - Input data (dimensions of parallelepipeds)
- `outputs/` - Generated JSON/HTML results

---

## 💻 Installation

| Step                            | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| Clone the repository            | `git clone https://github.com/yourusername/parallelepiped-statistics.git` |
| Navigate to the project folder  | `cd parallelepiped-statistics`                                      |
| Verify Python 3.7+ is installed  | `python --version`                                                 |
| Dependencies                     | No external dependencies required - Uses standard Python libraries. |

---

## 🛠 Usage

| Step                        | Description                                                      |
| --------------------------- | ---------------------------------------------------------------- |
| **Step 1: Prepare Input Data**  | Create/update `parallelepipeds.json` with your data.              |
| Example input:               | ```json { "figure_1": { "a": "2", "b": "1", "c": "6" }, "figure_2": { "a": "16", "b": "10", "c": "14" } } ``` |
| **Step 2: Run the Analysis**  | Run the following command: `python main.py`                        |
| **Step 3: View Results**      | Open the generated report files in your browser or JSON viewer.   |
| Files generated:              | `outputs/characteristics.json`, `outputs/statistics.json`, `outputs/data_summary.html` |

---

## 📂 File Structure

| File Path                              | Description                                                        |
| -------------------------------------- | ------------------------------------------------------------------ |
| `main.py`                              | Main script to run the analysis and generate outputs.              |
| `parallelepipeds.json`                 | Input file containing dimensions of parallelepipeds.               |
| `utils/functions.py`                   | Contains core geometric calculation functions.                     |
| `utils/statistics.py`                  | Contains statistical analysis functions.                           |
| `html.py`                              | HTML report generator.                                             |
| `outputs/`                             | Folder containing generated JSON and HTML results.                 |
| `README.md`                            | This file.                                                        |

---

## 🧩 Modules & Functions

| Function             | Description                                  | Formula                          |
| -------------------- | -------------------------------------------- | -------------------------------- |
| `get_diag(a, b, c)`  | Space diagonal length                        | √(a² + b² + c²)                  |
| `get_volume(a, b, c)`| Volume                                      | a × b × c                        |
| `get_surface(a, b, c)`| Surface area                                | 2(ab + bc + ca)                  |
| `get_alpha(a, b, c)` | Angle between diagonal and x-axis           | arccos(a / diagonal)             |
| `get_sphr_radius(...)`| Circumscribed sphere radius                | ½ × diagonal                     |
| Full list            | See `functions.py` for all 10+ calculations. |                                  |

---

## 📊 Output

| File                         | Description                                            |
| ---------------------------- | ------------------------------------------------------ |
| `characteristics.json`       | Calculated properties for each parallelepiped.          |
| Example:                     | ```json { "figure_1": { "diagonal": 6.403, "volume": 12, "surface_area": 40, "alpha_angle": 71.565, "sphere_volume": 137.861 } } ``` |
| `statistics.json`            | Statistical averages for the dataset.                   |
| Example:                     | ```json { "average_volume": 254.8, "max_diagonal": 28.142, "min_sphere_radius": 3.201 } ``` |
| `data_summary.html`          | Interactive HTML report with data visualizations.       |

---

## 🤝 Contributing

| Step                         | Description                                                        |
| ---------------------------- | ------------------------------------------------------------------ |
| Fork the repository          | Create your own fork of the repository.                           |
| Create a feature branch      | `git checkout -b feature/amazing-feature`                         |
| Commit your changes          | `git commit -m 'Add amazing feature'`                             |
| Push to your branch          | `git push origin feature/amazing-feature`                         |
| Open a Pull Request          | Submit a pull request for review.                                 |

---

