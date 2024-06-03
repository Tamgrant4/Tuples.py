# Q Task 1

def format_flight_itineraries(itineraries):
  """
  Formats a list of flight itineraries into a readable string.

  Args:
      itineraries: A list of tuples containing traveler name, origin, and destination.

  Returns:
      A string containing formatted itinerary information.
  """
  formatted_itineraries = ""
  for i, itinerary in enumerate(itineraries, start=1):
    traveler_name, origin, destination = itinerary
    formatted_itineraries += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
  return formatted_itineraries.rstrip()  # Remove trailing newline

# Example usage
itinerary_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_string = format_flight_itineraries(itinerary_list)
print(formatted_string)

# Q2 Task 1

def add_book(library, new_book):
  """
  Adds a new book to the library, handling duplicates.

  Args:
      library: A list of tuples representing books (title, author).
      new_book: A tuple representing the new book (title, author).

  Returns:
      The updated library list with the new book (if not a duplicate).
  """
  if new_book not in library:
    library.append(new_book)
    print(f"Book '{new_book[0]}' by {new_book[1]} added successfully!")
  else:
    print(f"Book '{new_book[0]}' by {new_book[1]} already exists in the library.")
  return library

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add new books (handling duplicates)
new_book1 = ("The Lord of the Rings", "J.R.R. Tolkien")
new_book2 = ("Brave New World", "Aldous Huxley")  # Duplicate

add_book(library.copy(), new_book1)  # Use a copy to avoid modifying original list
add_book(library.copy(), new_book2)

# Q3 Task1

def calculate_average_price(stock_data, symbol, start_date, end_date):
  """
  Calculates the average closing price of a stock over a period.

  Args:
      stock_data: A list of tuples containing stock data (symbol, date, price).
      symbol: The stock symbol to analyze.
      start_date: The start date of the period (YYYY-MM-DD format).
      end_date: The end date of the period (YYYY-MM-DD format).

  Returns:
      The average closing price of the stock for the specified period, 
      or None if no data is found.
  """
  total_price = 0.0
  count = 0
  for data in stock_data:
    if data[0] == symbol and start_date <= data[1] <= end_date:
      total_price += data[2]
      count += 1
  if count > 0:
    return total_price / count
  else:
    return None

# Sample data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-04", 131.0),
    # More data...
]

# Example usage
symbol = "AAPL"
start_date = "2021-01-01"
end_date = "2021-01-04"

average_price = calculate_average_price(stock_data, symbol, start_date, end_date)

if average_price is not None:
  print(f"Average closing price of {symbol} from {start_date} to {end_date}: ${average_price:.2f}")
else:
  print(f"No data found for {symbol} between {start_date} and {end_date}.")

# Q Task 1

def process_orders(orders):
  """
  Processes customer orders and prints details in a user-friendly format.

  Args:
      orders: A list of tuples containing customer order data (name, product, quantity).
  """
  for customer_name, product, quantity in orders:
    print(f"Customer: {customer_name}")
    print(f"  Product: {product}")
    print(f"  Quantity: {quantity}")
    print("---")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Headphones", 3),
]

process_orders(orders)

# Q5 Task 1

def merge_catalogs(*catalogs):
  """
  Merges multiple product catalogs into a single tuple.

  Args:
      *catalogs: A variable number of tuples representing product catalogs.

  Returns:
      A single tuple containing all products from the merged catalogs,
      preserving the original order within each catalog.
  """
  merged_catalog = ()
  for catalog in catalogs:
    merged_catalog += catalog
  return merged_catalog

# Example catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Merge catalogs
combined_catalog = merge_catalogs(catalog1, catalog2)

# Print the combined catalog
print("Combined Catalog:")
for product_name, price in combined_catalog:
  print(f"  - {product_name}: ${price}")

