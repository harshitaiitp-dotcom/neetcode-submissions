class Solution:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_to_code:
            return self.url_to_code[longUrl]
        
        # Generate a unique short code using the counter
        code = self.base_url + str(self.counter)
        self.counter += 1
        
        # Store both mappings
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.code_to_url.get(shortUrl, "")