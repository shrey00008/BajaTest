from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

class InputData(BaseModel):
    data: List[Any]

@app.post("/bfhl")
def bfhl(payload: InputData):
    try:
        arr = payload.data
        numbers = []
        alphabets = []
        special_characters = []

        for item in arr:
            if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):
                numbers.append(int(item))
            elif isinstance(item, str) and item.isalpha():
                alphabets.append(item)
            elif isinstance(item, str):
                special_characters.append(item)

        even_numbers = [str(num) for num in numbers if num % 2 == 0]
        odd_numbers = [str(num) for num in numbers if num % 2 != 0]
        sum_of_numbers = str(sum(numbers))
        uppercase_alphabets = [char.upper() for char in alphabets]

        alpha_concat = ''.join(alphabets)
        rev_alt_caps = ''.join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(alpha_concat[::-1])
        )

        return {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets": uppercase_alphabets,
            "special_characters": special_characters,
            "sum": sum_of_numbers,
            "concat_string": rev_alt_caps
        }
    except Exception:
        return {"is_success": False}