# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი

# def sum_numbers(n=5):
#     total_number = 0
#     for i in range(n):
#         num = float(input("Enter a number: "))
#         total_number = total_number + num
#     return total_number
# print(sum_numbers())



# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

def my_function(*args):
    lst = [1, 3, 43, 212, 12, 23, 5, 4, 49, 52, 6, 7, 86, 76]
    odd_number = []
    even_number = []
    for i in lst:
        if i % 2 == 0:
            even_number.append(i)
        else:
            odd_number.append(i)
    return odd_number, even_number

odd_numbers, even_numbers = my_function()
print(f" კენტი რიცხვები :{odd_numbers}")
print(f" ლუწი რიცხვები :{even_numbers}")



#3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
   # და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
   # შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
   # ჰქონდეს მნიშვნელობა!)


def count_and_seperate():

    text = "This is a test. This test is fun.".lower()
    text_split = text.split()
    empty_dict = {}

    for i in text_split:
        if i in empty_dict:
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
        print()
    return empty_dict
print(count_and_seperate())







