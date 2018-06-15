import jnius_config, os

jnius_config.add_classpath(os.path.join(os.path.dirname(__file__), "java", "out", "production", 'java'))

from jnius import autoclass, PythonJavaClass, java_method


class PythonAPI(PythonJavaClass):
    __javainterfaces__ = ["top/yunp/IPythonAPI"]

    def __init__(self):
        super(PythonAPI, self).__init__()

    @java_method("()V")
    def say_hello(self):
        print("Hello Python")


Main = autoclass("top.yunp.Main")
Main.addApi(PythonAPI())
