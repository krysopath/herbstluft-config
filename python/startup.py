import os

def run():
    command = 'silent new_attr bool my_not_first_autostart'
    exitcode = os.system('herbstclient ' + command)

    if exitcode == 0:
        #os.system("compton &")
        os.system("dunst &")
        os.system("parcellite &")
        os.system("nitrogen --restore &")
        os.system('xli -border black -onroot -display ":0" -fillscreen  ~/.config/herbstluftwm/cat_pic.jpg')
        os.system("mpd &")
        os.system("redshift &")
        os.system("gpg-agent &")

