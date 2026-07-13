import os
files = os.listdir("ClutteredFolder")
i=1
for file in files:
    if file.endswith(".Png"):
        print (file)
        os.rename(f"ClutteredFolder/{file}",f"clutteredFolder/{i}.Png")
        i=i+1