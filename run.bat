
cd /d D:\mine

call .venv\Scripts\activate

pytest -v -m regression --html=reporttss/report.html --alluredir=allure-results

allure generate allure-results -o allure-report --clean