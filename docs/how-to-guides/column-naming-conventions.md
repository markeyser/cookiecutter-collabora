# Column Naming Conventions for ML/AI Projects

## Overview

To maintain consistency and readability in our project, we use the
"snake_case" naming convention for all column names in CSV, JSON, and
other data files. This guide provides a set of rules and examples to
help you name columns correctly, applicable to all types of data
including structured, semi-structured, and unstructured data.

## What is Snake_Case?

Snake_case is a naming convention where each word in a column name is
lowercase and separated by underscores (`_`). This format is widely used
in the Python ecosystem and ensures that column names are easily
readable and consistent.

## Rules for Snake_Case Column Naming

1. **Use Lowercase Letters**: All letters should be in lowercase.
2. **Separate Words with Underscores**: Use underscores (`_`) to
   separate words.
3. **Be Descriptive**: Column names should clearly indicate the contents
   or purpose of the column.
4. **Avoid Special Characters and Spaces**: Do not use spaces, hyphens,
   or any special characters other than underscores.

## Examples

### Structured Data (CSV File)

```csv
user_id, age, gender, purchase_amount, purchase_date
1, 34, "M", 45.67, "2023-05-12"
2, 29, "F", 78.90, "2023-05-13"
```

### Semi-Structured Data (JSON File)

```json
[
  {
    "user_id": 1,
    "age": 34,
    "gender": "M",
    "purchase_amount": 45.67,
    "purchase_date": "2023-05-12"
  },
  {
    "user_id": 2,
    "age": 29,
    "gender": "F",
    "purchase_amount": 78.90,
    "purchase_date": "2023-05-13"
  }
]
```

### Unstructured Data (Text with Metadata)

```json
{
  "documents": [
    {
      "doc_id": "12345",
      "title": "Analysis of Sales Data",
      "author": "John Doe",
      "content": "The sales data for Q1 shows a significant increase in revenue.",
      "timestamp": "2023-06-01T12:34:56Z"
    },
    {
      "doc_id": "12346",
      "title": "Customer Feedback Summary",
      "author": "Jane Smith",
      "content": "Customer feedback for Q1 has been overwhelmingly positive.",
      "timestamp": "2023-06-02T14:22:33Z"
    }
  ]
}
```

## Common Column Names in ML/AI Projects

- `user_id`
- `age`
- `gender`
- `purchase_amount`
- `purchase_date`
- `doc_id`
- `title`
- `author`
- `content`
- `timestamp`

## Tips

- **Keep it Short and Simple**: Aim for clarity but avoid overly long
  column names.
- **Use Consistent Terminology**: Use the same terms consistently across
  different columns (e.g., `timestamp` vs. `date_time`).
- **Context-Specific Names**: Tailor column names to the specific
  context and requirements of your project.

## Common Mistakes to Avoid

- **Uppercase Letters**: `UserID` (Incorrect)
- **Spaces**: `user id` (Incorrect)
- **Hyphens**: `user-id` (Incorrect)
- **Special Characters**: `user@id!` (Incorrect)

By following these guidelines, we ensure that our column names are
consistent, readable, and easy to work with in data processing and
analysis tasks, regardless of the type of data.