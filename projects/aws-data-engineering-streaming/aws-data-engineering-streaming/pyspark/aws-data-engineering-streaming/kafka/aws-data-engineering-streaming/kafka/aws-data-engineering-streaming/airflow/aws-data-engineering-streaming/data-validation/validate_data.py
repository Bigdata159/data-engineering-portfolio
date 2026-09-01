def validate_data(df):

    errors = []

    if df.empty:
        errors.append("Dataset is empty")

    if "customer_id" in df.columns:
        if df["customer_id"].isnull().any():
            errors.append(
                "customer_id contains null values"
            )

    if df.duplicated().any():
        errors.append(
            "Duplicate records detected"
        )

    if errors:

        print("Data validation failed:")

        for error in errors:
            print(f"- {error}")

        return False

    print("Data validation passed")

    return True
