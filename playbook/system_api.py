#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
import json
from datetime import datetime
import psutil
from flask import Flask, render_template_string
import logging
logging.basicConfig(level=logging.INFO)
print("APP_ENV =", os.environ.get("APP_ENV"))

app = Flask(__name__)

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except subprocess.CalledProcessError:
        return "Not Running"


def get_system_status():
    data = {}

    # --- Server info ---
    data["server_info"] = {
        "hostname": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "kernel": platform.version(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # --- Disk usage ---
    total, used, free = shutil.disk_usage("/")
    data["disk_usage"] = {
        "total_gb": round(total / (2**30), 2),
        "used_gb": round(used / (2**30), 2),
        "free_gb": round(free / (2**30), 2),
        "percent_used": psutil.disk_usage("/").percent
    }

    # --- CPU usage ---
    data["cpu"] = {
        "cores_logical": psutil.cpu_count(),
        "cores_physical": psutil.cpu_count(logical=False),
        "load_percent": psutil.cpu_percent(interval=1)
    }

    # --- Memory usage ---
    mem = psutil.virtual_memory()
    data["memory"] = {
        "total_gb": round(mem.total / (2**30), 2),
        "used_gb": round(mem.used / (2**30), 2),
        "free_gb": round(mem.available / (2**30), 2),
        "percent_used": mem.percent
    }

    # --- Services ---
    data["services"] = {
        "ssh": run_cmd("pgrep -x sshd >/dev/null && echo Running || echo NotRunning"),
        "apache2": run_cmd("pgrep -x apache2 >/dev/null && echo Running || echo NotRunning")
    }

    return data


@app.route("/")
def html_status():
    env = os.environ.get("APP_ENV", "unknown").upper()
    logging.info(f"Rendering status page for {env} environment...")
    data = get_system_status()
    return render_template_string("""
    <html>
    <head>
        <title>System Status</title>
        <style>
            body {
                background-color: #0d47a1;
                color: white;
                font-family: Arial, sans-serif;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #fff;
            }
            table {
                width: 70%;
                margin: 20px auto;
                border-collapse: collapse;
                background: #1565c0;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            }
            th, td {
                padding: 10px 15px;
                border: 1px solid #90caf9;
                text-align: left;
            }
            th {
                background-color: #1976d2;
            }
        </style>
    </head>
    <body>
        <h1>System Status Dashboard - {{ env }}</h1>

        {% for section, values in data.items() %}
            <h2 style="text-align:center;">{{ section.replace("_", " ").title() }}</h2>
            <table>
                <thead>
                    <tr>
                        {% for key in values.keys() %}
                            <th>{{ key.replace("_", " ").title() }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        {% for value in values.values() %}
                            <td>{{ value }}</td>
                        {% endfor %}
                    </tr>
                </tbody>
            </table>
        {% endfor %}
    </body>
    </html>
    """, data=data, env=env)


if __name__ == "__main__":
    logging.info("Starting Flask app...")
    app.run(host="0.0.0.0", port=5001, debug=True)
