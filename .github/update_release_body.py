import sys

if len(sys.argv) != 3:
    print("Usage: update_release_body.py ${{env.RELEASE_PATH}} ${{inputs.release_tag}}")
    sys.exit(1)

RELEASE_PATH = sys.argv[1]
RELEASE_TAG = sys.argv[2]

with open("changelog.txt", "r") as changelog, open("release_body.txt", "r") as release_body, open("final_body.txt", "w") as output:
    for line in release_body:
        line.replace("${{env.RELEASE_PATH}}", RELEASE_PATH)
        line.replace("${{inputs.release_tag}}", RELEASE_TAG)
        output.write(line)

    output.write("\r\n")

    skipPrint = True
    for line in changelog:
        line = line.strip()
        if "What's Changed" in line:
            skipPrint = False
        if not line or "**Full Changelog**" in line :
            continue
        if not skipPrint:
            line = line.split(" in https:")[0]
            output.write(line + "\r\n")