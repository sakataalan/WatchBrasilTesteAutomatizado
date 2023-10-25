from behave import *
from helpers.ScreenshotHelpers import make_screenshot_dir

class BaseStep:
    @then(u'Take screenshot')
    def take_screenshot(context):
        screenshot_dir = make_screenshot_dir(str(context.scenario))
        print(screenshot_dir)
        context.driver.save_screenshot(screenshot_dir)
 
