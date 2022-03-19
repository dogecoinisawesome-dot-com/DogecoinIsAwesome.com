from app import app, port

if __name__ == "__main__":
    app.run(
        use_debugger=False,
        use_reloader=False,
        passthrough_errors=True,
        host="0.0.0.0",
        port=port,
    )
