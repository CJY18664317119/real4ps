@echo off

REM 启动前端开发服务器
cd 前端
npm run dev

REM 启动后端服务器
cd ..\后端
python app.py