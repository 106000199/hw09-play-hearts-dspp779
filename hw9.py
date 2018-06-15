# -*- coding: utf-8 -*-
from itertools import product
import random


def init_all_cards():
    suits = '♣♦♠♥'
    numbers = list(range(1, 14))
    return ["{0}{1}".format(suit, number) for suit,
            number in product(suits, numbers)]
    # 產生所有poker


def get_legal_moves(cards_you_have, cards_played, heart_broken=False):
    # write your code ...
    legal_cards = []
    # '♣2'
    if '♣2' in cards_you_have:
        legal_cards = ['♣2']
        return legal_cards
    else:
        if cards_played:  # 我不是頭家
            suit = cards_played[0][0]  # 找出這局花色
            for card in cards_you_have:
                if card.startswith(suit):
                    legal_cards.append(card)
            if legal_cards:
                return legal_cards
            else:  # 缺門棒棒
                return cards_you_have
        else:  # 我是頭家
            if not heart_broken:
                for card in cards_you_have:
                    if not card.startswith('♥'):
                        legal_cards.append(card)
                if legal_cards:
                    return legal_cards
                else:  # 只有紅心時不用管是否心碎 不燃沒牌可出
                    return cards_you_have
            else:  # 心碎了 好桑心
                return cards_you_have


def compute_score(cards):
    loser_score = 0
    for card in cards:
        if card.startswith('♥'):
            loser_score += 1
    if '♠12' in cards:  # 葛萊芬多扣13分
        loser_score += 13
    return loser_score


def get_good_moves(cards_you_have, cards_played, heart_broken=False):
    # write your code ...
    card_score = {}
    all_numbers = []
    can_only_play = []
    candidates = get_legal_moves(cards_you_have, cards_played, heart_broken)

    if '♣2' in candidates:
        can_only_play = ['♣2']
        return can_only_play
    else:
        if cards_played:

            # 紀錄牌面上出現-->所有有效牌的最大值
            suit = cards_played[0][0]
            for card in cards_played:
                if card.startswith(suit):
                    all_numbers.append(int(card[1:]))
            if 1 in all_numbers:
                max_number = 1
            else:
                max_number = max(all_numbers)

            # 算: 打啥牌最划算
            for card in candidates:
                card_num = int(card[1:])
                if card.startswith(suit) and (max_number != 1
                                              and card_num > max_number):
                                        # or card == 1:
                    score = compute_score(cards_played + [card])
                else:  # 缺門
                    score = 0
                card_score[card] = score

            min_score = min(card_score.values())
            hhh = []
            for card in candidates:
                if card_score[card] == min_score:
                    hhh.append(card)
            return hhh
        else:  # 我是頭家
            return candidates


def random_cards(cards):
    while True:
        cards_you_have = random.sample(cards, random.choice(range(1, 13)))
        cards_played = random.sample(cards, random.choice(range(4)))

        if any(card.startswith('♥') or card == '♠12' for card in cards_played):
            heart_broken = True
        else:
            heart_broken = random.choice([True, False])

        if all(card not in cards_you_have for card in cards_played):
            return cards_you_have, cards_played, heart_broken


test = [
 {
    'cards_you_have': ['♦13', '♣9', '♥3',
                       '♦9', '♦6', '♣11', '♠6', '♥13', '♠13'],
    'cards_played': ['♥11', '♣6'],
    'heart_broken': True,
    # 'cards_you_can_play': ['♥3', '♥13'],
    # 'cards_you_should_play': ['♥3']
 },
 {
    'cards_you_have': ['♥2', '♥3', '♥4',
                       '♥5', '♥6', '♥10', '♥11', '♣11', '♠6'],
    'cards_played': [],
    'heart_broken': False,
    # 'cards_you_can_play': ['♣11', '♠6'],
    # 'cards_you_should_play': ['♣11', '♠6']
 },
 {
    'cards_you_have': ['♥4', '♦11', '♥12',
                       '♦2', '♦12', '♣4', '♥8'],
    'cards_played': ['♠2', '♠10', '♣6'],
    'heart_broken': False,
    # 'cards_you_can_play': ['♥4', '♦11', '♥12', '♦2', '♦12', '♣4', '♥8'],
    # 'cards_you_should_play': ['♥4', '♦11', '♥12', '♦2', '♦12', '♣4', '♥8']
 },
 {
    'cards_you_have': ['♥2', '♥3', '♥4', '♥5',
                       '♥6', '♥10', '♥11'],
    'cards_played': [],
    'heart_broken': False,
    # 'cards_you_can_play': ['♥2', '♥3', '♥4', '♥5', '♥6', '♥10', '♥11'],
    # 'cards_you_should_play': ['♥2', '♥3', '♥4', '♥5', '♥6', '♥10', '♥11']
 },
 {
    'cards_you_have': ['♦12', '♣1', '♣13', '♦10',
                       '♥2', '♦1', '♥13', '♣6', '♠4', '♠11', '♣10'],
    'cards_played': ['♠5', '♥4', '♣3'],
    'heart_broken': True,
    # 'cards_you_can_play': ['♠4', '♠11'],
    # 'cards_you_should_play': ['♠4']
 },
 {
    'cards_you_have': ['♥4', '♦11', '♠3', '♥12',
                       '♦2', '♠8', '♠12', '♦12', '♣4', '♥8', '♥2', '♣6', '♣2'],
    'cards_played': [],
    'heart_broken': False,
    # 'cards_you_can_play': ['♣2'],
    # 'cards_you_should_play': ['♣2']
 },
 {
    'cards_you_have': ['♥4', '♦11', '♠3', '♥12',
                       '♦2', '♠8', '♠12', '♦12', '♣4', '♥8'],
    'cards_played': ['♠2', '♠7', '♣6'],
    'heart_broken': True,
    # 'cards_you_can_play': ['♠3', '♠8', '♠12'],
    # 'cards_you_should_play': ['♠3', '♠8']
 }]

if __name__ == '__main__':
    cards = init_all_cards()
    # cards.remove('♣2')

    for _ in range(10):
        cards_you_have, cards_played, heart_broken = random_cards(cards)
        # cards_you_have, cards_played, heart_broken = test

        print("You have:", ', '.join(cards_you_have))
        print("Cards played:", cards_played)

        cards_you_can_play = get_legal_moves(cards_you_have,
                                             cards_played, heart_broken)
        cards_you_should_play = get_good_moves(cards_you_have,
                                               cards_played, heart_broken)
        print("You can play:", ', '.join(cards_you_can_play))
        print("You should play:", ', '.join(cards_you_should_play))

        print()
