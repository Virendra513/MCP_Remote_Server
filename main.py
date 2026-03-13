from fastmcp import FastMCP
import random
import json

# Create the FastMCP server Instance
mcp=FastMCP("Random Number Generator Server")



@mcp.tool
def unique_random_number_generator(min_val: int= 1, max_val: int =100) -> int:
    """
    Generate a random number within a range

    Args:
        min_val: Minimum value (deafult: 1)
        max_val: Maximum vaue (default: 100)
    Returns :
        A random integar between min_val and max_val
    """
    return random.randint(min_val, max_val)



@mcp.tool
def random_float_range(min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Generate a random float within a specified range.

    Args:
        min_val: Minimum value
        max_val: Maximum value

    Returns:
        Random float between min_val and max_val
    """
    return min_val + (max_val - min_val) * random.random()



@mcp.tool
def list_unique_random_numbers(count: int=2, min_val: int= 1, max_val: int =100) -> list[int]:

    """
    Generate a list of random numbers within a range

    Args:
        count: Count(default: 2)
        min_val: Minimum value (deafult: 1)
        max_val: Maximum vaue (default: 100)
    Returns :
        A list of random numbers  between min_val and max_val
    """
    if count > (max_val - min_val + 1):
        raise ValueError("count cannot be larger than the range of unique numbers")

    return random.sample(range(min_val, max_val + 1), count)


@mcp.tool
def shuffle_numbers(nums: list[int]) -> list[int]:
    """
    Shuffle a list of numbers randomly.

    Args:
        nums: List of integers

    Returns:
        Shuffled list of integers
    """
    random.shuffle(nums)
    return nums


@mcp.tool
def list_random_floats(count: int = 2, min_val: float = 0.0, max_val: float = 1.0) -> list[float]:
    """
    Generate a list of random float numbers.

    Args:
        count: Number of random floats to generate (default: 2)
        min_val: Minimum value (default: 0.0)
        max_val: Maximum value (default: 1.0)

    Returns:
        A list of random float numbers between min_val and max_val
    """
    return [random.uniform(min_val, max_val) for _ in range(count)]




@mcp.resource("info://server")
def server_info() -> str:
    """ Get Information about the server"""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description" : "A basic MCP server with math tools",
        "tools":["add", "random_number_generator"],
        "author": "essmorath"
    }
    return json.dumps(info, indent=2)



if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
