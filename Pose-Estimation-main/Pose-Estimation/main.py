import subprocess
import PySimpleGUI as sg

sg.theme('DarkBlue12')
while True:
    layout = [[sg.Text(
        " \n      P   O   S   E       E   S   T   I   M   A   T   I   O   N   \n\t\t\t\t\t",
        background_color='#003B73', text_color='white', font='Impact', key='-DISPLAY-', size=(175, 3),
        justification='center')],
              [sg.Button("Hand Pose",font='Arial', size=(90, 2))],
        [sg.Button("Face Pose", font='Arial', size=(90, 2))],
        [sg.Button("Body Pose", font='Arial', size=(90, 2))],

        [sg.Cancel("EXIT", font='Arial', size=(140, 2))]]
    window = sg.Window("POSE-ESTIMATION VIEW", layout, size=(500, 340))
    event, values = window.read()
    window.close()

    if event == "Hand Pose":
        subprocess.run("python3 HandPoseEstimation.py", shell=True)

    elif event == "Face Pose":
        subprocess.run("python3 FacePose.py", shell=True)

    elif event == "Body Pose":
        subprocess.run("python3 BodyPose.py", shell=True)

    elif event == "EXIT":
        break

    else:
        exit()


