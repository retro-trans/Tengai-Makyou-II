"""Package verified local ISOs using Retro Trans Tools; no game files are uploaded."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--library', type=Path, required=True)
    parser.add_argument('--commit', required=True, help='Full translation/release source commit')
    args = parser.parse_args()
    from retro_trans.core import sha256_file
    from retro_trans.release import build_release, validate_directory
    from retro_trans.game_library import read, validate_registration
    root = Path(__file__).resolve().parents[1]
    provenance = json.loads((root/'release/provenance.json').read_text(encoding='utf-8'))
    for key, path in [('source', args.source), ('target', args.target)]:
        expected = provenance[key]
        if path.stat().st_size != expected['bytes'] or sha256_file(path) != expected['sha256']:
            parser.error('Incorrect ' + key + ' ISO identity')
    template = json.loads((root/'release/config.example.json').read_text(encoding='utf-8'))
    template['source_commit'] = args.commit
    template['patches'][0].update(source=str(args.source.resolve()), target=str(args.target.resolve()))
    library = read(args.library)
    validate_registration(template, 'retro-trans/Tengai-Makyou-II', library)
    with tempfile.TemporaryDirectory(prefix='tengai-release-') as temporary:
        config = Path(temporary)/'release-local.json'
        config.write_text(json.dumps(template, indent=2)+'\n', encoding='utf-8')
        build_release(config, args.out, library=library)
    validate_directory(args.out)
    print('Verified 0.8.0 patch and canonical release metadata:', args.out)

if __name__ == '__main__':
    main()
