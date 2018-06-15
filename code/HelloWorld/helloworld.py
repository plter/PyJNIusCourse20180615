from jnius import autoclass

JavaLangSystem = autoclass("java.lang.System")
JavaLangSystem.out.println("Hello World")
