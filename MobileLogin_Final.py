import os
import time
class Android:
    def __init__(self, id):
        self.ID=id

    def wakeup(self):
        cmd='adb -s ' + self.ID + ' shell input keyevent KEYCODE_WAKEUP'
        result=self.executeCmd(cmd)
    def home(self):
        cmd = 'adb -s ' + self.ID + ' shell input keyevent KEYCODE_HOME'
        result=self.executeCmd(cmd)
    def lock(self):
        cmd = 'adb -s ' + self.ID + ' shell input keyevent KEYCODE_POWER'
        result=self.executeCmd(cmd)
    def unlock(self):
        cmd = 'adb -s ' + self.ID + ' shell input swipe 440 1000 440 100 100'
        result=self.executeCmd(cmd)
    def clearLog(self):
        cmd = 'adb -s ' + self.ID + ' logcat -c'
        self.executeCmd(cmd)

    def executeCmd(self,cmd):
        process = os.popen(cmd)
        stdout= process.read()
        return stdout

    def buttonPress(self,x,y):
        cmd='adb -s ' + self.ID + ' shell input tap ' + str(x) + ' ' + str(y)
        self.executeCmd(cmd)

    def result(self):
        cmd='adb -s ' + self.ID + ' logcat -d'
        result=self.executeCmd(cmd)
        if "OAuth authorization success" in result:
            return 1
        else:
            return 0

    def openApp(self,app):
        cmd='adb -s ' + self.ID + ' shell am start -n ' + app
        self.executeCmd(cmd)
    def stopApp(self,app):
        cmd='adb -s ' + self.ID + ' shell am force-stop ' + app
        self.executeCmd(cmd)
    def inputText(self, txt):
        cmd = 'adb -s ' + self.ID + ' shell input text ' + txt
        self.executeCmd(cmd)

if __name__ == "__main__":
    # Create object for the device need device ID
    myAndroidPhone=Android('ZY323FDNKZ')
    # Preconditioning
    myAndroidPhone.home()
    myAndroidPhone.lock()
    myAndroidPhone.wakeup()
    time.sleep(1)
    myAndroidPhone.unlock()
    # close and Open Outlook App
    myAndroidPhone.stopApp('com.microsoft.office.outlook')
    myAndroidPhone.openApp('com.microsoft.office.outlook/.MainActivity')
    time.sleep(3)
    # based on the device login pages this can be scaled to any other device depending on the screen size
    myAndroidPhone.buttonPress(377,1012)
    time.sleep(3)
    myAndroidPhone.inputText('testing1234567@outlook.com')
    myAndroidPhone.buttonPress(628, 727)
    time.sleep(6)
    myAndroidPhone.clearLog()
    myAndroidPhone.inputText('abcdefge')
    myAndroidPhone.buttonPress(575, 673)
    time.sleep(3)
    if myAndroidPhone.result():
        print("Login Success")
    else:
        print("Login Failure")
