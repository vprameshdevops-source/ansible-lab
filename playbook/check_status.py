#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
import json

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except subprocess.CalledProcessError:
        return "Not Running"

def main():
    data = {}
    data["server_info"] = {
        "hostname": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "kernel": platform.version()
    }

    total, used, free = shutil.disk_usage("/")
    data["disk_usage"] = {
        "total_gb": total // (2**30),
        "used_gb": used // (2**30),
        "free_gb": free // (2**30)
    }

    data["services"] = {
        "ssh": run_cmd("systemctl is-active ssh || service ssh status | grep Active || echo NotRunning"),
        "apache2": run_cmd("systemctl is-active apache2 || service apache2 status | grep Active || echo NotRunning")
    }

    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
