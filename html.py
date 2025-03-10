import json

def generate_html():
    # Load statistics.json data
    with open("outputs/statistics.json", "r") as file:
        data_dict = json.load(file)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Summary</title>
        <style>
            body {{
                background-color: #000000;
                color: #FFFFFF;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                width: 80%;
                margin: 0 auto;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
                background-color: #1c1c1c;
            }}
            th, td {{
                border: 1px solid #444;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #333;
            }}
            td {{
                background-color: #222;
            }}
            h1, p {{
                margin: 10px;
            }}
            .header {{
                color: #FFD700;
            }}
            #asciiArt {{
                font-family: monospace;
                white-space: pre;
                color: #FFD700;
                position: absolute;
                top: 10px;
                right: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="header">Data Summary</h1>
            <p>Мы обработали полученные фигуры и подвели статистику</p>
            <table>
                <tr><th>Parameter</th><th>Value</th></tr>
                <tr><td>Average Diagonal</td><td>{data_dict.get('avg_diag', 'N/A')}</td></tr>
                <tr><td>Average Volume</td><td>{data_dict.get('avg_volume', 'N/A')}</td></tr>
                <tr><td>Average Surface Area</td><td>{data_dict.get('avg_surface_area', 'N/A')}</td></tr>
                <tr><td>Average Alpha</td><td>{data_dict.get('avg_alpha', 'N/A')}</td></tr>
                <tr><td>Average Beta</td><td>{data_dict.get('avg_beta', 'N/A')}</td></tr>
                <tr><td>Average Gamma</td><td>{data_dict.get('avg_gamma', 'N/A')}</td></tr>
                <tr><td>Average Radius of Described Sphere</td><td>{data_dict.get('avg_radius_described_sphere', 'N/A')}</td></tr>
                <tr><td>Average Volume of Described Sphere</td><td>{data_dict.get('avg_volume_described_sphere', 'N/A')}</td></tr>
            </table>
        </div>
        <div id="asciiArt"></div>
        <script>
            const asciiArt = [
                "MY FIRST SCRIPT\\n\\n",
                "    *********\\n",
                "   *       **\\n",
                "  *       * *\\n",
                " *********  *\\n",
                " *       *  *\\n",
                " *       *  *\\n",
                " *       * *\\n",
                " *********\\n",
                "\\nI LOVE PYTHON"
            ];

            let artIndex = 0;
            function displayArt() {{
                if (artIndex < asciiArt.length) {{
                    document.getElementById("asciiArt").innerText += asciiArt[artIndex];
                    artIndex++;
                    setTimeout(displayArt, 400);
                }}
            }}
            displayArt();
        </script>
    </body>
    </html>
    """
    with open("data_summary.html", "w") as file:
        file.write(html_content)

# Run function to generate HTML
generate_html()