# MCP Server Demo with Cloud Desktop

This project demonstrates an MCP server implementation tested locally with Cloud Desktop integration (Claude Desktop). The server provides basic library management functions such as checking book availability, borrowing books, and retrieving user borrowing history.

## Features

- **Check Book Availability:** Determine if a book is available for borrowing.
- **Borrow Books:** Borrow one or more books with a specified due date.
- **Get Borrowing History:** Retrieve a user's borrowing history.
- **Welcome Message:** Provides a personalized greeting to users.

## Getting Started

### Prerequisites

- **Python 3.11 or later** (specified in `.python-version`)
- **MCP CLI dependencies**  
  Install with:
  ```bash
  pip install mcp[cli]
  ```

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/mcp-server-demo.git
   cd mcp-server-demo
   ```
2. **Create & Activate a Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install mcp[cli]
   ```

### Running the MCP Server Locally

Use the following command to set up the MCP server local environment with Cloud Desktop integration:
```bash
uv run mcp install main.py
```
This command creates the virtual environment (if not already created) and runs the MCP server, allowing you to test the tools and resources provided by the application.

## Project Structure

- `main.py` - Main entry point containing the MCP server definition and all tools/resources.
- `.gitignore` - Specifies files and directories to be ignored by Git.
- `pyproject.toml` - Project configuration and metadata.
- `.python-version` - Defines the required Python version.
- `README.md` - Project documentation and usage instructions.

## Usage

After launching the MCP server, you can interact with the following tools:

- **Check Book Availability (`check_book_availability`):**  
  Pass a valid book ID to get the availability status of a book.
- **Borrow Books (`borrow_books`):**  
  Provide a user ID, a list of book IDs, and a due date to borrow books.
- **Get Borrowing History (`get_borrowing_history`):**  
  Retrieve the history of books borrowed by a user.
- **Welcome Message (`get_welcome`):**  
  Get a personalized greeting message.

## Contributing

Contributions are welcome! If you'd like to improve the project, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- MCP Framework for powering the server.
- Cloud Desktop (Claude Desktop) for local testing.
