import random


class Robot_musun:
    def oto_deger_ata(func):
        def wrapper(self):

            random_deger1 = random.randint(1, 10)
            random_deger2 = random.randint(1, 10)
            random_deger3 = random.randint(1, 10)
            random_deger4 = random.randint(1, 10)
            random_deger5 = random_deger1 + random_deger2 + random_deger3 + random_deger4

            func(self, random_deger5, random_deger1,
                 random_deger2, random_deger3, random_deger4)
            
        return wrapper

    @oto_deger_ata
    def __init__(self, hane=4, number=1, b_char=1, s_char=1, alf_numeric_karakter=1) -> str:
        self.hane = hane
        self.number_no = number
        self.b_char_no = b_char
        self.s_char_no = s_char
        self.alfa_numeric_karakter_no = alf_numeric_karakter

        if self.number_no + self.b_char_no + self.s_char_no + self.alfa_numeric_karakter_no != self.hane:
            raise Exception("Hane sayısı yetersiz")

    """
        number_no = Bu değişkenin içinde robotmusnun metininde kaç tane                 #! SAYI olduğunu söyler
        b_char_no = Bu değişkenin içinde robotmusnun metininde kaç tane                 #! BÜYÜK HARF olduğunu söyler
        s_char_no = Bu değişkenin içinde robotmusnun metininde kaç tane                 #! KÜÇK HARF olduğunu söyler
        alfa_numeric_karakter_no = Bu değişkenin içinde robotmusnun metininde kaç tane  #! ALFA NUMERİC KARAKTER OLACAĞINI SÖYLER olduğunu söyler
    """

    def random_number(self):  # Random number karakter
        numbers_list = []  # Bu listenin içinde rastgele sayılar tutulacak

        i = 0  # Döngü değişkeni

        while i < self.number_no:
            random_number = random.randint(0, 9)  # Rastgele sayı oluşturur
            numbers_list.append(random_number)  # Onu ekler
            i += 1  # İ artar
        return numbers_list

    def random_s_char(self):  # Random small char karakter
        s_char_list = []

        i = 0
        while i < self.b_char_no:
            random_number = random.randint(97, 122)
            s_char_list.append(chr(random_number))
            i += 1
        return s_char_list

    def random_b_char(self):  # Random Big char karakter
        b_char_list = []

        i = 0
        while i < self.b_char_no:
            random_number = random.randint(65, 89)
            b_char_list.append(chr(random_number))
            i += 1
        return b_char_list

    def random_alfa_numeric_char(self):

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

    def robot_musun_test_sorusu(self): # Burada olan işlem bir sonuç string'in içine rastgele olarak deger atar
        result_string = str()

        random_list = set()

        for i in [self.random_alfa_numeric_char(), self.random_b_char(), self.random_number(), self.random_s_char()]:
            for i1 in i:
                random_list.add(i1)
        for i in random_list:
            result_string = result_string + str(i)
        self.robot_test_sorusu_string = result_string    
        return result_string
    
    def Robot_mu(self ,return_answer):
        is_bot = False
        if self.robot_test_sorusu_string == return_answer:
            is_bot = True
        else:
            raise BaseException("Seni gidi robot seni")
        return is_bot



# 33 ve 126
robotum = Robot_musun()
print(robotum.robot_musun_test_sorusu())
a = False
while a:
    a = input("Bir şey gir")
    robotum.Robot_mu(a)
