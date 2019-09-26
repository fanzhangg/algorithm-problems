def find_strings(strs: list, prefix: str)->list:
    return [s for s in strs if s.startswith(prefix)]
