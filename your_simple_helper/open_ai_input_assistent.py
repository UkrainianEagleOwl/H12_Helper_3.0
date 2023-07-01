import openai

def activate_openai(key):
    openai.api_key = key
    

def analize_input_activate_func(command, customer_input = None,  iteration_done = None):
    if command:
        prompt_string = create_prompt_for_openai(command, iteration_done)
    else:
        prompt_string = customer_input

    # Generate text relevant to the command using OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_string,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.6,
        frequency_penalty=0.2,
        presence_penalty=0.2
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

def create_prompt_for_openai(command = dict, command_done = False):
    simple_commands = (1,6,7,8)
    arguments_commands = (2,3,4)
    if command_done:
        return f'Command {command.get("name")} with such description - {command.get("description")} was done. Tell this in friendly form to the user.'
    else:
        if command.get('id') in simple_commands:
            return f'{command.get("description")} in friendly form about work with you.'
        elif command.get('id') in arguments_commands:
            return f'For {command.get("name")} that is {command.get("description")} you need this {command.get("arguments")} splitted by comma. Say this for user in friendly form.'
        else:
            return f'Command {command.get("name")} with such description - {command.get("description")} was done. Tell this in friendly form to the user.'
