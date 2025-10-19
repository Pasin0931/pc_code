# Name: Pasin Makcharoen # Student ID: 6810545794

from pathlib import Path

config_ = {
    "port": "",
    "allowed_users": [],
    "database": {
        "user": "",
        "password": "",
        "timeout": "0"
    }
}

STATE = True
contents_ = []

in_ = input("Load from 'file' or 'manual' input? ")

if in_ == "file":
    name_ = input("Enter filename: ").strip()
    path_ = Path(name_)
    if path_.exists():
        with open(path_, 'r', encoding="utf-8") as fp:
            for a_ in fp:
                aph_ = a_.strip()
                if not aph_ or aph_.startswith("#"):
                    continue
                contents_.append(aph_)
    else:
        print(f"Error: File '{name_}' not found.")
        STATE = False
elif in_ == "manual":
    print("Enter configuration (type 'DONE' to finish):")
    while True:
        usr_in = input("").strip()
        if usr_in == "DONE":
            break
        if not usr_in or usr_in.startswith("#"):
            continue
        contents_.append(usr_in)

if STATE:
    for a_ in contents_:
        a_ = a_.replace(" ", "")
        if a_.startswith("port="):
            b_ = a_.split("=")[1]
            if not b_.isdigit() or int(b_) < 1 or int(b_) > 65535:
                print("Validation Error: Port must be an integer between 1 and 65535.")
                STATE = False
                break
            config_["port"] = b_
        elif a_.startswith("allowed_users="):
            c_ = a_.split("=")[1]
            d_ = c_.split(",")
            if not d_ or any(x == "" for x in d_):
                print("Validation Error: Allowed users list must not be empty.")
                STATE = False
                break
            config_["allowed_users"] = d_
        elif a_.startswith("database="):
            if "user=" not in a_ or "password=" not in a_:
                print("Validation Error: Database dictionary must contain both 'user' and 'password' keys.")
                STATE = False
                break
            e_ = a_.replace("database={", "").replace("}", "")
            f_ = e_.split(";")
            for g_ in f_:
                h_ = g_.split("=")
                if len(h_) == 2:
                    if h_[0] == "user":
                        config_["database"]["user"] = h_[1]
                    elif h_[0] == "password":
                        config_["database"]["password"] = h_[1]
                    elif h_[0] == "timeout":
                        if not h_[1].isdigit() or int(h_[1]) <= 0:
                            print("Validation Error: Database timeout must be a positive integer.")
                            STATE = False
                            break
                        config_["database"]["timeout"] = h_[1]
            if not STATE:
                break

if STATE:
    if config_["port"] == "" or int(config_["port"]) < 1 or int(config_["port"]) > 65535:
        print("Validation Error: Port must be an integer between 1 and 65535.")
        STATE = False
    elif not config_["allowed_users"] or any(x == "" for x in config_["allowed_users"]):
        print("Validation Error: Allowed users list must not be empty.")
        STATE = False
    elif config_["database"]["user"] == "" or config_["database"]["password"] == "":
        print("Validation Error: Database dictionary must contain both 'user' and 'password' keys.")
        STATE = False
    elif not config_["database"]["timeout"].isdigit() or int(config_["database"]["timeout"]) <= 0:
        print("Validation Error: Database timeout must be a positive integer.")
        STATE = False

if STATE:
    print("Configuration file is valid.")
    print("Parsed Data:")
    print(f"port: {config_['port']}")
    n_ = ",".join(config_["allowed_users"])
    print(f"allowed_users: {n_}")
    print("database:")
    print(f"  user: {config_['database']['user']}")
    print(f"  password: {config_['database']['password']}")
    print(f"  timeout: {config_['database']['timeout']}")


