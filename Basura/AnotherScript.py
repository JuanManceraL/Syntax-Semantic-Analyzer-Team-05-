import UI.UI
import main
import UI
from pathlib import Path

arg1 = "olaolaola"

script_dir = Path(__file__).parent

#input_file_name = "UI.py"
#input_file_dir = script_dir / "UI" / input_file_name
#print(f"\n\n {input_file_dir} \n\n")

#exec(open(input_file_dir).read())
#main.Analize(arg1)

UI.UI.generarUI()