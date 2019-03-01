# Ecommerce-Framework
[![build status of master](https://travis-ci.org/Svaity/Ecommerce-Framwork.svg?branch=master)](https://travis-ci.org/Svaity/Ecommerce-Framwork)
![screenshot 2018-12-09 at 9 06 45 pm](https://user-images.githubusercontent.com/43662680/50105411-9e40a800-01fa-11e9-9296-fe7c6f584c56.png)

You've been hired to create an e-commerce solution in Python to allow multiple stores to sell multiple products to multiple customers.   

You'll need to download five different data files that you'll need to include in your solution.  Each file, except the product file,  includes a header row to describe each column:

stores.txt describes each of the stores in e-commerce solution you're building with a store_id and store name
products.txt describes the products sold by each store with the product_id, the store_id where the product is sold, and a description of the item sold.
inventory.txt identifies the store_id of the store, the product_id of the product, and initial quantities of each product when the store opens.  Customer orders may exceed the initial supply but the store has no mechanism to add more inventory. 
customers.txt includes the customer_id and the name of the customer who purchase products from the stores
transactions.txt describes the transactions where the customers attempt to purchase products from sellers and includes the customer_id who is making the purchase, the quantity to be purchased, the product_id of the product being purchased, and the store_id where the product is being purchased
Your solution should define classes to store all of the relevant information and then read the data files to create instances of those classes.  My solution creates the stores, defines the products, identifies the customers, then processes the initial inventory to store the quantities of each product at each store.  Then it processes each line in the transactions file to update the sales and purchase information.  Finally, it generates prettytables to summarize the sales at each stores and the orders placed by the individual customers.  
