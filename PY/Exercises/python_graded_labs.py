def ryerson_letter_grade(pct):
	grade_dictionary = {(90, 150): 'A+',
						(85, 89): 'A',
						(80, 84): 'A-',
						(77, 79): 'B+',
						(73, 76): 'B',
						(70, 72): 'B-',
						(67, 69): 'C+',
						(63, 66): 'C',
						(60, 62): 'C-',
						(57, 59): 'D+',
						(53, 56): 'D',
						(50, 52): 'D-',
						(0, 49): 'F'}

	for grade_range in grade_dictionary:
		if pct >= grade_range[0] and pct <= grade_range[1]:
			return grade_dictionary[grade_range]

def is_ascending(items):
	for i in range(len(items)-1):
		if items[i] >= items[i+1]:
			return False
	return True

def double_until_all_digits(n, giveup = 1000):
	i = 0
	while i < giveup:
		if len(set(str(n))) == 10:
			return i
		n *= 2
		i += 1
	return -1

def caps_lock_stuck(text):
	caps_lock = False
	return_text = ''
	
	for character in text:
		if character.lower() == 'a':
			caps_lock = not caps_lock
		else:
			if caps_lock:
				if character.isupper():
					return_text += character.lower()
				else:
					return_text += character.upper()
			else:
				return_text += character
	return return_text

def scrabble_value(word, multipliers):
	scrabble_dict = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, "m":3, 
					 "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
	value = 0
	for i, letter in enumerate(word):
		value += scrabble_dict.get(letter) * multipliers[i]

	return value

def create_zigzag(rows, cols, start = 1):
	zigzag = [[start + col + row * cols for col in range(cols)] for row in range(rows)]

	for i in range(len(zigzag)):
		if i % 2 != 0:
			zigzag[i] = zigzag[i][::-1]

	return zigzag

def contains_bingo(card, numbers, centerfree = True):
	marked_board = [['X' for x in range(5)] for y in range(5)]

	if centerfree:
		marked_board[2][2] = 'O'

	for n, row in enumerate(card):
		for i, number in enumerate(row):
			if number in numbers:
				marked_board[n][i] = 'O'

	# Vertical Bingo
	for y in range(5):
		vertical_bingo = []
		for x in range(5):
			vertical_bingo.append(marked_board[y][x])
		if len(set(vertical_bingo)) == 1 and vertical_bingo[0] == 'O':
			return True

	# Horizontal Bingo
	for y in range(5):
		if len(set(marked_board[y])) == 1 and marked_board[y][0] == 'O':
			return True

	# Diagonal Bingo and Antidiagonal Bingo
	diagonal_bingo = []
	antidiagonal_bingo = []

	for n in range(5):
		diagonal_bingo.append(marked_board[n][n])
		antidiagonal_bingo.append(marked_board[n][4-n])

	if len(set(diagonal_bingo)) == 1 and diagonal_bingo[0] == 'O':
		return True

	if len(set(antidiagonal_bingo)) == 1 and antidiagonal_bingo[0] == 'O':
		return True

	return False

def group_equal(items):
	master_list = []
	section = []

	if len(items) == 1:
		return [items]

	for i, item in enumerate(items):
		if i == 0:
			section.append(item)
			continue

		if item == section[0]:
			section.append(item)

		else:
			master_list.append(section)
			section = [item]

		if i == len(items) - 1:
			master_list.append(section)
	
	return master_list

def recaman(n):
	recaman_series = [1]
	recaman_set = set(recaman_series)

	for i in range(2, n + 1):

		subtracted = recaman_series[-1] - i
		added = recaman_series[-1] + i

		if subtracted > 0 and subtracted not in recaman_set:
			recaman_series.append(subtracted)
			recaman_set.add(subtracted)
		
		else:
			recaman_series.append(added)
			recaman_set.add(added)

	return recaman_series

def running_median_of_three(items):
	return_list = items[:2]

	if len(items) < 2:
		return return_list

	for i in range(len(items) - 2):
		mini_list = [items[n] for n in range(i, i+3)]
		mini_list.remove(max(mini_list))
		mini_list.remove(min(mini_list))
		return_list.append(mini_list[0])

	return return_list

def detab(text, n = 8, sub = ' '):
	detabbed = ''
	
	for character in text:
		if character == '\t':
			while len(detabbed) % n != 0:
				detabbed += sub
		else:
			detabbed += character

	return detabbed

def reverse_ascending_sublists(items):
	
	sublists = []
	sublist = [items[0]]

	for item in items[1:]:
		if sublist[-1] < item:
			sublist.append(item)
		else:
			sublists.append(sublist)
			sublist = [item]

	sublists.append(sublist)

	return [n for i in list(map(reversed, sublists)) for n in i]

def hand_is_badugi(hand):
	numbers = [card[0] for card in hand]
	suits = [card[1] for card in hand]

	return len(set(numbers)) == len(set(suits)) == 4

def brangelina(first, second):
	import re

	pattern = re.compile(r'[aeiou]+')

	first_vowel_group = [match.regs[0] for match in pattern.finditer(first)]

	if len(first_vowel_group) == 1:
		pos = first_vowel_group[0][1] - 1
		first = first[:pos]

	else:
		pos = first_vowel_group[-2][1] - 1
		first = first[:pos]

	while second[0] not in ('a', 'e', 'i', 'o', 'u'):
		second = second[1:]
	
	return first + second

def can_balance(items):
	for index in range(len(items)):
		
		sumLeft = 0
		sumRight = 0
		
		for n, i in enumerate(items):
			if n < index:
				sumLeft += i * (index - n)

			if n > index:
				sumRight += i * (n - index)

		if sumLeft == sumRight:
			return index
	return -1

def sort_by_digit_count(items):
	import functools

	def is_larger_digit(item1, item2):
		item1_dict = {i: 0 for i in range(0, 10)}
		item2_dict = {i: 0 for i in range(0, 10)}

		for i in str(item1):
			item1_dict[int(i)] += 1

		for i in str(item2):
			item2_dict[int(i)] += 1

		for n in range(9, 0, -1):
			if item1_dict[n] > item2_dict[n]:
				return 1
			elif item2_dict[n] > item1_dict[n]:
				return -1

		if item1 > item2:
			return 1
		else:
			return -1

	return sorted(items, key=functools.cmp_to_key(is_larger_digit))

def count_divisors_in_range(start, end, n):

	if start < 0 and end > 0:
		return count_divisors_in_range(start, 0, n) + count_divisors_in_range(1, end, n)

	total = 0 

	if start % n == 0:
		total += 1
		start += 1

	if end % n == 0:
		total += 1
		end -= 1

	total += abs(end - start) // n
	return max(total, 0)

def expand_intervals(intervals):

	intervals = intervals.split(',')
	
	master = []

	for interval in intervals:
		try:
			lower, higher = map(int, interval.split('-'))
			master +=  [n for n in range(lower, higher + 1)]
		
		except:
			master += [int(interval)]

	return master

def bridge_hand_shape(hand):
	suits = {"spades": 0, "hearts": 0, "diamonds": 0, "clubs": 0}
	for card in hand:
		suits[card[1]] += 1

	return [suit for suit in suits.values()]

def milton_work_point_count(hand, trump = 'notrump'):
	CARD_TO_POINTS = {'ace': 4, 'jack': 1, 'queen': 2, 'king': 3}

	points = 0

	suits = {'spades': 0, 'hearts': 0, 'diamonds': 0, 'clubs': 0}

	for card in hand:
		
		try:
			points += CARD_TO_POINTS[card[0]]
		except:
			pass

		suits[card[1]] += 1

	if sorted(suits.values()) == [3, 3, 3, 4]:
		points -= 1

	for k, v in suits.items():
		if v == 0 and trump != 'notrump' and k != trump:
			points += 5
		
		if v == 1 and trump != 'notrump' and k != trump:
			points += 3
		
		if v == 5:
			points += 1
		
		if v == 6:
			points += 2
		
		if v >= 7:
			points += 3

	return points

def count_consecutive_summers(n):
	count = 1
	for i in range(1, n):

		summ = i

		while summ < n:
			i += 1
			summ += i
			if summ == n:
				count += 1
				break
			if summ > n:
				break
	return count


def winning_card(cards, trump = None):
	ranks = {'deuce' : 2, 'trey' : 3 , 'four' : 4, 'five' : 5,
         	 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9,
         	 'ten' : 10, 'jack' : 11, 'queen' : 12, 'king' : 13,
         	 'ace' : 14 }

	if trump is None:
		trump = cards[0][1]

	pile = [card for card in cards if card[1] == trump]

	return sorted(pile, key=lambda x: ranks[x[0]])[-1]


def iterated_remove_pairs(items):
	while True:
		changed = False
		for i in range(len(items) - 1):
			
			if items[i] == items[i + 1]:
				items.pop(i+1)
				items.pop(i)
				changed = True
				break

		if not changed:
			return items


def bridge_hand_shorthand(hand):
	shorthand = ''
	
	spades = [card[0] for card in hand if card[1] == 'spades']
	hearts = [card[0] for card in hand if card[1] == 'hearts']
	diamonds = [card[0] for card in hand if card[1] == 'diamonds']
	clubs = [card[0] for card in hand if card[1] == 'clubs']

	shorthand = ''

	for suit in (spades, hearts, diamonds, clubs):
		shorthand_piece = ''
		while True:
			if 'ace' in suit:
				shorthand_piece += 'A'
				suit.remove('ace')
				continue

			if 'king' in suit:
				shorthand_piece += 'K'
				suit.remove('king')
				continue

			if 'queen' in suit:
				shorthand_piece += 'Q'
				suit.remove('queen')
				continue

			if 'jack' in suit:
				shorthand_piece += 'J'
				suit.remove('jack')
				continue

			shorthand_piece += ''.join(['x' for x in suit])
			break

		if not shorthand_piece:
			shorthand_piece = '-'

		shorthand += shorthand_piece + ' '

	return shorthand.strip()


def give_change(amount, coins):

	current_coin = 0
	change = []

	while sum(change) != amount:
		change.append(coins[current_coin])
		if sum(change) > amount:
			change.pop(-1)
			current_coin += 1
	return change


def bulls_and_cows(guesses):

	import itertools
	output = []


	def calc_delta(list1, list2):

		delta = 0
		equal = 0

		for i in range(len(list1)):
			if list1[i] == list2[i]:
				equal += 1

			elif list1[i] in list2:
				delta += 1

		return delta, equal


	for x in guesses:
		guess, bull, cow = x

		guess = [i for i in str(guess)]

		if not output:
			all_possible = itertools.permutations('123456789', 4)
		else:
			all_possible = [i for i in output]
			output = []

		for possible in all_possible:
			delta, equal = calc_delta(guess, possible)

			if delta == cow and equal == bull:
				output.append(possible)

	return sorted([int(''.join(i)) for i in output])

def longest_palindrome(text):
	longest = ''
	
	for end in range(len(text), -1, -1):
		for start in range(0, end):
			section = text[start:end+1]
			
			if section == section[::-1] and len(section) >= len(longest):
				longest = section

	return longest

def words_with_given_shape(words, shape):
	matches = []
	for word in words:
		sh = []
		for i in range(len(word) - 1):
			if ord(word[i]) < ord(word[i + 1]):
				sh.append(1)
			elif ord(word[i]) == ord(word[i + 1]):
				sh.append(0)
			else:
				sh.append(-1)
		if sh == shape:
			matches.append(word)
	return matches

def frequency_sort(elems):
	d = {}
	ordered = sorted(elems)
	for elem in elems:
		d.setdefault(elem, 0)
		d[elem] += 1
	return sorted(ordered, key=lambda x: d[x], reverse=True)

def is_perfect_power(n):
	exponent = 2	
	while True:
		if 2**exponent > n:
			return False
		low = 2
		high = low
		while high ** exponent <= n:
			high *= 2
		while high - low > 1:
			middle = (high+low)//2
			if middle**exponent <= n:
				low = middle
			else:
				high = middle 
		if low**exponent==n:
			return True
		exponent += 1

def highest_n_scores(scores, n = 5):
	player_dict = {}
	for score in scores:
		player, points = score
		player_dict.setdefault(player, [])
		player_dict[player].append(points)
	
	output = []
	for player, score in player_dict.items():
		output.append((player, sum(sorted(score, reverse=True)[:n])))
	return output

def all_cyclic_shifts(text):
	cyclic_shifts = [text]
	for _ in range(len(text)-1):
		text = text[1:] + text[0]
		if text not in cyclic_shifts:
			cyclic_shifts.append(text)
	return sorted(cyclic_shifts)

def collapse_intervals(items):
	output = ''
	sublists = []

	if len(items) == 0:
		return ''

	if len(items) == 1:
		return str(items[0])

	current = [items[0]]

	for i in range(1, len(items)):

		if current[-1] + 1 == items[i]:
			current.append(items[i])

		else:
			sublists.append(current)
			current = [items[i]]

	sublists.append(current)

	for i in range(len(sublists)):

		if len(sublists[i]) == 1:
			output += str(sublists[i][0])

		else:
			output += str(sublists[i][0]) + '-' + str(sublists[i][-1])

		if i != len(sublists) - 1:
			output += ','

	return output

def fibonacci_sum(n):
	def fibonacci_list(n, lst=[1,2]):
		while lst[-1] < n:
			lst.append(lst[-1] + lst[-2])
		return lst

	fib_list = fibonacci_list(n)

	counter = len(fib_list) - 1
	fib_sum = []

	while n != 0:
		current = fib_list[counter]
		if n - current >= 0:
			n -= current
			fib_sum.append(current)

		counter -= 1

	return fib_sum

def postfix_evaluate(items):
	i = 0
	while True:
		if items[i] in ('*', '+', '-', '/'):

			operator = items.pop(i)
			num2 = items.pop(i - 1)
			num1 = items.pop(i - 2)

			if operator == '+':
				answer = num1 + num2
			elif operator == '-':
				answer = num1 - num2
			elif operator == '*':
				answer = num1 * num2
			else:
				if num2 == 0:
					answer = 0
				else:
					answer = num1 // num2
			
			items.insert(i-2, answer)
			i = -1

			if len(items) == 1:
				return items[0]

		i += 1

def factoring_factorial(n):
	import math

	def generate_primes(n):
		primes = [2]
		for i in range(2, n+1):
			if is_prime(i):
				primes.append(i)
		return primes

	def is_prime(n):
		for i in range(2, math.ceil(math.sqrt(n)+1)):
			if n % i == 0:
				return False
		return True

	def list2dict(lst):
		dictionary = {}
		for item in lst:
			dictionary.setdefault(item, 0)
			dictionary[item] += 1
		return dictionary

	primes_list = generate_primes(n)
	factors = []

	for factorial in range(2, n+1):
		index = 0
		while factorial != 1:
			divisor = primes_list[index]

			if factorial % divisor == 0:
				factorial /= divisor
				factors.append(divisor)

			else:
				index += 1

	return sorted([(k, v) for k, v in list2dict(factors).items()], key=lambda x: x[0])

def calkin_wilf(n):
	from fractions import Fraction
	calkin_wilf_series = [(1, 1)]
	amt_in_row = 1

	while True:
		while amt_in_row <= amt_in_row * 2:
			
			numerator = calkin_wilf_series[-amt_in_row][0]
			denominator = calkin_wilf_series[-amt_in_row][1]

			calkin_wilf_series.append((numerator, (numerator+denominator)))
			calkin_wilf_series.append(((numerator+denominator), denominator))

			if len(calkin_wilf_series) > n:
				numerator, denominator = calkin_wilf_series[n-1]
				return Fraction(numerator, denominator)

			amt_in_row += 1

def aliquot_sequence(n, giveup = 100):
	def find_factors(n):
		factors = [1]
		for i in range(2, n//2 + 1):
			if n % i == 0:
				factors.append(i)
		return factors

	sequence = [n]
	index = 0

	while sequence[-1] != 0 and len(sequence) != giveup:
		q = sum(find_factors(sequence[index]))

		if q in sequence:
			sequence.append(q)
			return sequence

		sequence.append(q)

		if q == 1:
			sequence.append(0)

		index += 1

	return sequence

def josephus(n, k):
	soldiers = list(range(1, n+1))
	order = []
	s = k - 1
	while True:
		if len(soldiers) == 1:
			return order + soldiers

		dead = soldiers.pop(s)
		order.append(dead)
		soldiers = list(filter(lambda x: x != dead, soldiers))

		while len(soldiers) < s:
			soldiers *= 2

		if (s + k) % len(soldiers) == 0:
			s = len(soldiers) - 1
		else:
			s = ((s + k) % len(soldiers)) - 1

def reverse_reversed(items):
	copy = []
	for item in reversed(items):
		if isinstance(item, list):
			copy.append(reverse_reversed(item))
		else:
			copy.append(item)
	return copy

def flatten(items):
	copy = []
	for item in items:
		if isinstance(item, list):
			copy += flatten(item)
		else:
			copy += [item]
	return copy

def prime_factors(n):
	import math
	def generate_primes(n):
		yield 2
		for i in range(2, n+1):
			if is_prime(i):
				yield i				

	def is_prime(n):
		for i in range(2, math.ceil(math.sqrt(n)+1)):
			if n % i == 0:
				return False
		return True

	factors = []
	primes = generate_primes(n)
	i = next(primes)

	while n != 1:
		if n % i == 0:
			n /= i
			factors.append(i)
		else:
			i = next(primes)

	return factors

def balanced_ternary(n):

	def convert_ternary(n):
		output = ''
		while n != 0:
			output = str(n%3) + output
			n = n//3
		return list(map(lambda x: int(x), list(output)))

	if n > 0:
		negative = False
	elif n < 0:
		n = -n
		negative = True
	else:
		return [0]

	normal_ternary = convert_ternary(n)
	
	for i in range(len(normal_ternary)-1, -1, -1):
		if normal_ternary[i] == 2:
			normal_ternary[i] = -1
			if i != 0:
				normal_ternary[i-1] += 1
			else:
				normal_ternary = [1] + normal_ternary
		
		elif normal_ternary[i] == 3:
			normal_ternary[i] = 0
			if i != 0:
				normal_ternary[i-1] += 1
			else:
				normal_ternary = [1] + normal_ternary

	mult = 1
	for i in range(len(normal_ternary)-1, -1, -1):
		normal_ternary[i] *= mult
		mult *= 3

	normal_ternary = list(filter(lambda x: x != 0, normal_ternary))

	if negative:
		normal_ternary = list(map(lambda x: -x, normal_ternary))

	return normal_ternary

def fibonacci_word(k):
	import math
	golden_ratio = (1+5**(1/2))/2

	return str(math.floor((k+1)*golden_ratio) - math.floor(k*(golden_ratio)) - 1)