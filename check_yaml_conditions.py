"""Check YAML files for condition code mismatches."""
import yaml
from pathlib import Path

# Files to check
files_to_check = [
    'configs/analyses/from_1_ACC1.yaml',
    'configs/analyses/from_1.yaml',
    'configs/analyses/from1_to_any.yaml',
    'configs/analyses/from1_to_any_ACC1.yaml',
    'configs/analyses/from2_to_any.yaml',
    'configs/analyses/from2_to_any_ACC1.yaml',
    'configs/analyses/from3_to_any.yaml',
    'configs/analyses/from3_to_any_ACC1.yaml',
    'configs/analyses/from4_to_any.yaml',
    'configs/analyses/from4_to_any_ACC1.yaml',
]

print('=' * 80)
print('CHECKING from_X PATTERN FILES FOR CONDITION CODE MISMATCHES')
print('=' * 80)

errors_found = []

for file_path in files_to_check:
    p = Path(file_path)
    if not p.exists():
        continue

    with open(p, 'r') as f:
        config = yaml.safe_load(f)

    print(f'\nFile: {p.name}')
    print('-' * 60)

    for cond_set in config.get('selection', {}).get('condition_sets', []):
        name = cond_set.get('name', '')
        codes = cond_set.get('conditions', [])

        # Extract expected pattern from name
        if ' to ' in name:
            parts = name.split(' to ')
            if len(parts) == 2:
                expected_code = parts[0].strip() + parts[1].strip()
                actual_code = codes[0] if codes else 'MISSING'

                if expected_code == actual_code:
                    status = 'OK'
                else:
                    status = 'ERROR'
                    errors_found.append({
                        'file': p.name,
                        'condition_name': name,
                        'expected': expected_code,
                        'actual': actual_code
                    })

                print(f'  [{status}] {name:20s} -> codes={codes} (expected: ["{expected_code}"])')
            else:
                print(f'  [SKIP] {name:20s} -> codes={codes}')
        else:
            print(f'  [INFO] {name:20s} -> codes={codes}')

print('\n' + '=' * 80)
if errors_found:
    print(f'FOUND {len(errors_found)} ERRORS:')
    print('=' * 80)
    for err in errors_found:
        print(f'  File: {err["file"]}')
        print(f'    Condition: "{err["condition_name"]}"')
        print(f'    Expected code: "{err["expected"]}"')
        print(f'    Actual code: "{err["actual"]}"')
        print()
else:
    print('NO ERRORS FOUND!')
print('=' * 80)
