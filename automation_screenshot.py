# from datetime import datetime
import datetime


def take_screenshot(my_driver):
    vDate = datetime.datetime.now().date()
    vHOUR = datetime.datetime.now().hour  # the current hour
    vMINUTE = datetime.datetime.now().minute  # the current minute
    vSECONDS = datetime.datetime.now().second  # the current second
    result = str(vDate)+"_ts"+str(vHOUR)+str(vMINUTE)+str(vSECONDS)
    my_driver.get_screenshot_as_file(
        f"C:\\Users\\gayat\\PycharmProjects\\pythonProject\\0304pyprojj1\\c_screenshots\\testrun{result}.png")
