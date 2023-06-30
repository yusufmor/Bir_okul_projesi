import os
import re


class Dosya_düzenleme():  # Bu class bir klasördeki dosyaları adını isteğe bağli olarak değiştirmek için yapılmıştır
    def __init__(self, hangi_dosya: str, dosya_uzantisi: str, ad: str, dosya_yolu: str):
        """Dosya oluşturuluken

        Args:
            hangi_dosya (str): Ariyicaği dosya adi
            dosya_uzantisi (str): Içindeki dosylarin uzantisi
            ad (str): Içindeki dosyalarin değiştirileceği ad 
            dosya_yolu (str): Ariyacağin dosyanın içinde oluduğu clasör Full path giriniz 
        """
        self.Hangi_dosya = hangi_dosya
        self.Dosya_uzantisi = dosya_uzantisi
        self.Ad = ad
        self.Dosya_yolu = dosya_yolu

    @property
    def Ad(self):
        return self.__ad

    @Ad.setter
    def Ad(self, value):
        self.__ad = None
        value = str(value)
        self.__ad = value

    @property
    def Hangi_dosya(self):
        return self.__hangi_dosya

    @Hangi_dosya.setter
    def Hangi_dosya(self, value: str):
        self.__hangi_dosya = None
        value = str(value)
        self.__hangi_dosya = value

    @property
    def Dosya_uzantisi(self):
        return self.__dosya_uzantisi

    @Dosya_uzantisi.setter
    def Dosya_uzantisi(self, value: str):
        self.__dosya_uzantisi = None
        value = str(value)
        self.__dosya_uzantisi = value

    @property
    def Dosya_yolu(self):
        return self.__dosya_yolu

    @Dosya_yolu.setter
    def Dosya_yolu(self, value: str):
        """Dosya_yolu

        Args:
            value (str): Ful path giriniz
        """

        value = str(value)

        if value.isalnum():
            if "_" in value:
                pass
            else:
                raise MemoryError("Ne ypıyon be dayi oğli")

        try:
            value = re.search(
                value, f"(?<Disk>\w:\{os.sep})(?<Gerikalan_Yol>[\w\dıüçşöğ]+\{os.sep})+")
        except BaseException:
            value.replace("\\", "\\\\")

        if value == None:
            raise ChildProcessError("Yalnış değer girdiniz")
        self.__dosya_yolu = value

    def __call__(self):  # Obje fonksiyon gibi çağrıldığında çalışacak fonksiyon
        if not os.path.isdir(self.Dosya_yolu + self.Hangi_dosya):
            os.mkdir(self.Dosya_yolu + self.Hangi_dosya)
            print(self.Hangi_dosya, "is created")

        sayac = 0
        a = False

        for i in os.listdir(self.Dosya_yolu + self.Hangi_dosya):
            try:

                uzanti = i.split(".")

                if uzanti[1] != self.Dosya_uzantisi:
                    os.remove(self.Dosya_yolu + os.sep +
                              self.Hangi_dosya + os.sep + i)
                    continue
                

            except IndexError:
                os.remove(self.Dosya_yolu + self.Hangi_dosya + os.sep + i)
                uzanti = [0 , self.Dosya_uzantisi]
                a = True
            if not a:
                sayac += 1
                os.renames(self.Dosya_yolu + "{}\{}".format(
                    self.Hangi_dosya, i), self.Dosya_yolu + "{}\{}".format(self.Hangi_dosya, f"{self.Ad}{sayac}.{self.Dosya_uzantisi}"))
