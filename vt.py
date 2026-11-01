import subprocess

with (
    open(HASH_LIST_PATH, "r", encoding="utf-8") as file,
    open(OUTPUT_PATH, "w") as output,
):
    api = API
    subprocess.run(["vt", "init", "--apikey", api], check=True)
    lines = 237
    counter = 0
    for line in file:
        marker_id = line.find(".nca")
        if ".nca" in line:
            start_look = marker_id + len(".nca") + 1
            parsed_line = line[start_look:].strip()
            result = subprocess.run(
                ["vt", "analysis", parsed_line], capture_output=True, text=True
            )
            output.write(result.stdout + "\n")
            counter += 1
            print(f"{counter}/{lines}")
