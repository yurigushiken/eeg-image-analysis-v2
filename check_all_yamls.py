"""Comprehensive check of ALL YAML files for potential issues."""
import yaml
from pathlib import Path
from collections import defaultdict

yaml_dir = Path('configs/analyses')
all_yamls = list(yaml_dir.glob('*.yaml'))

print('=' * 80)
print(f'COMPREHENSIVE CHECK OF {len(all_yamls)} YAML FILES')
print('=' * 80)

errors = []
warnings = []
condition_registry = defaultdict(list)  # Track what each code means

for yaml_path in sorted(all_yamls):
    with open(yaml_path, 'r') as f:
        config = yaml.safe_load(f)

    for cond_set in config.get('selection', {}).get('condition_sets', []):
        name = cond_set.get('name', '')
        codes = cond_set.get('conditions', [])

        if not codes:
            warnings.append(f'{yaml_path.name}: Condition "{name}" has no codes!')
            continue

        code = codes[0]

        # Register this code with its name
        condition_registry[code].append({
            'file': yaml_path.name,
            'name': name,
            'response': cond_set.get('response', 'ALL')
        })

        # Check "X to Y" pattern consistency
        if ' to ' in name:
            parts = name.split(' to ')
            if len(parts) == 2:
                from_card = parts[0].strip()
                to_card = parts[1].strip()
                expected_code = from_card + to_card

                if expected_code != code:
                    errors.append({
                        'file': yaml_path.name,
                        'condition': name,
                        'code': code,
                        'expected': expected_code,
                        'reason': f'Name "{name}" implies code "{expected_code}" but uses "{code}"'
                    })

# Report errors
if errors:
    print(f'\nFOUND {len(errors)} ERRORS:')
    print('=' * 80)
    for err in errors:
        print(f'File: {err["file"]}')
        print(f'  Condition: "{err["condition"]}"')
        print(f'  Code: "{err["code"]}" (expected: "{err["expected"]}")')
        print(f'  Reason: {err["reason"]}')
        print()
else:
    print('\nNO ERRORS FOUND!')

# Check for ambiguous condition codes (same code used with different names)
print('\n' + '=' * 80)
print('CHECKING FOR AMBIGUOUS CONDITION CODES:')
print('=' * 80)

ambiguous_found = False
for code, usages in sorted(condition_registry.items()):
    unique_names = set(u['name'] for u in usages)
    if len(unique_names) > 1:
        ambiguous_found = True
        print(f'\nCode "{code}" has MULTIPLE different names:')
        for usage in usages:
            print(f'  - "{usage["name"]}" in {usage["file"]} (response={usage["response"]})')

if not ambiguous_found:
    print('No ambiguous codes found!')

# Summary
print('\n' + '=' * 80)
print(f'Total YAML files checked: {len(all_yamls)}')
print(f'Total condition codes found: {len(condition_registry)}')
print(f'Errors: {len(errors)}')
print(f'Warnings: {len(warnings)}')
print('=' * 80)
