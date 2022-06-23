import sys
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=+9), 'JST')
    
def main():
    sec = int(sys.argv[1])
    dt = datetime.fromtimestamp(sec).astimezone(tz=JST)
    print(dt.isoformat())

if __name__ == "__main__":
    main()
