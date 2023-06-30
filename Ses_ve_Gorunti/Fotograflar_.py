import sys
sys.path.append(
    r"C:\Users\huaweı\Desktop\Masaüstü\YAZILIM\python\python_Çalışmalarım\Python_ile_Okul_Canli_dersten")
from Main.Dosya_islemleri import *
import random
import os
from typing import Tuple
import cv2
from Robot_musun import Robot_musun


class Resim_göster():
    def __init__(self, resim_adi: str, yazi: str, loaction: tuple) -> None:
        
        self.Resim_adi = resim_adi
        self.yazi = yazi
        self.Location = loaction

    @property
    def Resim_adi(self) -> str:
        return self.__resim_adi

    @Resim_adi.setter
    def Resim_adi(self, value: str):
        value = str(value)
        if value.isalnum() or value.isdigit():
            raise OverflowError("Ne yapıyon be abi gözünü seviyimn be abla")

        self.__resim_adi = value

    @property
    def Location(self):
        return self.__location

    @Location.setter
    def Location(self, value: Tuple[int, int]):
        if not isinstance(value, tuple):
            raise ResourceWarning("Hello be abi good by be abla")

        sayac = 0

        for i in value:
            if not isinstance(i, int):
                raise KeyError("Bir Hata")
            sayac += 1
        if sayac != 2:
            raise UserWarning("Ne giriyon be abi")

        self.__location = value

    def resim_editle(self):
        self.file = cv2.imread(self.Resim_adi)

        cv2.putText(self.file, self.yazi, self.Location,
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 200))

        cv2.imshow("Robot musun", self.file)

        cv2.waitKey(0)

    @classmethod
    def create_resim(cls):
        dosya = Dosya_düzenleme(
            "Fotograflar", "png", "resim", os.getcwd() + os.sep + "Ses_ve_Gorunti" + os.sep)
        dosya()  # Obje callable bir obje olduğu için böyle çağırdım
        random_file = "Ses_ve_Gorunti" + os.sep + "Fotograflar" + os.sep + \
            str(random.choice(os.listdir(os.getcwd() + os.sep +
                "Ses_ve_Gorunti" + os.sep + "Fotograflar")))

        print(random_file)

        random_location = (random.randint(0, 458), random.randint(0, 458))
        random_yazi = Robot_musun.rastgele_olustur(True, False, False, 8)

        return cls(random_file, random_yazi.robot_test_sorusu_string,  random_location)

resim1 = Resim_göster.create_resim()

resim1.resim_editle()
