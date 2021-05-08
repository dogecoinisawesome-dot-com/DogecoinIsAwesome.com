from app import app

if __name__ == "__main__":
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)