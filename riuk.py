#.robot/bin/python
import tdl

import robot

URL = 'http://100.95.255.181:8080'
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
tdl.setFPS(20)

class RoboState(object):
  def __init__(self, url, console):
    self._robot = robot.Robot(url)
    self.console = console
    self.choice = 0
    self.gropen = True  # gripper is open
    self.refresh()
  def refresh(self):
    self.pose = self._robot.getPose()
    self.links = len(self.pose.angles)
  def draw(self, x=2, y=2):
    """ draw robot links and their angles, and other stuff """
    self.console.draw_str(1, 1, str(self.choice))
    active = [48, 48, 120]
    passive = [0, 0, 0]
    for linkno in range(self.links):
      dx = x + linkno*9
      dy = y #+ linkno
      num = "{:.7}".format(str(self.pose.angles[linkno]))
      #print len(num)
      color = active if self.choice == linkno else passive
      self.console.draw_rect(dx-1, dy, len(num)+2, 1, None, bg=color)
      self.console.draw_str(dx, dy, num, bg=color)
  def next(self):
    self.choice = (self.choice+1) % self.links
  def prev(self):
    self.choice -= 1
    if self.choice < 0:
      self.choice = self.links-1
  def up(self):
    self.refresh()
    self.pose.angles[self.choice] += 1
    self._robot.setPose(self.pose)
  def down(self):
    self.refresh()
    self.pose.angles[self.choice] -= 1
    self._robot.setPose(self.pose)
  def grip(self):
    self.gropen = not self.gropen
    if self.gropen:
      self._robot.closeGripper()
    else:
      self._robot.openGripper()


def center():
  return (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)


console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Riuk AI Hackaton'17")
riuk = RoboState(URL, console)

def handle_keys():
  global riuk
  # blocking
  #user_input = tdl.event.key_wait()

  #realtime
  for event in tdl.event.get():
    if event.type == 'KEYDOWN':
      if event.key == 'SPACE':
	riuk.refresh()
      elif event.key == 'LEFT':
	riuk.prev()
	riuk.refresh()
      elif event.key == 'RIGHT':
	riuk.next()
	riuk.refresh()
      elif event.key == 'UP':
	riuk.up()
	riuk.refresh()
      elif event.key == 'DOWN':
	riuk.down()
	riuk.refresh()
      elif event.key == 'ENTER':
        riuk.grip()
      elif event.key == 'ESCAPE':
        return -1

while not tdl.event.is_window_closed():
  riuk.draw()
  tdl.flush()
  res = handle_keys()
  if res == -1:
    break
 

