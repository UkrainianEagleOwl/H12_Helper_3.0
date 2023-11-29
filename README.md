# Advanced Contact Management System

## Overview
This advanced version of the Contact Management System introduces persistent data storage and enhanced search functionality. It allows for saving the address book to disk and retrieving it, as well as searching for contacts by partial name or phone number matches.

## New Features
- **Data Persistence**:
  - Save and load address book data to and from disk using chosen serialization protocol.
  - Methods for saving all data to a file and loading it from the file.
- **Enhanced Search Functionality**:
  - Search contacts by partial matches in names and phone numbers.

## Core Classes
- **AddressBook**: Now with methods for saving to and loading from disk.
- **Record, Name, Phone, Birthday**: Unchanged from previous iterations.

## Functionality
- **Data Storage**:
  - Save the entire address book to a file.
  - Load the address book from a file to restore previous state.
- **Search Capability**:
  - Search through the address book based on partial name or phone number.
  - Display a list of users with matching criteria.

## Installation
Clone the repository and ensure Python is installed. This application may require additional libraries for serialization/deserialization, depending on the chosen protocol.
