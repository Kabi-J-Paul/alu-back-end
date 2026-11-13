# alu-back-end

Projects for the ALU Back-End curriculum.

## API

Python scripts that access employee data via a REST API and export it to
different data structures (console, CSV, JSON).

### Files

| File | Description |
|------|-------------|
| `api/0-gather_data_from_an_API.py` | Gather TODO list progress from the API |
| `api/1-export_to_CSV.py` | Export an employee's TODO list to CSV |
| `api/2-export_to_JSON.py` | Export an employee's TODO list to JSON |
| `api/3-dictionary_of_list_of_dictionaries.py` | Export all employees' TODO lists to JSON |

### Usage

```bash
python3 api/0-gather_data_from_an_API.py <employee_id>
python3 api/1-export_to_CSV.py <employee_id>
python3 api/2-export_to_JSON.py <employee_id>
python3 api/3-dictionary_of_list_of_dictionaries.py
```

### Example

```bash
$ python3 api/0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```
