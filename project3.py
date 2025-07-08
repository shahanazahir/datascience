def tuple_to_dict(tuple_data):
    try:
        result_dict = dict(tuple_data)
        return result_dict
    except (TypeError, ValueError):
        print("Invalid tuple format. Ensure it contains pairs (key, value).")
        return None


tuple_data = (("a", 1), ("b", 2), ("c", 3))
converted_dict = tuple_to_dict(tuple_data)
print("Converted Dictionary:", converted_dict)










