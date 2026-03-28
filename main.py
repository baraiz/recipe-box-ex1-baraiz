import uvicorn

def main():
    """Start the FastAPI server."""
    print("🚀 Starting Recipe Box API...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()