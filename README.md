# Brave Leo

"Brave Leo" is a Python module that provides access to Brave's Leo AI chat functionality based on Llama. With this module, you can easily integrate AI chat capabilities powered by Brave's Leo into your Python applications.

## Installation

You can install "brave-leo" using pip:

```bash
pip install brave-leo
```

## Usage

Here's a quick example of how to use "brave-leo" to interact with Brave's Leo AI:

Sync,
```python
from brave_leo import Leo

# Initialize the Leo instance
leo = Leo()

# Ask to Leo and get a response
response = leo.ask('What is the weather like today?')

print("Leo:", response.completion)
```

Async,
```python
import asyncio
from brave_leo import AsyncLeo

# Initialize the Leo instance
leo = AsyncLeo()

async def main():
    # Ask to Leo and get a response
    response = await leo.ask('What is the weather like today?')
    print("Leo:", response.completion)
    # Close Session
    await leo.close()

asyncio.run(main())
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/KohnoseLami/Brave-Leo/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions or find issues, please feel free to open an issue or submit a pull request.