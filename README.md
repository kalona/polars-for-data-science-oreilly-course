# Polars for Data Science - A Practical Guide

Welcome to "Polars for Data Science - a Practical Guide". This course, created in partnership with O'Reilly Publisher, is designed to provide a comprehensive and practical understanding of the Polars library, an innovative tool for data manipulation and analysis. Hosted entirely on this GitHub repository, this course will take you from the basics of Polars to integrating it within a full data science workflow.

## Course Overview

- **Introduction**: Understand what makes Polars a groundbreaking technology for data science, where it sits in the landscape of data science tooling, and have an intuition of the syntax differences between Polars, Pandas, and SQL.
- **Getting Started**: Be familiar with Polars's two modes, lazy-mode versus in-memory mode, and understand how to leverage Polars's query optimization.
- **Data Manipulation I: Basics**: Be familiar with the Polars API, and be able to perform basic selecting and filtering queries.
- **Data Manipulation II: Grouping and Aggregation**: Be able to perform Polars queries that involve aggregations, such as group-by's and window functions.
- **Data Manipulation III: Combining Data**: Be able to perform Polars queries that involve combining data, such as joins and concatenations.
- **Data Manipulation IV: Data Types**: Understand all the different data types that exist in Polars, and how to work with them.
- **Data Manipulation V: IO and Interoperation**: Be able to switch their data seamlessly between Pandas, Numpy, and Polars, and be able to read and write data both locally and to the cloud.
- **Integrating with the Data Science Workflow**: Be comfortable using Polars in a typical everyday data science workflow, integrating it with Matplotlib, Plotly, and Scikit Learn.
- **Conclusion**: Have their understanding of the different facets of Polars unified into one clear picture, and be prepared with all the knowledge and reference resources they need to continue using Polars on an everyday basis while growing their knowledge of the tool.

## Installation Instructions

To get started with the course, you'll need to set up your environment with the required packages. The requirements are listed in the `requirements.txt` file. Below are the instructions for Mac with Intel chip, Mac with M1 chip, and Windows.

### Mac with Intel Chip

1. **Install Python with Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv polars-env
   source polars-env/bin/activate
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Mac with M1 Chip

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**:
   ```bash
   brew install python
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv polars-env
   source polars-env/bin/activate
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Windows

1. **Install Python** (if not already installed):
   Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv polars-env
   polars-env\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Additional Notes

Ensure that you have Jupyter Notebook installed and ready to use, as the course modules are provided in the form of Jupyter notebooks. If you encounter any issues with the installation or setup, please refer to the [official documentation](https://jupyter.org/install) for additional support.

Happy learning and enjoy your journey into the world of Polars!