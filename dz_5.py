# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'У абв лукоморья дуб зелёный; Златая абв цепь на дубе том: И днём абв и ночью кот учёный Всё абв ходит по цепи кругом'
# print('Исходный текст: ', text)
# text_word = text.split()
# find = 'абв'
# new_text = []

# for i in text_word:
#     if find not in i:
#         new_text.append(i)

# text_2 = ' '.join(new_text) 
# print('Полученный текст: ', text_2)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после 
# друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 
# 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет 
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


# from random import randint
# candies = int(input('Сколько конфет: '))
# take = int(input("Максимальное количество конфет можно взять: "))
# # сколько нужно взять конфет для победы:
# def take_to_have_for_first(candies, take):
#     take_candies = candies % (take + 1)
#     if take_candies == 0:
#         take_candies = take
#     return(f'чтобы выиграть первому ходящему необходимо взять {take_candies}')
# first_move = randint(1,2) # определяем, кто ходит первым кто вторым
# print(f"Первым ходит игрок {first_move}")
# second_move = 3 - first_move
# print(f'Второй ходит игрок {second_move}')
# count = 0
# while candies > 0:
#     count += 1
#     player1 = int(input("Ход первого игрока. Возьмите конфеты: "))
#     candies = candies - player1
#     print(f'осталось конфет: {candies}')
#     print(take_to_have_for_first(candies, take))
#     if candies > 0:
#         player2 = int(input("Ход второго игрока. Возьмите конфеты: "))
#         candies = candies - player2
#         print(f'осталось конфет: {candies}')
#         print(take_to_have_for_first(candies, take))
# if candies == 0:
#     print('Игра окончена')
# if take % 2 != 0:
#     print(f'Победил игрок {first_move}')
# else:
#     print(f'Победил игрок {second_move}')


# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import *
# import os
# os.system("cls")

# greeting = ('Вас приветствует игра "Забери конфеты!"\n'
#             'Основные правила игры: \n'
#             'Дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы договоримся. \n'
#             'Итак, начнём!\n')

# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# def candy(n):  # выбираем окончание для слова конфеты
#     if n == 1 or n % 10 == 1:
#         return 'а'
#     elif 1 < n < 5 or 1 < n % 10 < 5:
#         return 'ы'
#     else:
#         return ''


# def introduce_players():
#     player1 = input('Давайте знакомиться. Как Вас зовут? ')
#     print(f'Очень приятно, меня зовут {os.getlogin()}')
#     return [player1, os.getlogin()]


# def get_rules(players):
#     n = int(input('Сколько конфет будем разыгрывать? '))
#     m = int(input('Сколько максимально будем брать конфет за один ход? '))     
#     first = input(
#     f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу ')
#     if first != '1':
#         first = 0
#         return [n, m, int(first)]


# def get_rules(players):
#     n = int(input('Сколько конфет будем разыгрывать? '))
#     m = int(input('Сколько максимально будем брать конфет за один ход? '))
#     first = input(
#         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу ')
#     if first != '1':
#         first = 0
#     return [n, m, int(first)]


# def play_game(rules, players, messages):
#     count = rules[2]
#     print(count)

#     while rules[0] > 0:
#         if not count % 2:
#             move = rules[0] % (rules[1] + 1)
#             if move == 0:
#                 move = rules[1]
#             print(f'Я забираю {move} конфет{candy(move)}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(f'Это слишком много, можно взять не более {rules[1]} конфет{candy(rules[1])}, у нас всего {rules[0]} конфет{candy[rules[0]]}')
#                 attempt = 3
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{candy(rules[0])}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[count % 2]


# print(greeting)

# players = introduce_players()
# rules = get_rules(players)

# winer = play_game(rules, players, messages)
# print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!\n')


# 3.Создайте программу для игры в ""Крестики-нолики"".


# import os
# os.system("cls")

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "Вы выиграли!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_encode.txt', 'w') as data:
    data.write('fffggggggggqqqqqqqUUUUUUUUU')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Исходные данные: \t' + decoded_string)
print('Декодированные данные: \t' + rle_encode(decoded_string))