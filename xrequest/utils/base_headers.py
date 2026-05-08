HEADERS = {
    # navegador recomendado
    "recommended": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/avif,image/webp,*/*;q=0.8"
        ),

        # identity evita html quebrado/comprimido
        "Accept-Encoding": "identity",

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1",

        "Cache-Control": "no-cache",
    },

    # navegador humano
    "human": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
        ),

        "Accept-Encoding": "identity",

        "Cache-Control": "max-age=0",

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1",

        "Sec-CH-UA": (
            '"Google Chrome";v="135", '
            '"Chromium";v="135", '
            '"Not.A/Brand";v="24"'
        ),

        "Sec-CH-UA-Mobile": "?0",

        "Sec-CH-UA-Platform": '"Windows"',

        "Sec-Fetch-Dest": "document",

        "Sec-Fetch-Mode": "navigate",

        "Sec-Fetch-Site": "none",

        "Sec-Fetch-User": "?1",
    },

    # firefox
    "firefox": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) "
            "Gecko/20100101 Firefox/138.0"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/avif,image/webp,*/*;q=0.8"
        ),

        "Accept-Encoding": "identity",

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1",
    },

    # edge
    "edge": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/webp,*/*;q=0.8"
        ),

        "Accept-Encoding": "identity",

        "Connection": "keep-alive",
    },

    # api json
    "api": {
        "User-Agent": "xrequest/0.1.0",

        "Accept": "application/json",

        "Content-Type": "application/json",

        "Accept-Encoding": "identity",

        "Connection": "keep-alive",
    },

    # ajax/fetch
    "ajax": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),

        "Accept": "*/*",

        "Accept-Encoding": "identity",

        "X-Requested-With": "XMLHttpRequest",

        "Sec-Fetch-Mode": "cors",

        "Sec-Fetch-Site": "same-origin",
    },

    # android
    "android": {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 14; SM-S918B) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Mobile Safari/537.36"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/webp,*/*;q=0.8"
        ),

        "Accept-Encoding": "identity",
    },

    # iphone
    "iphone": {
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/18.0 Mobile/15E148 Safari/604.1"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,*/*;q=0.8"
        ),

        "Accept-Encoding": "identity",
    },

    # curl
    "curl": {
        "User-Agent": "curl/8.8.0",

        "Accept": "*/*",

        "Accept-Encoding": "identity",
    },

    # requests
    "requests": {
        "User-Agent": "python-requests/2.32.3",

        "Accept": "*/*",

        "Accept-Encoding": "identity",

        "Connection": "keep-alive",
    },

    # httpx
    "httpx": {
        "User-Agent": "python-httpx/0.28.1",

        "Accept": "*/*",

        "Accept-Encoding": "identity",

        "Connection": "keep-alive",
    },

    # scraping
    "scraper": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),

        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/webp,*/*;q=0.8"
        ),

        "Accept-Encoding": "identity",

        "DNT": "1",

        "Pragma": "no-cache",

        "Cache-Control": "no-cache",

        "Connection": "keep-alive",
    },

    # minimal
    "minimal": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),

        "Accept-Encoding": "identity",
    },
}
