# aih hackathon2017

### API Robot control

    arm_api.txt   - robot side server code
    robot.py      - client side API to control arm

Prerequisites (numpy, requests):

    pip install -r requirements.txt

### Direct Robot control

Make sure API prerequisites are installed. Then install
`gcc`, `libffi-devel`, `SDL2-devel` (Fedora):

    dnf install libffi-devel SDL2-devel

Create virtualenv with dependencies:

    virtualenv .robot
    # install dependencies
    .robot/bin/pip install -r requirements_riuk.txt

Run `.robot/bin/python riuk.py`.

    ENTER       - open/close gripper
    LEFT/RIGHT  - move between robot links
    UP/DOWN     - change link angle by 1 degree
    ESCAPE      - run away

