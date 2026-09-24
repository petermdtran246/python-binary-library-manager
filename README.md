# CLI Library Management System (Binary Storage Engine)

A lightweight Python Command Line Interface (CLI) application for library inventory management. Built to demonstrate low-level file I/O operations, binary data serialization, and manual record pointer manipulation without relying on external databases or high-level formats like JSON/CSV.

## Key Architecture & Implementation Details

* **Fixed-Length Binary Records:** Data is persisted to a binary file (`library.dat`) using Python's native `struct` module. Each book entry is packed into a fixed 60-byte binary record:
  * `book_id`: 4-byte Integer (`i`)
  * `title`: 30-byte Encoded String (`30s`)
  * `author`: 20-byte Encoded String (`20s`)
  * `stock`: 4-byte Integer (`i`)
* **Memory-Efficient File Operations:** Instead of loading the entire file into memory (RAM), operations stream data block-by-block using standard 60-byte chunk buffers.
* **In-Place Mutation (Soft Deletion):** Deletion utilizes file seeking (`f.seek()`) in `r+b` mode to overwrite specific bytes in-place (updating `stock = 0`) rather than rewriting the entire file or performing costly array shifts.

## Project Structure

```text
.
├── main.py           # CLI entry point, menu loop, and user routing
├── book_manager.py   # Core business logic, byte packing/unpacking, and File I/O
└── library.dat       # Binary storage file (auto-generated at runtime)
```

## Data Layout & Binary Format

Each record follows the struct format string `'i30s20si'`:

| Field | Type | Size | Encoding |
| :--- | :--- | :--- | :--- |
| `Book ID` | Integer | 4 bytes | Native C Int |
| `Title` | String | 30 bytes | UTF-8 (Padded with spaces) |
| `Author` | String | 20 bytes | UTF-8 (Padded with spaces) |
| `Stock` | Integer | 4 bytes | Native C Int |
| **Total** | | **60 bytes** | |

## Getting Started

### Prerequisites

* Python 3.8+ (Standard Library only — no `pip install` required).

### Execution

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/python-binary-library-manager.git](https://github.com/your-username/python-binary-library-manager.git)
   cd python-binary-library-manager
