def display_domains(domains, title="Domain State"):
    print(f"\n[{title}]")
    for var, values in sorted(domains.items()):
        if len(values) <= 5:
            print(f"  {var}: {values}")
        else:
            print(f"  {var}: [{len(values)} values]")
    print()
