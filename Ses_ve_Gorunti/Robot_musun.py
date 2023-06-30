import random


class Robot_musun:
    @classmethod
    def rastgele_olustur(cls, sayisal_agirlikli: bool = False, sozel_agirlikli: bool = False, alf_numeric_agirlikli: bool = False, hane: int = 8):
        """Rastgele sayi oluştuır

        Bu fonksiyon sayesinde otomatik olarak rastgele bir string oluşturulur

        Args:
            sayisal_agirlikli (bool): bool Eğer string'in içinde sayisal agirlik olsun diyorsanız True giriniz ..:
            sozel_agirlikli (bool): bool Eğer string'in içinde sozel agirlik olsun diyors anız True giriniz ..:
            alf_numeric_agirlikli (bool): bool Eğer string'in içinde alfanumeric karakter agirlik olsun diyorsanız True giriniz ..:
            hane (int): Kaç haneli olsun

        Returns:
            str: Döenen Değer string'tir
        """
        hane = int(hane)
        sayisal_agirlikli = bool(sayisal_agirlikli)
        sozel_agirlikli = bool(sozel_agirlikli)
        alf_numeric_agirlikli = bool(alf_numeric_agirlikli)

        if hane <= 4:
            TypeError("Hane Sıfırdan Büytük olmalı")

        agirlik = round(hane * 0.6, 0)
        azinlik = round(hane * 0.2, 0)

        if not (sayisal_agirlikli == sozel_agirlikli) != alf_numeric_agirlikli\
                and alf_numeric_agirlikli == True:
            return cls(azinlik, azinlik // 2, azinlik // 2, agirlik)

        elif not (alf_numeric_agirlikli == sozel_agirlikli) != sayisal_agirlikli\
                and sayisal_agirlikli == True:
            return cls(agirlik, azinlik // 2, azinlik // 2, azinlik)

        elif not (sayisal_agirlikli == alf_numeric_agirlikli) != sozel_agirlikli\
                and sozel_agirlikli == True:
            return cls(azinlik, agirlik // 2, agirlik // 2, azinlik)

        else:
            raise Warning("Ne yapıyon be abi gözünü seviyim be abla")

    def __init__(self, number: int = 1, b_char: int = 1, s_char: int = 1, alf_numeric_karakter: int = 1) -> None:
        self.number_no = number
        self.b_char_no = b_char
        self.s_char_no = s_char
        self.alfa_numeric_karakter_no = alf_numeric_karakter
        self.hane = number + b_char + s_char + alf_numeric_karakter
        self.robot_test_sorusu_string = self.robot_musun_test_sorusu()

    """
        number_no = Bu değişkenin içinde robotmusnun metininde kaç tane                 #! SAYI olduğunu söyler
        b_char_no = Bu değişkenin içinde robotmusnun metininde kaç tane                 #! BÜYÜK HARF olduğunu söyler
        s_char_no = Bu değişkenin içinde robotmusnun metininde kaç tane                 #! KÜÇK HARF olduğunu söyler
        alfa_numeric_karakter_no = Bu değişkenin içinde robotmusnun metininde kaç tane  #! ALFA NUMERİC KARAKTER OLACAĞINI SÖYLER olduğunu söyler
    """

    def random_number(self) -> int:  # Random number karakter
        numbers_list = []  # Bu listenin içinde rastgele sayılar tutulacak

        i = 0  # Döngü değişkeni

        while i < self.number_no:
            random_number = random.randint(0, 9)  # Rastgele sayı oluşturur
            numbers_list.append(random_number)  # Onu ekler
            i += 1  # İ artar
        return numbers_list

    def random_s_char(self) -> int:  # Random small char karakter
        s_char_list = []

        i = 0
        while i < self.b_char_no:
            random_number = random.randint(97, 122)
            s_char_list.append(chr(random_number))
            i += 1
        return s_char_list

    def random_b_char(self) -> int:  # Random Big char karakter
        b_char_list = []

        i = 0
        while i < self.b_char_no:
            random_number = random.randint(65, 89)
            b_char_list.append(chr(random_number))
            i += 1
        return b_char_list

    def random_alfa_numeric_char(self) -> int:

        alfa_numeric_list = []

        i = 0

        while i < self.alfa_numeric_karakter_no:
            random_number1 = random.randint(33, 47)
            random_number2 = random.randint(58, 64)
            random_number3 = random.randint(91, 96)
            random_number4 = random.randint(123, 126)
            random_deger = random.choice([chr(random_number1), chr(
                random_number2), chr(random_number3), chr(random_number4)])

            alfa_numeric_list.append(random_deger)
            i += 1

        return alfa_numeric_list

    # Burada olan işlem bir sonuç string'in içine rastgele olarak deger atar
    def robot_musun_test_sorusu(self) -> str:
        result_string = str()

        random_list = set()

        for i in [self.random_alfa_numeric_char(), self.random_b_char(), self.random_number(), self.random_s_char()]:
            for i1 in i:
                random_list.add(i1)
        for i in random_list:
            result_string = result_string + str(i)

        return result_string

    def Robot_mu(self, return_answer: str) -> bool:
        is_bot = False
        if self.robot_test_sorusu_string == return_answer:
            is_bot = True
        else:
            raise BaseException("Seni gidi robot seni")
        return is_bot