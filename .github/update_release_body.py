import sys

if len(sys.argv) != 3:
    print("Usage: update_release_body.py ${{env.RELEASE_PATH}} ${{inputs.release_tag}}")
    sys.exit(1)

RELEASE_PATH = sys.argv[1]
RELEASE_TAG = sys.argv[2]

with open("changelog.txt", "r") as changelog, open("release_body.txt", "r") as release_body, open("final_body.txt", "w") as output:
    for line in release_body:
        line = line.replace("${{env.RELEASE_PATH}}", RELEASE_PATH)
        line = line.replace("${{inputs.release_tag}}", RELEASE_TAG)
        output.write(line)

    output.write("\n")

    skipPrint = True
    for line in changelog:
        line = line.strip()
        if "What's Changed" in line:
            skipPrint = False
            output.write("\n" + line + "\n\n")
            continue
        if not line or "**Full Changelog**" in line :
            continue
        if not skipPrint:
            line = line.split(" in https:")[0] # rm link
            line = " ".join(line.split(' ')[:-2]) # rm author
            output.write(line + "\n")
