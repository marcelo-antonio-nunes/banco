import os
import platform


class Utils:
    def limpa_tela(self, ) -> None:
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
