import picamera
import logging
import sys
from datetime import datetime
from aws import upload_file


# logging settings
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)


if __name__ == "__main__":
    logging.info("Starting Recording")
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.start_recording("local_footage.h264")
    camera.wait_recording(60)  # seconds
    camera.stop_recording()
    logging.info("Finished Recording")
    upload_file("local_footage.h264")
