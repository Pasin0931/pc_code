from pathlib import Path as nigger

# print(nigger.cwd())       # current path


# print(nigger.home())      # home path


# this_nigga = nigger.cwd() / "data" / "users.csv"        # Build path to subdirectory file
# print(this_nigga)


reports_dir = nigger("reports")
monthly_report = reports_dir / "january" / "sales"
print(f"Report Path: {monthly_report}")


# this_nigga.mkdir()