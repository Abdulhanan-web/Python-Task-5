def load_template(name):
    try:
        with open(f"templates/{name}.txt", "r", encoding="utf-8") as file:
            return file.read()
    except:
        print("Template not found!")
        return ""


def personalize(template, data, message):
    try:
        return template.format(
            name=data.get("name", ""),
            company=data.get("company", ""),
            message=message
        )
    except KeyError:
        return template