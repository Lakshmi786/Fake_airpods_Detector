# Airpods Authenticity Checker

## Overview
This code provides a simple interface to check the authenticity of Apple AirPods. The checker verifies the AirPods' model number, serial numbers, firmware version, and whether the serial numbers are iterative. It returns one of three possible outputs:

Congratulations, Your Earpods/ Headphones are Genuine
Looks like Earpods/ Headphones are mostly Genuine, but Case has been swapped
Extremely sorry, Your Earpods/ Headphones are Probably Knock off

## Prerequisites
This code requires the following modules:

pandas
os
gradio

## How to use
To run the AirPods authenticity checker, follow these steps:

Install the required modules.
Copy the code and save it to a file.
Run the file.
Select the AirPods model from the dropdown menu.
Enter the requested information in the text boxes.
Click "Submit."
The output will be displayed in the "Output Box."

## Inputs
AirPods model: Select the AirPods model from the dropdown menu.
Charging case serial number: Enter the charging case serial number.
Box serial number: Enter the box serial number.
Left bud model number: Enter the left bud model number.
Right bud model number: Enter the right bud model number.
Left bud serial number: Enter the left bud serial number.
Right bud serial number: Enter the right bud serial number.
Firmware: Enter the firmware version.

## Outputs
Output Box: Displays one of the three possible outputs:
Congratulations, Your Earpods/ Headphones are Genuine
Looks like Earpods/ Headphones are mostly Genuine, but Case has been swapped
Extremely sorry, Your Earpods/ Headphones are Probably Knock off


## Troubleshooting
If the code returns an error or unexpected output, check the input values and ensure that the required modules are installed.

## Contributors
This code was written by a single contributor.

## License
This code is provided under the MIT License.
