# Enable this plugin by removing the '_' at the start of the filename.

def onLoad():
    _thisFunctionWillNotBeExecutedByExtensionLoader()

def preHook():
    pass

def afterHook():
    pass

def _thisFunctionWillNotBeExecutedByExtensionLoader():
    print("Hello, World!")