@echo off
:: Clear the screen and display introductory information
cls
echo.
echo ================================
echo Please wait... Starting the program...
echo ================================
echo [PRESS ANY KEY TO CONTINUE]
pause >nul
echo.

:: Display project details
echo Project Title: Novel Smart Algae Bio Panel and Its Growth Forecasting using ML - A Sustainable Solution
echo Created by: Mr. Shreyash A. Kamble
echo For inquiries, please contact: shreyash261020@gmail.com
echo GitHub: https://github.com/mrkshreyash
echo P.R. : https://github.com/mrkshreyash/Algae-BioFuel.git
echo.
echo This program is available for public use with due credit to the author.
echo.

:: Install virtualenv if not already installed
echo Installing virtualenv...
pip install virtualenv
echo.

:: Create a virtual environment named 'myenv'
echo Creating a virtual environment...
virtualenv myenv
echo.

:: Activate the virtual environment
echo Activating the virtual environment...
call .\myenv\Scripts\activate.bat
echo.

:: Install required Python packages
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
echo.

:: Run the Streamlit application
echo Starting the Streamlit application...
streamlit run Smart_Algae_Growth_Forecasting.py
echo.

:: End of script
echo ================================
echo Program executed successfully.
echo ================================
