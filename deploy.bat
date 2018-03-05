REM cd joule-fe
REM npm run build
REM cd ..
rsync -rv joule-fe/dist pi@192.168.0.90:/home/pi/
rsync -rv joule-be pi@192.168.0.90:/home/pi/
ssh pi@192.168.0.90 "chmod -R 775 dist; rsync -rv joule-be pi@192.168.2.1:/home/pi/; ssh pi@192.168.0.90 'sudo service joule restart';"