from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools

class HelloConan(ConanFile):
    name = "rgbmatrix"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = ["lib/*", "include/*"]

    def build(self):
        with tools.chdir("lib"):
            atools = AutoToolsBuildEnvironment(self)
            # atools.configure() # use it to run "./configure" if using autotools
            atools.make()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rgbmatrix"]