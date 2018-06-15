import jnius_config
import os

java_class_path = os.path.join(os.path.dirname(__file__), 'JavaApp', 'out', 'artifacts', 'JavaApp_jar', 'JavaApp.jar')

print(java_class_path)

jnius_config.add_classpath(java_class_path)

from jnius import autoclass

Main = autoclass("top.yunp.Main")
Main.main([])
