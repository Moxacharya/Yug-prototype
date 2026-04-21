# Traffic Flow Visualization Prototype

This Python script visualizes a traffic flow vector field using NumPy and Matplotlib. It demonstrates concepts from vector calculus including divergence (congestion) and curl (rotation) in the context of traffic flow.

## Features

- Interactive vector field visualization
- Divergence plot showing congestion areas
- Curl plot showing rotational flow
- Three interactive buttons to switch between views

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository
2. Install dependencies: `pip install numpy matplotlib`
3. Run the script: `python prototype.py`

## Usage

Run the script and use the buttons at the bottom to switch between:
- Vector Field: Shows the direction and magnitude of traffic flow
- Divergence: Highlights areas of congestion (sources/sinks)
- Curl: Shows rotational components of the flow

## Mathematical Model

The traffic flow is modeled as:
- u = -x * exp(-x² - y²)
- v = -y * exp(-x² - y²)

This creates a flow that converges to the origin.