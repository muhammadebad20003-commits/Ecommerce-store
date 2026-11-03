

# E-Commerce & Inventory Management System

## Project Description
This project demonstrates the use of Python multithreading concepts through an E-Commerce and Inventory Management System.

In an e-commerce platform, multiple customer orders, flash sales, warehouse updates, and payment gateways need to be processed at the same time. Instead of processing each task one by one, threads are used to handle different operations concurrently.

The project uses sample e-commerce data and demonstrates 12 distinct Python threading and synchronization concepts.

## Dataset
The project utilizes fictional e-commerce order data containing attributes such as:
- Order ID
- Customer Name
- Product Name
- Quantity
- Price
- Processing Time

## Threading Concepts Implemented

| Concept | Python File | Purpose |
| :--- | :--- | :--- |
| Basic Threads | `modules/flash_sale.py` | Synchronizes regional warehouse nodes to launch a flash sale simultaneously (Barrier). |
| Custom Thread Class | `modules/express_riders.py` | Creates express delivery workers using a class that inherits from `threading.Thread`. |
| Lock | `modules/transaction_locks.py` | Protects shared financial ledgers and inventory records from simultaneous updates. |
| RLock | `modules/warehouse_rlock.py` | Allows the same thread to acquire a lock multiple times for nested warehouse bins. |
| Semaphore | `modules/promo_semaphore.py` | Limits concurrent requests to the API rate-limited voucher dispenser. |
| Event | `modules/order_event.py` | Allows packaging workers to wait until the payment gateway provides a start confirmation signal. |
| Condition | `modules/inventory_cond.py` | Coordinates warehouse buffer stock management and restock notifications. |
| Queue | `modules/order_queue.py` | Assigns high-volume customer purchase orders to available fulfillment worker threads. |
| Sequential Join Loop | `modules/audit_reports.py` | Ensures orderly sequential generation of end-of-day department audit reports. |
| Named Threads | `modules/microservices.py` | Manages core background microservice daemons (Payment, Inventory sync). |
| Custom Supplier Threads | `modules/suppliers.py` | Handles bulk supplier batch processing. |

## Project Structure
```text
ecommerce-threading-system/
│
├── data/
│   └── ecommerce_orders.csv
│
├── modules/
│   ├── __init__.py
│   ├── audit_reports.py
│   ├── express_riders.py
│   ├── flash_sale.py
│   ├── inventory_cond.py
│   ├── microservices.py
│   ├── order_event.py
│   ├── order_queue.py
│   ├── promo_semaphore.py
│   ├── suppliers.py
│   ├── transaction_locks.py
│   └── warehouse_rlock.py
│
├── main.py
└── README.md

```

## Requirements

* Python 3.x
* Visual Studio Code (recommended)
* No external Python libraries are required. The project uses Python standard libraries (`threading`, `queue`, `os`, `time`, `random`).

## How to Run the Project

Open your terminal in the project root folder and run the master orchestrator script:

```bash
python main.py

```

You can also execute individual modules independently if needed:

```bash
python -m modules.flash_sale
python -m modules.express_riders
python -m modules.transaction_locks

```

## Expected Outcome

Each Python file demonstrates a different threading concept in an e-commerce and inventory scenario. The output illustrates how multiple warehouse nodes, flash sales, payment gateways, and order queues can be efficiently coordinated using Python threading and synchronization techniques.

## GitHub Version Control

The project is maintained using Git and GitHub.

The following commands are used for version control:

```bash
git status
git add .
git commit -m 
git pull

```

Meaningful commit messages are used to document the changes made to the project.

```

```