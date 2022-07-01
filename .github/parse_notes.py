with open("input.txt", "r") as input, open("output.txt", "w") as output:
    skipPrint = True
    for line in input:
        line = line.strip()
        if "What's Changed" in line:
            skipPrint = False
        if not line or "**Full Changelog**" in line :
            continue
        if not skipPrint:
            line = line.split(" in https:")[0]
            output.write(line + "\r\n")
