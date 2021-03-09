@ECHO off
TITLE COVID-19 vaccination update
ECHO Scraping ACT Health COVID-19 vaccination data ...
start /w /b py ./scrape.py
ECHO Recording changes ...
ECHO.
git add ..\*.*
git commit -m "scheduled update"
git push
ECHO.
ECHO Update complete
exit