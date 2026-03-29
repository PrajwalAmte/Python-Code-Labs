import pyshorteners

try:
    url = input("Enter the URL: ").strip()
    
    if not url:
        print("URL cannot be empty.")
    else:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        print(f"Short link: {short_url}")
except Exception as e:
    print(f"Error shortening URL: {str(e)}")