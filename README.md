[![GitHub license](https://img.shields.io/github/license/SINGHxTUSHAR/mpin-validator.svg)](https://github.com/SINGHxTUSHAR/mpin-validator/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/SINGHxTUSHAR/mpin-validator.svg)](https://GitHub.com/SINGHxTUSHAR/mpin-validator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/SINGHxTUSHAR/mpin-validator.svg)](https://GitHub.com/SINGHxTUSHAR/mpin-validator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/SINGHxTUSHAR/mpin-validator.svg)](https://GitHub.com/SINGHxTUSHAR/mpin-validator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


[![GitHub watchers](https://img.shields.io/github/watchers/SINGHxTUSHAR/mpin-validator.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/mpin-validator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/SINGHxTUSHAR/mpin-validator.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/mpin-validator/network/)
[![GitHub stars](https://img.shields.io/github/stars/SINGHxTUSHAR/mpin-validator.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/mpin-validator/stargazers/)

[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/SINGHxTUSHAR/mpin-validator)

## This repo is private, after the submission and checking for the OneBanc-Assignment, this repo will be public. -> Thanks to visit : Author(TUSHAR SINGH)


# MPIN-Validator/Checker:
The project aims to address the security vulnerability of guessable MPINs used for mobile banking access. Users often set weak MPINs that are either common patterns (e.g., 1122) or derived from easily obtainable personal details like date of birth or anniversaries.   

The core task is to develop a program that evaluates the strength of an MPIN (initially 4-digit, then extended to 6-digit).
![Gemini_Generated_Image_8tzm8h8tzm8h8tzm](https://github.com/user-attachments/assets/07964590-0bc1-4557-a231-0682f40e384b)

### `Key Requirements:`

* Identify if a 4-digit MPIN is commonly used.   
* Assess MPIN strength ("WEAK" or "STRONG") considering user demographics (DOB, spouse's DOB, anniversary).   
* If the MPIN is "WEAK", provide specific reasons (e.g., COMMONLY_USED, DEMOGRAPHIC_DOB_SELF).   
* Extend the functionality to support 6-digit MPINs.   
* Include comprehensive testing with at least 20 test cases.

## `How to Run the code:`
Run this command in your VSCode cmd terminal : ``` python mpinValidator.py```

## `How to Run the code:`
Run this command in your VSCode cmd terminal : ``` python mpinValidator.py```


## Project Directory Structure:
```
# Project structure:
# MPIN-VALIDATOR/
# ├── common/
# │   ├── __init__.py
# │   ├── constants.py     # Common constants used across the project
# │   └── utils.py         # Utility functions
# ├── validators/
# │   ├── __init__.py
# │   ├── common_mpin.py   # Common MPIN validator
# │   └── demographic.py   # Demographic based validation
# ├── models/
# │   ├── __init__.py
# │   ├── user.py          # User model with demographic information
# │   └── result.py        # Result model for validation output
# ├── main.py              # Contains the MPIN-Validation class
# ├── mpinValidator.py     # Main entry point: Run this file for checking/validating the strength of MPIN
# └── tests/
#     ├── __init__.py
#     └── test_mpin.py     # Test cases

```

## Requirements💻 :

Ensure you have the following dependencies installed:

- Python (version 3.12.x)
- IDE: VS-CODE or collab
- Virtual-environment(venv)
- Other dependencies (refer to the requirement.txt)
- This project is purely on Python and some Python packages

You can install the required Python packages using:

```bash
pip install -r requirement.txt
```

## Setup 💿:

- Clone the repository:
```bash
git clone https://github.com/SINGHxTUSHAR/mpin-validator.git
cd NextWordAI
```
- Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
- Activate the virtual environment:
  - On Windows:
   ```bash
   venv\Scripts\activate
   ```
  - On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```


## Contributing 📌:
If you'd like to contribute to this project, please follow the standard GitHub fork and pull request process. Contributions, issues, and feature requests are welcome!

## Suggestion 🚀: 
If you have any suggestions for me related to this project, feel free to contact me at tusharsinghrawat.delhi@gmail.com or <a href="https://www.linkedin.com/in/singhxtushar/">LinkedIn</a>.

## License 📝:
This project is licensed under the <a href="https://github.com/SINGHxTUSHAR/mpin-validator/blob/main/LICENSE">MIT License</a> - see the LICENSE file for details.
