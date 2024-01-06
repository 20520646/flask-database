from datetime import datetime
# df = now.strftime("%H:%M:%S")
while True:
    now = datetime.now()
    
    df = now.strftime("%H:%M:%S")
    print(df)
    if df == "16:36:00":
        print("dfdsfd")
        break
print(df)