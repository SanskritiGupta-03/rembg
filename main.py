
from rembg import remove
import time
input_path = "oldpic.JPG"
output_path = "new.jpg"

start_time = time.time()
with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input = i.read()
        output = remove(input)
        o.write(output)
        end_time = time.time()
print(f"Image background is removed in {str(end_time - start_time)[:3]}")

