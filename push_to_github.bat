@echo off
cd /d "c:\Users\ankit\Downloads\PEP PYTHON COURSE\codes\smart_campus_project"

REM Reset any pending merges
git reset --hard HEAD
git merge --abort 2>nul

REM Pull from remote with allow unrelated histories
git pull origin main --allow-unrelated-histories --no-edit

REM Push to GitHub
git push -u origin main

REM Show status
git status

echo.
echo Push completed! Check the output above for any errors.
pause
