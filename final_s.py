"""

@author: Shrey
Created on 8th December
Title: Ecommerce Framework
Description: An e-commerce solution in Python to allow multiple stores to sell multiple products to multiple customers.
"""


from other import pat as file_reader
import os
from prettytable import PrettyTable
from collections import defaultdict
import unittest


class Store:
	"""Store is where the values of all store deatils are saved"""
	def __init__(self, store_id, store_name):
		self._store_id = store_id
		self._store_name = store_name
		self._product_name = dict()
		self._product_quantity = dict()
		self._product_sold = defaultdict(lambda: defaultdict(int))

	def add_inventory(self, in_quantity, prod_id):
		self._product_quantity[prod_id] = int(in_quantity)

	def add_productname(self, prod_id, prod_name):
		""""add product"""
		self._product_name[prod_id] = prod_name

	def available_prod(self, prod_id):
		"""available products"""
		return self._product_quantity[prod_id]
	def available_product(self, prod_id):
		return self._product_quantity[prod_id]

	def update_inv(self, prod_id, sold_quantity, cust_id):
		"""Inventory changes"""
		sold_quantity = int(sold_quantity)
		available_product = self.available_prod(prod_id)
		if available_product < sold_quantity:
			sold_quantity = available_product

			#add or substract values based on the quantity sold
		self._product_sold[prod_id][cust_id] += sold_quantity
		self._product_quantity[prod_id] -= sold_quantity

	def pt_row(self):
		for product_id in self._product_sold.keys():
			yield [self._store_name, self._product_name[product_id], sorted(self._product_sold[product_id].keys()),
			sum(self._product_sold[product_id].values())]

class Customer:
	"""Customer class is where all details related to customer is stored"""
	def __init__(self, customer_id, customer_name):
		self._customer_id = customer_id
		self._name = customer_name
		self._sold_quantity = dict()

	def add_quantity(self, product_id, sold_quantity):
		if product_id in self._sold_quantity:
			self._sold_quantity[product_id] = self._sold_quantity[product_id] + int(sold_quantity)
		else:
			self._sold_quantity[product_id] = int(sold_quantity)

	def pt_row(self):
		for product_id, quantity in self._sold_quantity.items():
			if quantity > 0:
				yield [self._name, product_id, quantity]

class University:

	def __init__(self, wdir, ptables=True):
		"""Main Repository to read files store values and print pretty table"""
		self._wdir = wdir
		self._customers = dict()
		self._products = dict()
		self._stores = dict()

		self._read_customers(os.path.join(wdir, "customers.txt"))
		self._read_stores(os.path.join(wdir, "stores.txt"))
		self._read_inventory(os.path.join(wdir, "inventory.txt"))
		self._read_products(os.path.join(wdir, "products.txt"))
		self._read_transactions(os.path.join(wdir, "transactions.txt"))

		if ptables:
			print("\n Customer Table")
			self.customer_table()
			print("\n Store Table")
			self.store_table()

	def _read_customers(self, path):
		""" read customer from path and add to self._customers """
		try:
			for cust_id, cust_name in file_reader(path, 2, sep=",", header=True):
				if cust_id in self._customers:
					print(f"customer id already there {cust_id}")
				else:
					self._customers[cust_id] = Customer(cust_id, cust_name)
		except ValueError as err:
			print(err)

	def _read_stores(self, path):
		"""read store file"""
		try:
			for store_id, store_name in file_reader(path, 2, sep="*", header=True):
				if store_id in self._stores:
					print(f"Store id already there {store_id}")
				else:
					self._stores[store_id] = Store(store_id, store_name)
		except ValueError as err:
			print(err)

	def _read_inventory(self, path):
		"""read inventory file"""
		try:
			for store_id, available_quantity, product_id in file_reader(path, 3, sep="|", header=True):
				if store_id in self._stores:
					self._stores[store_id].add_inventory(available_quantity, product_id)
				else:
					print(f"Warning: Store id does not exists {store_id}")
		except ValueError as err:
			print(err)

	def _read_products(self, path):
		"""read product file"""
		try:
			for prod_id, store_id, prod_name in file_reader(path, 3, sep="|", header=False):
				if prod_id in self._products:
					print(f"product id already exists {prod_id}")
				else:
					self._stores[store_id].add_productname(prod_id, prod_name)
		except ValueError as err:
			print(err)

	def _read_transactions(self, path):
		"""read transaction file"""
		try:
			for cust_id, quantity, prod_id, store_id in file_reader(path, 4, sep="|", header=True):
				if cust_id in self._customers:
					available_product = self._stores[store_id].available_product(prod_id)

					self._customers[cust_id].add_quantity(self._stores[store_id]._product_name[prod_id], quantity
					if int(quantity) < available_product else available_product)

				else:
					print(f"Warning: Customer Id {cust_id} does not exist")

				if store_id in self._stores:
					self._stores[store_id].update_inv(prod_id, quantity, self._customers[cust_id]._name)
				else:
					print(f"Warning: Store Id {store_id} does not exist")
		except ValueError as err:
			print(err)

	def store_table(self):
		"""print store pretty table"""
		pt = PrettyTable(field_names=["Store", "Product", "Customer", "Quantity"])
		for store in self._stores.values():
			for row in store.pt_row():
				pt.add_row(row)
		print(pt)

	def customer_table(self):
		"""store customer pretty table"""
		pt = PrettyTable(field_names=["Customer", "Product", "Sold"])
		for customer in self._customers.values():
			for row in customer.pt_row():
				pt.add_row(row)
		print(pt)

def main():
	University('/Users/Shrey/PycharmProjects/F18')


if __name__ == '__main__':
	main()



