# MacWindowSort

## Description
The Window Sorter program is a command line script that allows you to easily sort and arrange windows on your Mac computer using the Magnet app. It provides a convenient way to open and organize multiple windows or tabs for your work or projects.

## Prerequisites
Before using the Window Sorter program, make sure you have the following prerequisites:

1. Mac computer running Darwin/MacOS 13.4.1 or later.
2. Magnet app installed on your Mac. You can download it from the Mac App Store.
3. Shortcut keys in the Magnet app configured to your preference. This is necessary for the program to work correctly.
4. A configuration file specifying the windows or tabs you want to open. This file needs to be updated with the desired window arrangements.

## Installation
To install and set up the Window Sorter program, follow these steps:

1. Clone the repository or download the source code to your local machine.
2. Open a terminal and navigate to the directory where you downloaded the source code.
3. Run the following command to install the required dependencies:

   ```
   pip install .
   ```

4. Once the installation is complete, you are ready to use the Window Sorter program.

## Usage
To use the Window Sorter program, follow these steps:

1. Update the configuration file (`config.json`) with the desired window arrangements. The file should be located in the same directory as the program.
2. Open a terminal and navigate to the directory where the program is installed.
3. Run the following command to execute the program:

   ```
   work
   ```

   This will open the specified windows or tabs according to the configurations in the `config.json` file.

## Example Configuration
The `config.json` file should contain an array of window configurations. Each configuration should specify the application name and the desired window arrangement. Here is an example configuration:

```json
[
  {
    "app": "Safari",
    "windows": [
      {
        "title": "Window 1",
        "position": "left"
      },
      {
        "title": "Window 2",
        "position": "right"
      }
    ]
  },
  {
    "app": "Terminal",
    "windows": [
      {
        "title": "Window 1",
        "position": "top"
      },
      {
        "title": "Window 2",
        "position": "bottom"
      }
    ]
  }
]
```

In this example, the program will open two Safari windows, one positioned on the left and the other on the right side of the screen. It will also open two Terminal windows, one positioned at the top and the other at the bottom of the screen.

## Notes
- Make sure the Magnet app is running before executing the Window Sorter program.
- If you make changes to the `config.json` file, you need to restart the program for the changes to take effect.
- The Window Sorter program relies on the Magnet app and its shortcut keys for window arrangement. Make sure the shortcut keys are properly configured in the Magnet app for the program to work correctly.