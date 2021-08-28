import unittest
import python_graded_labs

class TestExercises(unittest.TestCase):

	def test_ryerson_letter_grade(self):
		self.assertEqual(python_graded_labs.ryerson_letter_grade(45), 'F')
		self.assertEqual(python_graded_labs.ryerson_letter_grade(62), 'C-')
		self.assertEqual(python_graded_labs.ryerson_letter_grade(89), 'A')
		self.assertEqual(python_graded_labs.ryerson_letter_grade(107), 'A+')

	def test_is_ascending(self):
		self.assertEqual(python_graded_labs.is_ascending([-5, 10, 99, 123456]), True)
		self.assertEqual(python_graded_labs.is_ascending([99]), True)
		self.assertEqual(python_graded_labs.is_ascending([]), True)
		self.assertEqual(python_graded_labs.is_ascending([4, 5, 6, 7, 3, 7, 9]), False)
		self.assertEqual(python_graded_labs.is_ascending([1, 1, 1, 1]), False)

	def test_double_until_all_digits(self):
		self.assertEqual(python_graded_labs.double_until_all_digits(1, 1000), 68)
		self.assertEqual(python_graded_labs.double_until_all_digits(1234567890, 1000), 0)
		self.assertEqual(python_graded_labs.double_until_all_digits(555, 10), -1)

	def test_caps_lock_stuck(self):
		self.assertEqual(python_graded_labs.caps_lock_stuck("Why are you asking me that?"), "Why RE YOU sking me thT?")
		self.assertEqual(python_graded_labs.caps_lock_stuck("Madder than Mad Brian of Madcastle"), "MDDER THn MD bRIn of MDCstle")
		self.assertEqual(python_graded_labs.caps_lock_stuck("Why āre you ăsking me thąt?"), "Why āre you ăsking me thąt?")

	def test_scrabble_value(self):
		self.assertEqual(python_graded_labs.scrabble_value("hello", [1, 1, 1, 1, 1]), 8)
		self.assertEqual(python_graded_labs.scrabble_value("world", [1, 3, 1, 1, 1]), 11)

	def test_create_zigzag(self):
		self.assertEqual(python_graded_labs.create_zigzag(3, 5), [[1,2,3,4,5],[10,9,8,7,6],[11,12,13,14,15]])
		self.assertEqual(python_graded_labs.create_zigzag(10, 1), [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
		self.assertEqual(python_graded_labs.create_zigzag(4, 2), [[1,2],[4,3],[5,6],[8,7]])

	def test_contains_bingo(self):
		card1 = [[38, 93, 42, 47, 15], [90, 13, 41, 10, 56], [54, 23, 87, 70, 6], [86, 43, 48, 40, 92], [71, 24, 44, 1, 34]]
		numbers1 = [1, 2, 3, 4, 6, 8, 12, 13, 15, 16, 19, 21, 22, 24, 28, 34, 38, 40, 41, 42, 43, 45, 47, 49, 51, 53, 55, 57, 58, 62, 65, 66, 69, 70, 72, 82, 83, 84, 86, 88, 95, 97]

		card2 = [[89, 23, 61, 94, 67], [19, 85, 90, 70, 32], [36, 98, 57, 82, 20], [76, 46, 25, 29, 7], [55, 14, 53, 37, 44]]
		numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 31, 33, 35, 36, 37, 38, 39, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 68, 70, 71, 73, 75, 76, 77, 79, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 94, 98]
		
		self.assertEqual(python_graded_labs.contains_bingo(card1, numbers1), True)
		self.assertEqual(python_graded_labs.contains_bingo(card2, numbers2), True)

	def test_group_equal(self):
		self.assertEqual(python_graded_labs.group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]), [[1,1],[4,4,4],["hello","hello"],[4]])
		self.assertEqual(python_graded_labs.group_equal([1, 2, 3, 4]), [[1], [2], [3], [4]])
		self.assertEqual(python_graded_labs.group_equal([1]), [[1]])
		self.assertEqual(python_graded_labs.group_equal([]), [])

	def test_recaman(self):
		self.assertEqual(python_graded_labs.recaman(10), [1, 3, 6, 2, 7, 13, 20, 12, 21, 11])
		self.assertEqual(python_graded_labs.recaman(1000000)[-5:], [2057162, 1057165, 2057163, 1057164, 2057164])

	def test_running_median_of_three(self):
		self.assertEqual(python_graded_labs.running_median_of_three([5, 2, 9, 1, 7, 4, 6, 3, 8]), [5, 2, 5, 2, 7, 4, 6, 4, 6])
		self.assertEqual(python_graded_labs.running_median_of_three([1, 2, 3, 4, 5, 6, 7]), [1, 2, 2, 3, 4, 5, 6])
		self.assertEqual(python_graded_labs.running_median_of_three([42]), [42])

	def test_detab(self):
		self.assertEqual(python_graded_labs.detab("Hello\tthereyou\tworld", 8, '$'), "Hello$$$thereyouworld")
		self.assertEqual(python_graded_labs.detab("Ilkka\tMarkus\tKokkarinen", 4, '-'), "Ilkka---Markus--Kokkarinen")
		self.assertEqual(python_graded_labs.detab("Tenser,\tsaid\tthe\ttensor", 5, '+'), "Tenser,+++said+the++tensor")

	def test_reverse_ascending_sublists(self):
		self.assertEqual(python_graded_labs.reverse_ascending_sublists([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
		self.assertEqual(python_graded_labs.reverse_ascending_sublists([5, 7, 10, 4, 2, 7, 8, 1, 3]), [10, 7, 5, 4, 8, 7, 2, 3, 1])
		self.assertEqual(python_graded_labs.reverse_ascending_sublists([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])
		self.assertEqual(python_graded_labs.reverse_ascending_sublists([1, 2, 2, 3]), [2, 1, 3, 2])

	def test_hand_is_badugi(self):
		self.assertEqual(python_graded_labs.hand_is_badugi([("queen", "hearts"), ("six", "diamonds"), ("deuce", "spades"), ("jack","clubs")]), True)
		self.assertEqual(python_graded_labs.hand_is_badugi([("queen", "hearts"), ("six", "diamonds"), ("deuce", "spades"), ("queen","clubs")]), False)
		self.assertEqual(python_graded_labs.hand_is_badugi([("queen", "hearts"), ("six", "diamonds"), ("deuce", "spades"), ("jack","spades")]), False)

	def test_brangelina(self):
		self.assertEqual(python_graded_labs.brangelina("brad", "angelina"), "brangelina")
		self.assertEqual(python_graded_labs.brangelina("sheldon", "amy"), "shamy")
		self.assertEqual(python_graded_labs.brangelina("ross", "rachel"), "rachel")
		self.assertEqual(python_graded_labs.brangelina("britain", "exit"), "brexit")
		self.assertEqual(python_graded_labs.brangelina("bill", "hillary"), "billary")
		self.assertEqual(python_graded_labs.brangelina("donald", "melania"), "delania")
		self.assertEqual(python_graded_labs.brangelina("barack", "michelle"), "bichelle")

	def test_can_balance(self):
		self.assertEqual(python_graded_labs.can_balance([6,1,10,5,4]), 2)
		self.assertEqual(python_graded_labs.can_balance([10,3,3,2,1]), 1)
		self.assertEqual(python_graded_labs.can_balance([7,3,4,2,9,7,4]), -1)
		self.assertEqual(python_graded_labs.can_balance([42]), 0)

	def test_sort_by_digit_count(self):
		self.assertEqual(python_graded_labs.sort_by_digit_count([98, 19, 4321, 9999, 73, 241, 111111, 563, 33]), [111111, 33, 241, 4321, 563, 73, 19, 98, 9999])
		self.assertEqual(python_graded_labs.sort_by_digit_count([1234, 4321, 3214, 1243]), [1234, 1243, 3214, 4321])

		# This test works, it just takes 7 seconds
		# hundred_thousand = python_graded_labs.sort_by_digit_count(list(range(100000)))

		# self.assertEqual(hundred_thousand[:5], [0, 1, 10, 100, 1000])
		# self.assertEqual(hundred_thousand[-5:], [98999, 99899, 99989, 99998, 99999])

	def test_count_divisors_in_range(self):
		self.assertEqual(python_graded_labs.count_divisors_in_range(7, 28, 4), 6)
		self.assertEqual(python_graded_labs.count_divisors_in_range(-77, 19, 10), 9)
		self.assertEqual(python_graded_labs.count_divisors_in_range(-19, -13, 10), 0)
		self.assertEqual(python_graded_labs.count_divisors_in_range(1, 10**12 - 1, 5), 199999999999)
		self.assertEqual(python_graded_labs.count_divisors_in_range(0, 10**12 - 1, 5), 200000000000)
		self.assertEqual(python_graded_labs.count_divisors_in_range(0, 10**12, 5), 200000000001)
		self.assertEqual(python_graded_labs.count_divisors_in_range(-10**12, 10**12, 12345), 162008911)

	def test_expand_intervals(self):
		self.assertEqual(python_graded_labs.expand_intervals("4-6,10-12,16"), [4, 5, 6, 10, 11, 12, 16])
		self.assertEqual(python_graded_labs.expand_intervals("1,3-9,12-14,9999"), [1, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 9999])

	def test_bridge_hand_shape(self):
		self.assertEqual(python_graded_labs.bridge_hand_shape([('eight', 'spades'), ('king', 'diamonds'), ('ten', 'diamonds'), ('trey', 'diamonds'), ('seven', 'spades'), ('five', 'diamonds'), ('deuce', 'hearts'), ('king', 'spades'), ('jack', 'spades'), ('ten', 'clubs'), ('ace', 'clubs'), ('six', 'diamonds'), ('trey', 'hearts')]), [4, 2, 5, 2])
		self.assertEqual(python_graded_labs.bridge_hand_shape([('ace', 'spades'), ('six', 'hearts'), ('nine', 'spades'), ('nine', 'diamonds'), ('ace', 'diamonds'), ('trey', 'diamonds'), ('five', 'spades'), ('four', 'hearts'), ('trey', 'spades'), ('seven', 'diamonds'), ('jack', 'diamonds'), ('queen', 'spades'), ('king', 'diamonds')]), [5, 2, 6, 0])

	def test_milton_work_point_count(self):
		self.assertEqual(python_graded_labs.milton_work_point_count([('four', 'spades'), ('five', 'spades'), ('ten', 'hearts'), ('six', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts'), ('four', 'hearts'), ('deuce', 'hearts'), ('trey', 'diamonds'), ('seven', 'diamonds'), ('four', 'diamonds'), ('deuce', 'diamonds'), ('four', 'clubs')], 'diamonds'), 8)
		self.assertEqual(python_graded_labs.milton_work_point_count([('trey', 'spades'), ('queen', 'hearts'), ('jack', 'hearts'), ('eight', 'hearts'), ('six', 'diamonds'), ('nine', 'diamonds'), ('jack', 'diamonds'), ('ace', 'diamonds'), ('nine', 'clubs'), ('king', 'clubs'), ('jack', 'clubs'), ('five', 'clubs'), ('ace', 'clubs')], 'clubs'), 20)
		self.assertEqual(python_graded_labs.milton_work_point_count([('trey', 'spades'), ('seven', 'spades'), ('deuce', 'spades'), ('trey', 'hearts'), ('queen', 'hearts'), ('nine', 'hearts'), ('ten', 'diamonds'), ('six', 'diamonds'), ('queen', 'diamonds'), ('ace', 'diamonds'), ('nine', 'clubs'), ('four', 'clubs'), ('five', 'clubs')], 'notrump'), 7)

	def test_count_consecutive_summers(self):
		self.assertEqual(python_graded_labs.count_consecutive_summers(42), 4)
		self.assertEqual(python_graded_labs.count_consecutive_summers(99), 6)
		self.assertEqual(python_graded_labs.count_consecutive_summers(92), 2)

	def test_winning_card(self):
		self.assertEqual(python_graded_labs.winning_card([("trey", "spades"), ("ace", "diamonds"), ("jack", "spades"), ("eight", "spades")]), ("jack", "spades"))
		self.assertEqual(python_graded_labs.winning_card([("ace", "diamonds"), ("ace", "hearts"), ("ace", "spades"), ("deuce", "clubs")], "clubs"), ("deuce", "clubs"))
		self.assertEqual(python_graded_labs.winning_card([("deuce", "clubs"), ("ace", "diamonds"), ("ace", "hearts"), ("ace", "spades")]), ("deuce", "clubs"))

	def test_iterated_remove_pairs(self):
		self.assertEqual(python_graded_labs.iterated_remove_pairs([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]), [])
		self.assertEqual(python_graded_labs.iterated_remove_pairs(['bob', 'tom', 'jack', 'jack', 'bob', 42]), ['bob', 'tom', 'bob', 42])
		self.assertEqual(python_graded_labs.iterated_remove_pairs([42, 42, 42, 42, 42]), [42])
		self.assertEqual(python_graded_labs.iterated_remove_pairs([42, 5, 8, 2, 99, 99, 2, 7, 7, 8, 5]), [42])

	def test_bridge_hand_shorthand(self):
		self.assertEqual(python_graded_labs.bridge_hand_shorthand([('four', 'spades'), ('five', 'spades'), ('ten', 'hearts'), ('six', 'hearts'), ('queen', 'hearts'), ('jack', 'hearts'), ('four', 'hearts'), ('deuce', 'hearts'), ('trey', 'diamonds'), ('seven', 'diamonds'), ('four', 'diamonds'), ('deuce', 'diamonds'), ('four', 'clubs')]), "xx QJxxxx xxxx x")
		self.assertEqual(python_graded_labs.bridge_hand_shorthand([('trey', 'spades'), ('queen', 'hearts'), ('jack', 'hearts'), ('eight', 'hearts'), ('six', 'diamonds'), ('nine', 'diamonds'), ('jack', 'diamonds'), ('ace', 'diamonds'), ('nine', 'clubs'), ('king', 'clubs'), ('jack', 'clubs'), ('five', 'clubs'), ('ace', 'clubs')]), "x QJx AJxx AKJxx")
		self.assertEqual(python_graded_labs.bridge_hand_shorthand([('trey', 'spades'), ('seven', 'spades'), ('deuce', 'spades'), ('trey', 'hearts'), ('queen', 'hearts'), ('nine', 'hearts'), ('ten', 'diamonds'), ('six', 'diamonds'), ('queen', 'diamonds'), ('ace', 'diamonds'), ('nine', 'clubs'), ('four', 'clubs'), ('five', 'clubs')]), "xxx Qxx AQxx xxx")

	def test_give_change(self):
		self.assertEqual(python_graded_labs.give_change(64, [50, 25, 10, 5, 1]), [50, 10, 1, 1, 1, 1])
		self.assertEqual(python_graded_labs.give_change(123, [100, 25, 10, 5, 1]), [100, 10, 10, 1, 1, 1])
		self.assertEqual(python_graded_labs.give_change(100, [42, 17, 11, 6, 1]), [42, 42, 11, 1, 1, 1, 1, 1])

	def test_bulls_and_cows(self):
		self.assertEqual(python_graded_labs.bulls_and_cows([(1234, 2, 2)]), [1243, 1324, 1432, 2134, 3214, 4231])
		self.assertEqual(python_graded_labs.bulls_and_cows([(8765, 1, 0), (1234, 2, 1)]), [1245, 1263, 1364, 1435, 1724, 1732, 2734, 3264, 4235, 8134, 8214, 8231])
		self.assertEqual(python_graded_labs.bulls_and_cows([(1234, 2, 2), (4321, 1, 3)]), [])
		self.assertEqual(python_graded_labs.bulls_and_cows([(3127, 0, 1), (5723, 1, 0), (7361, 0, 2), (1236, 1, 0)]), [4786, 4796, 8746, 8796, 9746, 9786])

	def test_longest_palindrome(self):
		self.assertEqual(python_graded_labs.longest_palindrome("saippuakauppias"), "saippuakauppias")
		self.assertEqual(python_graded_labs.longest_palindrome("abaababaaabbabaababababaa"), "aababababaa")
		self.assertEqual(python_graded_labs.longest_palindrome("xxzxxracecar"), "racecar")
		self.assertEqual(python_graded_labs.longest_palindrome("xyxracecaryxy"), "racecar")
		self.assertEqual(python_graded_labs.longest_palindrome("ctozotcxcabatoyota"), "ctozotc")

	def test_words_with_given_shape(self):
		from collections import Counter
		words = ['twigger', 'cooja', 'oopak', 'twiggen', 'attic', 'brogger', 'swigger', 'boonk', 
		 		 'fligger', 'ettle', 'progger', 'kooka', 'eeler', 'swollen', 'dooja', 'apple', 
		 		 'grommet', 'proffer', 'prigger', 'attid', 'dooli', 'cooba', 'gooma', 'stollen', 
		 		 'joola', 'strolld', 'stiffen', 'coomb', 'essed', 'nutseed', 'arrie']
		self.assertEqual(Counter(python_graded_labs.words_with_given_shape(words, [1, -1, -1, -1, 0, -1])), Counter(['nutseed', 'strolld']))
		self.assertEqual(Counter(python_graded_labs.words_with_given_shape(words, [1, -1, -1, 0, -1, 1])), Counter(['brogger', 'fligger', 'grommet', 'prigger', 'proffer', 'progger', 'stiffen', 'stollen', 'swigger', 'swollen', 'twiggen', 'twigger']))
		self.assertEqual(Counter(python_graded_labs.words_with_given_shape(words, [1, 0, -1, -1])), Counter(['apple', 'arrie', 'attic', 'attid', 'boonk', 'cooba', 'cooja', 'coomb', 'dooja', 'dooli', 'essed', 'ettle', 'gooma', 'joola', 'kooka']))
		self.assertEqual(Counter(python_graded_labs.words_with_given_shape(words, [0, 1, -1, 1])), Counter(['eeler', 'oopak']))

	def test_frequency_sort(self):
		self.assertEqual(python_graded_labs.frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]), [4, 4, 4, 4, 2, 2, 6, 6])
		self.assertEqual(python_graded_labs.frequency_sort([4, 6, 1, 2, 2, 1, 1, 6, 1, 1, 6, 4, 4, 1]), [1, 1, 1, 1, 1, 1, 4, 4, 4, 6, 6, 6, 2, 2])
		self.assertEqual(python_graded_labs.frequency_sort([17, 99, 42]), [17, 42, 99])
		self.assertEqual(python_graded_labs.frequency_sort(['bob','bob','carl','alex','bob']), ['bob','bob','bob','alex','carl'])

	def test_is_perfect_power(self):
		self.assertEqual(python_graded_labs.is_perfect_power(42), False)
		self.assertEqual(python_graded_labs.is_perfect_power(441), True)
		self.assertEqual(python_graded_labs.is_perfect_power(469097433), True)
		self.assertEqual(python_graded_labs.is_perfect_power(12**34), True)
		self.assertEqual(python_graded_labs.is_perfect_power(12**34-1), False)

	def test_highest_n_scores(self):
		self.assertEqual(sorted(python_graded_labs.highest_n_scores([('bill', 10), ('jack', 6), ('sheldon', 3), ('tina', 2), ('amy', 3), ('sheldon', 6), ('tina', 7), ('jack', 2), ('bob', 3), ('bob', 4), ('bill', 3), ('bill', 9), ('sheldon', 5), ('amy', 2), ('jack', 7), ('sheldon', 5), ('sheldon', 7), ('bill', 1), ('bill', 9), ('sheldon', 5), ('bill', 2), ('bill', 6), ('jack', 6), ('bob', 4), ('tina', 5), ('sheldon', 4), ('sheldon', 2), ('amy', 6), ('bob', 7), ('jack', 2), ('bob', 5), ('sheldon', 9), ('jack', 5), ('amy', 9), ('bob', 7), ('tina', 6), ('tina', 2), ('amy', 7), ('jack', 10), ('tina', 4), ('bob', 5), ('jack', 10), ('bob', 7), ('jack', 5), ('amy', 4), ('amy', 8), ('bob', 4), ('bill', 8), ('bob', 6), ('tina', 6), ('amy', 9), ('bill', 4), ('jack', 2), ('amy', 2), ('amy', 4), ('sheldon', 1), ('tina', 3), ('bill', 9), ('tina', 4), ('tina', 9)], n=3), key=lambda x: x[0]), [('amy', 26), ('bill', 28), ('bob', 21), ('jack', 27), ('sheldon', 22), ('tina', 22)])

	def test_all_cyclic_shifts(self):
		self.assertEqual(python_graded_labs.all_cyclic_shifts('01001'), ['00101', '01001', '01010', '10010', '10100'])
		self.assertEqual(python_graded_labs.all_cyclic_shifts('010101'), ['010101', '101010'])
		self.assertEqual(python_graded_labs.all_cyclic_shifts('hello'), ['elloh', 'hello', 'llohe', 'lohel', 'ohell'])
		self.assertEqual(python_graded_labs.all_cyclic_shifts('xxxxxxxxx'), ['xxxxxxxxx'])

	def test_collapse_intervals(self):
		self.assertEqual(python_graded_labs.collapse_intervals([1, 2, 6, 7, 8, 9, 10, 12, 13]), "1-2,6-10,12-13")
		self.assertEqual(python_graded_labs.collapse_intervals([42]), '42')
		self.assertEqual(python_graded_labs.collapse_intervals([3, 5, 6, 7, 9, 11, 12, 13]), "3,5-7,9,11-13")
		self.assertEqual(python_graded_labs.collapse_intervals([]), '')
		# self.assertEqual(python_graded_labs.collapse_intervals(list(range(1, 1000001))), "1-1000000")

	def test_fibonacci_sum(self):
		self.assertEqual(python_graded_labs.fibonacci_sum(10), [8, 2])
		self.assertEqual(python_graded_labs.fibonacci_sum(100), [89, 8, 3])
		self.assertEqual(python_graded_labs.fibonacci_sum(10**6), [832040, 121393, 46368, 144, 55])
		self.assertEqual(python_graded_labs.fibonacci_sum(10**20), [83621143489848422977, 12200160415121876738, 2880067194370816120, 1100087778366101931, 160500643816367088, 37889062373143906, 117669030460994, 27777890035288, 4052739537881, 1548008755920, 365435296162, 2971215073, 24157817, 3524578, 196418, 75025, 10946, 4181, 610, 233, 89, 21, 3, 1])

	def test_postfix_evaluate(self):
		self.assertEqual(python_graded_labs.postfix_evaluate([2, 3, "+", 4, "*"]), 20)
		self.assertEqual(python_graded_labs.postfix_evaluate([2, 3, 4, "*", "+"]), 14)
		self.assertEqual(python_graded_labs.postfix_evaluate([3, 3, 3, '-', '/']), 0)
		self.assertEqual(python_graded_labs.postfix_evaluate([7, 3, "/"]), 2)
		self.assertEqual(python_graded_labs.postfix_evaluate([1, 2, 3, 4, 5, 6, "*", "*", "*", "*", "+"]), 721)

	def test_factoring_factorial(self):
		self.assertEqual(python_graded_labs.factoring_factorial(5), [(2, 3), (3, 1), (5, 1)])
		self.assertEqual(python_graded_labs.factoring_factorial(10), [(2, 8), (3, 4), (5, 2), (7, 1)])
		self.assertEqual(python_graded_labs.factoring_factorial(20), [(2, 18), (3, 8), (5, 4), (7, 2), (11, 1), (13, 1), (17, 1), (19, 1)])
		self.assertEqual(python_graded_labs.factoring_factorial(100), [(2, 97), (3, 48), (5, 24), (7, 16), (11, 9), (13, 7), (17, 5), (19, 5), (23, 4), (29, 3), (31, 3), (37, 2), (41, 2), (43, 2), (47, 2), (53, 1), (59, 1), (61, 1), (67, 1), (71, 1), (73, 1), (79, 1), (83, 1), (89, 1), (97, 1)])
		
		output1 = python_graded_labs.factoring_factorial(1000)
		self.assertEqual(output1[:5], [(2, 994), (3, 498), (5, 249), (7, 164), (11, 98)])
		self.assertEqual(len(output1), 168)

		output2 = python_graded_labs.factoring_factorial(10000)
		self.assertEqual(output2[:5], [(2, 9995), (3, 4996), (5, 2499), (7, 1665), (11, 998)])
		self.assertEqual(len(output2), 1229)

	def test_calkin_wilf(self):
		from fractions import Fraction
		self.assertEqual(python_graded_labs.calkin_wilf(10), Fraction(3,5))
		self.assertEqual(python_graded_labs.calkin_wilf(1000), Fraction(11,39))
		self.assertEqual(python_graded_labs.calkin_wilf(100000), Fraction(127, 713))

	def test_aliquot_sequence(self):
		self.assertEqual(python_graded_labs.aliquot_sequence(12), [12, 16, 15, 9, 4, 3, 1, 0])
		self.assertEqual(python_graded_labs.aliquot_sequence(34), [34, 20, 22, 14, 10, 8, 7, 1, 0])
		self.assertEqual(python_graded_labs.aliquot_sequence(34, 2), [34, 20])

	def test_josephus(self):
		self.assertEqual(python_graded_labs.josephus(4, 1), [1, 2, 3, 4])
		self.assertEqual(python_graded_labs.josephus(4, 2), [2, 4, 3, 1])
		self.assertEqual(python_graded_labs.josephus(10, 3), [3, 6, 9, 2, 7, 1, 8, 5, 10, 4])
		self.assertEqual(python_graded_labs.josephus(8, 7), [7, 6, 8, 2, 5, 1, 3, 4])
		self.assertEqual(python_graded_labs.josephus(30, 4), [4, 8, 12, 16, 20, 24, 28, 2, 7, 13, 18, 23, 29, 5, 11, 19, 26, 3, 14, 22, 1, 15, 27, 10, 30, 21, 17, 25, 9, 6])

		lst1 = python_graded_labs.josephus(1000, 99)
		self.assertEqual(lst1[:5], [99, 198, 297, 396, 495])
		self.assertEqual(lst1[-5:], [183, 762, 380, 966, 219])

	def test_reverse_reversed(self):
		self.assertEqual(python_graded_labs.reverse_reversed([1, [2, 3, 4, 'yeah'], 5]), [5, ['yeah', 4, 3, 2], 1])
		self.assertEqual(python_graded_labs.reverse_reversed([[[[[[1, 2]]]]]]), [[[[[[2, 1]]]]]])
		self.assertEqual(python_graded_labs.reverse_reversed([42, [99, [17, [33, ['boo!']]]]]), [[[[['boo!'], 33], 17], 99], 42])

	def test_flatten(self):
		self.assertEqual(python_graded_labs.flatten([1, [2, 3, [4, "bob", 6], [7]], [8, 9]]), [1, 2, 3, 4, "bob", 6, 7, 8, 9])
		self.assertEqual(python_graded_labs.flatten([[[[[[]]]]]]), [])
		self.assertEqual(python_graded_labs.flatten([[], [[[[89, 85, 72, 84, 65], [[88, 31, 64, 11, 60, 42, 57, 55], 16, [79, 34, 82], [], 94, 36, [89, 26, 39, 94, 47, 72, 30], [72, 3, 73]], 18]], [[37, [51, 75, 83], 94, 57]], [37, 10, 62, 62], [[], 13]]]), [89, 85, 72, 84, 65, 88, 31, 64, 11, 60, 42, 57, 55, 16, 79, 34, 82, 94, 36, 89, 26, 39, 94, 47, 72, 30, 72, 3, 73, 18, 37, 51, 75, 83, 94, 57, 37, 10, 62, 62, 13])

	def test_prime_factors(self):
		self.assertEqual(python_graded_labs.prime_factors(42), [2, 3, 7])
		self.assertEqual(python_graded_labs.prime_factors(10**6), [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5])
		self.assertEqual(python_graded_labs.prime_factors(1234567), [127, 9721])
		self.assertEqual(python_graded_labs.prime_factors(99887766), [2, 3, 11, 31, 48821])
		self.assertEqual(python_graded_labs.prime_factors(10**12 - 1), [3, 3, 3, 7, 11, 13, 37, 101, 9901])
		self.assertEqual(python_graded_labs.prime_factors(10**15 - 3), [599, 2131, 3733, 209861])

	def test_balanced_ternary(self):
		self.assertEqual(python_graded_labs.balanced_ternary(5), [9, -3, -1])
		self.assertEqual(python_graded_labs.balanced_ternary(-5), [-9, 3, 1])
		self.assertEqual(python_graded_labs.balanced_ternary(42), [81, -27, -9, -3])
		self.assertEqual(python_graded_labs.balanced_ternary(100), [81, 27, -9, 1])
		self.assertEqual(python_graded_labs.balanced_ternary(10**6), [1594323, -531441, -59049, -6561, 2187, 729, -243, 81, -27, 1])

	def test_fibonacci_word(self):
		self.assertEqual(python_graded_labs.fibonacci_word(0), '0')
		self.assertEqual(python_graded_labs.fibonacci_word(1), '1')
		self.assertEqual(python_graded_labs.fibonacci_word(10), '0')
		self.assertEqual(python_graded_labs.fibonacci_word(10**6), '0')
		self.assertEqual(python_graded_labs.fibonacci_word(10**100), '0')
		self.assertEqual(python_graded_labs.fibonacci_word(10**100+1), '1')
		self.assertEqual(python_graded_labs.fibonacci_word(10**1000), '0')