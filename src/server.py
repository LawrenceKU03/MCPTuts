
from fastmcp import FastMCP 

mcp=FastMCP(name="calculator")

@mcp.tool(name="multiply",description="a function that takes two numbers and multiply them a:float b:float and returns the product of a * b which is of type float",tags=["maths","arithmetics"])
def multiply(a:float,b:float)-> float:
    return  a*b

@mcp.tool
def say_hello()-> str:
    return f"Hello world!"

if __name__ =="__main__":
    mcp.run()
