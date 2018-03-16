'''

 -- Multi Camera --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

from cscore import CameraServer

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb1 = cs.startAutomaticCapture(name="Front", path='/dev/v4l/by-path/platform-ci_hdrc.0-usb-0:1.1:1.0-video-index0')
    # usb2 = cs.startAutomaticCapture(name="Rear", path='/dev/v4l/by-path/platform-ci_hdrc.0-usb-0:1.2:1.0-video-index0')

    usb1.setFPS(10)
    # usb2.setFPS(10)

    usb1.setResolution(400, 300)
    # usb2.setResolution(400, 300)

    cs.waitForever()