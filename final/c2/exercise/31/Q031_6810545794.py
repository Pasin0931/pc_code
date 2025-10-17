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

in_ = input("Load from 'file' or 'manual' input? ")

if in_ == "file":
    name_ = input("Enter filename: ")
    path_ = Path.cwd() / f"{name_}"
    
    if path_.exists():
        print("Configuration file is valid.")
        print("Parsed Data:")

        fp = open(name_, 'r', encoding="utf-8")
        contents_ = fp.read()
        contents_ = contents_.split()

        contents_.pop(0)
        contents_.pop(0)
        contents_.pop(0)

        port_ = contents_[0].split("=")[1]
        allowed_g = contents_[1].split("=")[1].split(",")
        re_arrange = ""
        for i in contents_[2].split("e=")[1]:
            if i != "{" and i != "}":
                re_arrange += i

        db_values = re_arrange.split(";")
        for i in range(len(db_values)):
            db_values[i] = db_values[i].split("=")[1]

        config_["port"] = port_
        config_["allowed_users"] = allowed_g
        config_["database"] = {
            "user": db_values[0],
            "password": db_values[1],
            "timeout": db_values[2]
        }

        print(f"port: {config_['port']}")
        
        n_ = ",".join(config_["allowed_users"])
        print(f"allowed_users: {n_}")

        print("database:")
        print(f"  user: {config_['database']['user']}")
        print(f"  password: {config_['database']['password']}")
        print(f"  timeout: {config_['database']['timeout']}")
    else:
        print(f"Error: File '{name_}' not found.")

    # print(config_)

elif in_ == "manual":
    print("Enter configuration (type 'DONE' to finish):")

    while True:
        usr_in = input("")

        if usr_in == "DONE":
            break

        for_db = usr_in.split("e=")
        usr_in = usr_in.split("=")

        if usr_in[0] == "port":
            usr_in.pop(0)
            usr_in = usr_in[0]

            config_["port"] = usr_in

            # print(usr_in)
            # print(config_)

        elif usr_in[0] == "allowed_users":
            usr_in.pop(0)
            usr_in = usr_in[0].split(",")

            config_["allowed_users"] = usr_in

            # print(usr_in)
            # print(config_)

        elif for_db[0] == "databas":
            for_db.pop(0)
            for_db = for_db[0]

            re_arrange = ""
            for i in for_db:
                if i != "{" and i != "}":
                    re_arrange += i

            for_db = re_arrange.split(";")

            for i in range(len(for_db)):
                for_db[i] = for_db[i].split("=")

                if for_db[i][0] in config_["database"].keys():
                    config_["database"][for_db[i][0]] = for_db[i][1]

            # print(for_db)
            # print(config_)

        else:
            continue

    if config_["port"] == "" or int(config_["port"]) < 1 or int(config_["port"]) > 65535:
        print("Validation Error: Port must be an integer between 1 and 65535.")
        STATE = False

    elif config_["allowed_users"] == [""] or config_["allowed_users"] == "":
        print("Validation Error: Allowed users list must not be empty.")
        STATE = False

    elif config_["database"]["user"] == "" or config_["database"]["password"] == "":
        print("Validation Error: Database dictionary must contain both 'user' and 'password' keys.")
        STATE = False

    elif int(config_["database"]["timeout"]) < 0:
        print("Validation Error: Database timeout must be a positive integer.")
        STATE = False

    if STATE == True:
        WORD = "# Server configuration"

        print("Configuration file is valid.")
        print("Parsed Data:")

        for k, v in config_.items():
            if k == "port":
                print(f"port: {v}")
                WORD += f"\nport={v}"

            elif k == "allowed_users":
                this_v = ",".join(v)
                print(f"allowed_users: {this_v}")
                WORD += f"\nallowed_users={this_v}"

            elif k == "database":
                here_w = "\ndatabase={"
                print("database:")
                for tk, tv in config_["database"].items():
                    if tk == "user":
                        print(f"  user: {tv}")
                        a = f"user={tv};"

                    elif tk == "password":
                        print(f"  password: {tv}")
                        b = f"password={tv};"

                    elif tk == "timeout":
                        print(f"  timeout: {tv}")
                        c = f"timeout={tv}"
                here_w += a
                here_w += b
                here_w += c
                here_w += "}"

                WORD += here_w
        
        w_ = Path.cwd() / "manual.conf"
        fp_ = open(w_, mode="w", encoding="utf-8")
        fp_.write(WORD)
        fp_.close()

