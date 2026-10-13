from pathlib import Path
from datetime import datetime
import pandas as pd

def generate_report():
    # Sample logistics data
    data = {
        "Deposito": ["CD01", "CD02", "CD03"],
        "Transportadora": ["Trans A", "Trans B", "Trans C"],
        "Qtd_Cargas": [25, 18, 32],
        "Qtd_Volumes": [1200, 850, 1640]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Create output folder
    output_folder = Path.home() / "Downloads" / "robo_relatorios"
    output_folder.mkdir(parents=True, exist_ok=True)

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_folder / f"relatorio_{timestamp}.xlsx"

    # Export to Excel
    df.to_excel(file_path, index=False)

    print(f"Report generated: {file_path}")

    return file_path

if __name__ == "__main__":
    generate_report()