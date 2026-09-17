import re
import sys

if len(sys.argv) != 3:
    print("Usage: update_release_body.py ${{env.RELEASE_PATH}} ${{inputs.release_tag}}")
    sys.exit(1)

RELEASE_PATH = sys.argv[1]
RELEASE_TAG = sys.argv[2]

# GitHub's auto-generated notes end every line with " by @author in https://.../pull/N".
# Hand-written notes have no such suffix, so match it instead of cutting a fixed number of words.
AUTO_NOTES_SUFFIX = re.compile(r" by @\S+ in https://\S+$")

with open("changelog.txt", "r") as changelog, open("release_body.txt", "r") as release_body, open("final_body.txt", "w") as output:
    for line in release_body:
        line = line.replace("${{env.RELEASE_PATH}}", RELEASE_PATH)
        line = line.replace("${{inputs.release_tag}}", RELEASE_TAG)
        line = line.replace("${{inputs.short_version}}", RELEASE_TAG)
        output.write(line)

    output.write("\n")

    skipPrint = True
    lastBlank = True
    for line in changelog:
        line = line.strip()
        if "What's Changed" in line:
            skipPrint = False
            output.write("\n" + line + "\n\n")
            continue
        if skipPrint or "**Full Changelog**" in line:  # the changelog link points at the private repo
            continue
        if not line:
            if not lastBlank:
                output.write("\n")
            lastBlank = True
            continue
        lastBlank = False
        output.write(AUTO_NOTES_SUFFIX.sub("", line) + "\n")
