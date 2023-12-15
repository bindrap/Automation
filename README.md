Automated Reporting Tool

Description:
This project aims to automate the process of generating and downloading reports from a web application. Leveraging Selenium for web automation, the tool navigates through the application, selects specific options on the reporting page, generates the desired report, and ensures successful download. Additionally, it includes functionality to move downloaded reports to a designated destination folder. The automation script is designed for efficiency and ease of integration into various testing or data analysis workflows.

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
python TestScript.py

Testing
pytest --html=report.html

To Run test_feature.feature
behave test_feature.feature
