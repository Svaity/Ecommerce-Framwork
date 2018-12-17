from work import Ecommerce, Customer, Store
import unittest


class EcommTest(unittest.TestCase):
	def test_Ecomm(self):
		wdir = '/Users/Shrey/PycharmProjects/F18'
		stevens = Ecommerce(wdir, False)
		Store = [[["Maha's Movies", 'Bohemian Rhapsody movie tickets', ['GitHub Gus'], 4],["Maha's Movies",'Grinch movie tickets',['Debugging Dinesh', 'GitHub Gus'],10]],[["Ben's Books",'Java Programming Jokes',
		['Architect Armin', 'Debugging Dinesh', 'GitHub Gus'],
		 1],
		["Ben's Books",
		'Python Programming Pearls',
		['Architect Armin', 'Debugging Dinesh', 'GitHub Gus'],
		3],
		["Ben's Books",
		'Job Interview Tips',
		['Architect Armin', 'Debugging Dinesh', 'GitHub Gus'],
		2]],[["Dariel's Donuts",'Chocolate donuts',['Architect Armin', 'GitHub Gus'],36],["Dariel's Donuts",'Coffee',['Architect Armin', 'Debugging Dinesh', 'GitHub Gus'],25]]]


		Customer = [[['Debugging Dinesh', 'Java Programming Jokes', 1],
  		['Debugging Dinesh', 'Job Interview Tips', 1],
  		['Debugging Dinesh', 'Grinch movie tickets', 6],
  		['Debugging Dinesh', 'Python Programming Pearls', 1],
  		['Debugging Dinesh', 'Coffee', 11]],
 		[['Architect Armin', 'Python Programming Pearls', 1],
  		['Architect Armin', 'Coffee', 8],
  		['Architect Armin', 'Chocolate donuts', 16]],
 		[['GitHub Gus', 'Python Programming Pearls', 1],
  		['GitHub Gus', 'Chocolate donuts', 20],
  		['GitHub Gus', 'Job Interview Tips', 1],
  		['GitHub Gus', 'Bohemian Rhapsody movie tickets', 4],
  		['GitHub Gus', 'Coffee', 6],
  		['GitHub Gus', 'Grinch movie tickets', 4]]]

		ptstore = [list(s.pt_row()) for s in stevens._stores.values()]
		ptcustomer = [list(s.pt_row()) for s in stevens._customers.values()]

		self.assertEqual(ptstore, Store)
		self.assertEqual(ptcustomer, Customer)

if __name__ == '__main__':
	unittest.main(exit=False, verbosity=2)