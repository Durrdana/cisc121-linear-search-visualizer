import gradio as gr

# 1. BASIC LINEAR SEARCH (NO ENUMERATE)
def linear_search(arr, target):
    """
    Returns the index where the target is found,
    or -1 if it is not in the list.
    """
    index = 0  # start at first element

    while index < len(arr):
        if arr[index] == target:
            return index
        index = index + 1  # move to next index

    return -1  # not found

# 2. LINEAR SEARCH WITH STEP TRACKING
def linear_search_steps(arr_str, target_str):
    # check empty input
    if arr_str == "" or target_str == "":
        return "Error: enter a list and target."

    # convert list to integers  
    parts = arr_str.split(",")
    arr = []
    for p in parts:
        arr.append(int(p.strip()))

    target = int(target_str)

    steps = ""
    steps += "Starting linear search...\n\n"

    index = 0
    while index < len(arr):
        steps += "Checking index " + str(index) + ": value = " + str(arr[index]) + "\n"

        if arr[index] == target:
            steps += "\nFound target " + str(target) + " at index " + str(index)
            return steps

        index += 1

    steps += "\nTarget not found."
    return steps

# 3. GRADIO USER INTERFACE
with gr.Blocks() as demo:
    gr.Markdown()

    with gr.Group():
        arr_input = gr.Textbox(
            label="List of Numbers",
            placeholder="Example: 4, 1, 9, 2",
            info="Separate numbers with commas."
        )
        target_input = gr.Textbox(
            label="Target Number",
            placeholder="Example: 9",
        )

    run_button = gr.Button("Run Linear Search", variant="primary")

    output = gr.Textbox(
    label="Search Steps",
    lines=10,
    max_lines=20,
    interactive=False,
)
    run_button.click(
        fn=linear_search_steps,
        inputs=[arr_input, target_input],
        outputs=output
    )

demo.launch()
