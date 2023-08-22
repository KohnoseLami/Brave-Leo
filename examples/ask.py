from brave_leo import Leo

leo = Leo()

# It initially contains Brave's specified System Prompt.
response = leo.ask('What is the weather like today?')
print(response.completion)

# You can use it as Llama by explicitly leaving System Prompt empty.
response = leo.ask('What is the weather like today?', system_prompt='')
print(response.completion)