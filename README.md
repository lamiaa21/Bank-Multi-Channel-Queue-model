Overview

This project implements a Bank Multi-Channel Queue Model using Python to simulate the behavior of two types of customers—Ordinary and Distinguished—in a bank. It models customer arrivals, waiting times, service times, and idle times using random distributions. The objective is to analyze how well the bank can handle customer flow while maintaining priority service for distinguished customers.

Features

Customer Types:
Ordinary Customers (O)
Distinguished Customers (D) with priority over ordinary customers

Inter-Arrival Time & Service Time Generation:
Uses random distributions to simulate the inter-arrival and service times.

Service Priority Logic:
Distinguished customers are served first even if ordinary customers are waiting.

Performance Metrics:
Average inter-arrival and service times
Waiting time per customer type
Queue lengths and idle times of servers
