#!/usr/bin/env python3
"""Retrieve examples by topic, prerequisite, technique, or free text."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic')
    parser.add_argument('--technique')
    parser.add_argument('--prerequisite')
    parser.add_argument('--text')
    parser.add_argument('--solutions', action='store_true')
    parser.add_argument('--list-tags', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    data = json.loads((root / 'metadata.json').read_text())
    records = data['examples']
    if args.list_tags:
        for field in ('topics', 'prerequisites', 'techniques'):
            print(field + ':')
            print('\n'.join('  ' + tag for tag in sorted(
                {tag for record in records for tag in record[field]})))
        return
    matched = []
    for record in records:
        filters = ((args.topic, 'topics'), (args.technique, 'techniques'),
                   (args.prerequisite, 'prerequisites'))
        if any(value and value.casefold() not in ' '.join(record[field]).casefold()
               for value, field in filters):
            continue
        search_fields = [record['id'], record['title'], record['file'],
                         *record['topics'], *record['prerequisites'],
                         *record['techniques']]
        if args.text and args.text.casefold() not in ' '.join(search_fields).casefold():
            continue
        matched.append(record)
        print(f"{record['id']}  {record['title']}")
        print(f"  {record['file']}")
        print('  topics: ' + ', '.join(record['topics']))
        print('  techniques: ' + ', '.join(record['techniques']))
        if args.solutions:
            print('  result: ' + str(record['result']))
    if not matched:
        print('No matching examples. Use --list-tags to inspect vocabulary.')


if __name__ == '__main__':
    main()
