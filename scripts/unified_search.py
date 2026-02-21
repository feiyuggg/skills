#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path('/Users/gudaiping/.openclaw/workspace')
SERPER_DIR = WORKSPACE / 'skills' / 'openclaw-serper'
BRAVE_DIR = WORKSPACE / 'skills' / 'brave-search'
BING_SCRIPT = WORKSPACE / 'skills' / 'bing-search' / 'scripts' / 'search.py'


def run_cmd(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def run_serper(query: str, mode: str):
    cmd = ['bash', '-lc', f'. .venv/bin/activate && python scripts/search.py -q {json.dumps(query)} --mode {mode}']
    code, out, err = run_cmd(cmd, cwd=SERPER_DIR)
    if code != 0:
        return False, {'provider': 'serper', 'error': err or out}
    return True, {'provider': 'serper', 'raw': out}


def run_brave(query: str, n: int, content: bool):
    flags = f'-n {n}' + (' --content' if content else '')
    cmd = ['node', 'search.js', query] + flags.split()
    code, out, err = run_cmd(cmd, cwd=BRAVE_DIR)
    if code != 0:
        return False, {'provider': 'brave', 'error': err or out}
    return True, {'provider': 'brave', 'raw': out}


def run_bing(query: str):
    cmd = ['python3', str(BING_SCRIPT), query]
    code, out, err = run_cmd(cmd)
    if code != 0:
        return False, {'provider': 'bing', 'error': err or out}
    return True, {'provider': 'bing', 'raw': out}


def main():
    ap = argparse.ArgumentParser(description='Unified search entry for serper/brave/bing')
    ap.add_argument('-q', '--query', required=True)
    ap.add_argument('--mode', choices=['default', 'current'], default='default')
    ap.add_argument('--provider', choices=['auto', 'serper', 'brave', 'bing'], default='auto')
    ap.add_argument('-n', type=int, default=5)
    ap.add_argument('--content', action='store_true', help='Brave only: include page content')
    args = ap.parse_args()

    if args.provider == 'serper':
        ok, data = run_serper(args.query, args.mode)
        print(json.dumps(data, ensure_ascii=False, indent=2))
        sys.exit(0 if ok else 1)

    if args.provider == 'brave':
        ok, data = run_brave(args.query, args.n, args.content)
        print(json.dumps(data, ensure_ascii=False, indent=2))
        sys.exit(0 if ok else 1)

    if args.provider == 'bing':
        ok, data = run_bing(args.query)
        print(json.dumps(data, ensure_ascii=False, indent=2))
        sys.exit(0 if ok else 1)

    # auto fallback chain
    chain = [('serper', lambda: run_serper(args.query, args.mode)),
             ('brave', lambda: run_brave(args.query, args.n, args.content)),
             ('bing', lambda: run_bing(args.query))]

    errors = []
    for name, fn in chain:
        ok, data = fn()
        if ok:
            data['mode'] = args.mode
            print(json.dumps(data, ensure_ascii=False, indent=2))
            return
        errors.append(data)

    print(json.dumps({'error': 'all providers failed', 'details': errors}, ensure_ascii=False, indent=2))
    sys.exit(1)


if __name__ == '__main__':
    main()
