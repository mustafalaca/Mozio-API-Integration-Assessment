# Mozio API Integration Assessment

This repository contains the implementation of an API integration assessment for Mozio, a transportation service provider. The goal of this assessment is to integrate with the Mozio API to perform search, make reservations, poll for reservation status, and cancel reservations.

## Getting Started

### Prerequisites

- Python 3.x
- requests 2.31.x
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:
```commandline
   git clone https://github.com/mustafalaca/Mozio-API-Integration-Assessment.git
```
2. Navigate to the project directory:
```commandline
   cd Mozio-API-Integration-Assessment
```
3. Create a virtual environment (optional but recommended):
```commandline
    python -m venv venv
```

4. Activate the virtual environment:

- Windows:
```commandline
    venv\Scripts\activate
```
- macOS / Linux:
```commandline
    source venv/bin/activate
```
5. Install the required dependencies:
```commandline
    pip install -r requirements.txt
```

### Usage

Make sure you have a valid API KEY and the correct Mozio API URL. Update the `MOZIO_URL` and `API-KEY` variables in the `interact_mozio_api.py` and `request_parameters.py` files respectively.

### Acknowledgments

Special thanks to Mozio for providing the API integration assessment and the opportunity to work on this project.

For more information about Mozio and their services, visit their [official website](https://www.mozio.com).
