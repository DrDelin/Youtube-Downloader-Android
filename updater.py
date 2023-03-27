#ToDo - Build this updater script
import subprocess
from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(days = 1)

latest_release_date = str(subprocess.check_output('git log -1 --format=%ai ytd_win_beta', shell=True))
latest_release_date = latest_release_date.split(' ')[0].split("\'")[1]
latest_release_date = (latest_release_date.split('-')[0], latest_release_date.split('-')[1], latest_release_date.split('-')[2])

new_release_date = date(
    int(latest_release_date[0]), int(latest_release_date[1]), int(latest_release_date[2]))

print("Latest release is newer : ", new_release_date > yesterday)
