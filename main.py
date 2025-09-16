from mcp.server.fastmcp import FastMCP
from typing import List

# In-memory mock database for library books
library_books = {
    "B001": {"title": "The Python Guide", "author": "John Doe", "available": True, "borrowed_by": None, "due_date": None},
    "B002": {"title": "JavaScript Mastery", "author": "Jane Smith", "available": False, "borrowed_by": "U001", "due_date": "2025-10-01"},
    "B003": {"title": "Data Science Basics", "author": "Mike Johnson", "available": True, "borrowed_by": None, "due_date": None}
}

# User borrowing history
user_history = {
    "U001": ["B002", "B005"],
    "U002": []
}

# Create MCP server
mcp = FastMCP("LibraryManager")


# Tool: Check book availability
@mcp.tool()
def check_book_availability(book_id: str) -> str:
    """Check if a book is available for borrowing"""
    book = library_books.get(book_id)
    if book:
        if book["available"]:
            return f"Book '{book['title']}' by {book['author']} is available for borrowing"
        else:
            return f"Book '{book['title']}' is currently borrowed by {book['borrowed_by']}, due back on {book['due_date']}"
    return "Book ID not found"


# Tool: Borrow books
@mcp.tool()
def borrow_books(user_id: str, book_ids: List[str], due_date: str) -> str:
    """
    Borrow books with a specific due date (e.g., ["B001", "B003"], "2025-10-15").
    """
    if user_id not in user_history:
        user_history[user_id] = []
    
    borrowed_books = []
    unavailable_books = []
    
    for book_id in book_ids:
        if book_id not in library_books:
            unavailable_books.append(f"{book_id} (not found)")
        elif not library_books[book_id]["available"]:
            unavailable_books.append(f"{book_id} (already borrowed)")
        else:
            # Mark book as borrowed
            library_books[book_id]["available"] = False
            library_books[book_id]["borrowed_by"] = user_id
            library_books[book_id]["due_date"] = due_date
            user_history[user_id].append(book_id)
            borrowed_books.append(f"{book_id} ({library_books[book_id]['title']})")
    
    result = []
    if borrowed_books:
        result.append(f"Successfully borrowed: {', '.join(borrowed_books)}")
    if unavailable_books:
        result.append(f"Unable to borrow: {', '.join(unavailable_books)}")
    
    return ". ".join(result) if result else "No books processed"


# Tool: Get user borrowing history
@mcp.tool()
def get_borrowing_history(user_id: str) -> str:
    """Get borrowing history for a user"""
    history = user_history.get(user_id, [])
    if history:
        book_titles = []
        for book_id in history:
            book = library_books.get(book_id)
            if book:
                book_titles.append(f"{book_id} ({book['title']})")
            else:
                book_titles.append(f"{book_id} (unknown)")
        return f"Borrowing history for {user_id}: {', '.join(book_titles)}"
    return f"No borrowing history found for user {user_id}"


# Resource: Welcome message
@mcp.resource("welcome://{user}")
def get_welcome(user: str) -> str:
    """Get a personalized welcome message"""
    return f"Welcome to the Library, {user}! How can I help you find or manage books today?"


if __name__ == "__main__":
    mcp.run()